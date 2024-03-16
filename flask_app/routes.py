
from flask import get_flashed_messages, request, Blueprint, url_for, render_template, redirect, abort,flash
from .database import connection
from functools import wraps
from datetime import datetime, timedelta

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
    return render_template('signup.html')

@main.route('/signup', methods=["POST"])
def register_post():
    
    # data validate
    user_found = 0
    validate = 1

    if user_found:
        return redirect('/signin')
    if not validate:
        return redirect('/signup')
    
    return redirect('/')
    
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
    print(data)

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
        response.set_cookie('user_id', user_id, expires=date_)
        return response
    
    else:
        print('redirecting to login')
        return redirect('/login')


@main.route('/logout')
def logout():
    reponse = redirect('/')
    reponse.set_cookie('user_id', '', expires=0)
    return reponse
