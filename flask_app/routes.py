
import re
from flask import get_flashed_messages, request, Blueprint, url_for, render_template, redirect, abort,flash
from .database import connection
from functools import wraps
from datetime import datetime, timedelta
from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
    user_id_cookie = request.cookies.get('user_id')
    name=None
    if user_id_cookie:
     uidcookie=int(user_id_cookie)
     username=connection.execute(f'SELECT username from users where userid= {uidcookie}')
     if username:
            name = username[0][0]
     else:
            redirect('/ logout')
    else:
        print("User is not logged in")

    return render_template('home.html', data={'name': name})


@main.route('/login')
def login():
    message = None
    try:
        message = get_flashed_messages()
        print(message)
    except:
        pass
    return render_template('login.html', message = message)

@main.route('/signup')
def signup():
    message = None
    try:
        message = get_flashed_messages()
        print(message)
    except:
        pass
    return render_template('signup.html', message = message)


@main.route('/signup', methods=["POST"])
def register_post():
    
    user_name=request.form.get('username')
    fname=request.form.get('fname')
    lname=request.form.get('lname')
    email=request.form.get('email')
    password=request.form.get('password')
    data=connection.execute('select * from users')
    dup=0
    dup2=0
    for x in data:
        if x[1]==user_name:
            dup=1
            break
    if dup==1:
        flash('Choose a different username please')
        return redirect('/signup')
    for x in data:
        if x[4]==email:
            dup2=1
            break
    if dup2==1:
        flash('Email already exists please sign in')
        return redirect('/signup')
    if dup==0:
        if is_valid_email(email)==False:
            flash('Please specify a valid email address.')
            return redirect('/signup')  
        if is_strong_password(password)==False:
            flash('Password should be of 8 characters minimum with one of special,lower and upper characters and number')
            return redirect('/signup')
        if is_valid_email(email) and is_strong_password(password):
            connection.execute(f"INSERT into users(username,firstname,lastname,email,password)values('{user_name}','{fname}','{lname}','{email}','{password}')")
            uid=connection.execute(f"SELECT userid from users where username='{user_name}' ")[0][0]
            print(uid)
            user_id = str(uid)
            response = redirect('/')
            print('redirecting to homepage')
            date_ = datetime.now() + timedelta(days = 7)
            response.set_cookie('user_id', user_id, expires=date_)
            return response
    
def is_strong_password(password):
    return all([
        len(password) >= 8,
        re.search(r'[A-Z]', password),
        re.search(r'[a-z]', password),
        re.search(r'\d', password),
        re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password)
    ])

def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
        
    
    
    
@main.route('/login', methods = ["POST"])
def login_post():
    # extract data from form
    user_name = request.form.get('username')
    password=request.form.get('password')
    print(user_name,password)
    # authenticate
    uid=0
    user_found=0
    password_correct=0
    authenticate = 0
    data= connection.execute('select * from users')
    

    for x in data:
        if x[1]==user_name:
            user_found=1
            if x[5]==password:
                password_correct=1
                authenticate=1
                uid=x[0]

    if user_found== 0 or password_correct==0:
        flash('Username or password is incorrect')
        return redirect('/login')
    
    if authenticate==1:
        user_id = str(uid)
        response = redirect('/')
        print('redirecting to homepage')
        date_ = datetime.now() + timedelta(days = 7)
        print("user_id value : ", user_id)
        response.set_cookie('user_id', user_id, expires=date_)
        return response
    
    else:
        print('redirecting to login')
        return redirect('/login')


@main.route('/forgot')
def forgot():
    message = None
    try:
        message = get_flashed_messages()
        print(message)
    except:
        pass
    return render_template('forgot.html',message=message)
    
@main.route('/forgot', methods = ["POST"])
def forgot_post():
    # extract data from form
    email= request.form.get('email')
    password=request.form.get('new-password')
    conf=request.form.get('confirm-password')
    # authenticate
    uid=0
    user_found=0
    email_flag=1
    strong=1
    password_correct=1
    data= connection.execute('select * from users')
    
    if is_valid_email(email)==False:
        email_flag=0
        flash('Email is of invalid format')     
        return redirect('/forgot')

    if email_flag==1:
     for x in data:
         if x[4]==email:
             user_found=1
             uid=x[0]
            
    if user_found== 0:
     flash('Email is incorrect')
     return redirect('/forgot')
    
    if is_strong_password(password)==False:
        strong=0
        flash('Password should be of 8 characters minimum with one of special,lower and upper characters and number') 
        return redirect('/forgot')
    
    
    if strong==1:
     if password!=conf:
         password_correct=0
         flash("Passwords don't match")
         return redirect('/forgot')
    
    if user_found==1 and password_correct==1:
        connection.execute(f"update users set password='{password}' where userid={uid} ")
        flash("Password updated succesfully")
        return redirect('/login')
    
def is_strong_password(password):
    return all([
        len(password) >= 8,
        re.search(r'[A-Z]', password),
        re.search(r'[a-z]', password),
        re.search(r'\d', password),
        re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password)
    ])

def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


@main.route('/logout')
def logout():
    reponse = redirect('/')
    reponse.set_cookie('user_id', '', expires=0)
    return reponse

@main.route('/news')
def news():
    news_stories=connection.execute("select * from top_stories")
    
    user_id_cookie = request.cookies.get('user_id')
    name=None
    if user_id_cookie:
     uidcookie=int(user_id_cookie)
     username=connection.execute(f'SELECT username from users where userid= {uidcookie}')
     if username:
            name = username[0][0]
     else:
            redirect('/ logout')
    else:
        print("User is not logged in")

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    
    
    pagination = Pagination(page=page, total=len(news_stories), search=search,per_page=6, record_name='news_stories')

    return render_template('news.html', data={'name': name}, news = news_stories,pagination=pagination, page = page, per_page = 6)

@main.route('/lawyers')
def lawyers():
   user_id_cookie = request.cookies.get('user_id')
   name=None
   if user_id_cookie:
     uidcookie=int(user_id_cookie)
     username=connection.execute(f'SELECT username from users where userid= {uidcookie}')
     if username:
            name = username[0][0]
     else:
            redirect('/ logout')
   else:
        print("User is not logged in")

   lawyers=connection.execute("Select * from lawyers")
   return render_template('lawyers.html', data={'name': name},lawyers=lawyers)

@main.route('/resume/<lawyer_id>')
def resume(lawyer_id):
   user_id_cookie = request.cookies.get('user_id')
   name=None
   if user_id_cookie:
     uidcookie=int(user_id_cookie)
     username=connection.execute(f'SELECT username from users where userid= {uidcookie}')
     if username:
            name = username[0][0]
     else:
            redirect('/ logout')
   else:
        print("User is not logged in")
   lawyer_details=connection.execute(f'select * from lawyers where lawyer_id={lawyer_id}')
   if lawyer_details:
        lawyer_details = lawyer_details[0]
        return render_template('resume.html',data={'name':name},lawyer_details=lawyer_details)
   else:
       return redirect('/not-found')

@main.route('/documents')
def documents():
 user_id_cookie = request.cookies.get('user_id')
 name=None
 if user_id_cookie:
     uidcookie=int(user_id_cookie)
     username=connection.execute(f'SELECT username from users where userid= {uidcookie}')
     if username:
            name = username[0][0]
     else:
            redirect('/ logout')
 else:
        print("User is not logged in")
 documents=connection.execute('Select * from documents')
 return render_template('documents.html',data={'name':name},documents=documents)

@main.route('/iframe/<doc_id>')
def iframe(doc_id):
   
   doc_path=connection.execute(f'select title from documents where id={doc_id}')
   print(doc_path)
   if doc_path:
        doc_path = doc_path[0][0]
        print(doc_path)
        return render_template('iframe.html',doc_path=doc_path)
   else:
       return redirect('/not-found')

 