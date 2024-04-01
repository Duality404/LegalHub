
import requests
from bs4 import BeautifulSoup
import re
from flask_app.database import connection

base_url = 'https://www.livelaw.in/top-stories'

def get_url():
    connection.execute("delete from top_stories_url")
    j=0
    i=0
    flag=True
    
    while flag:
        i=i+1
        if i==1:
            url = base_url
        else:
            url=f"{base_url}/{i}"
            

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = {link.get('href') for link in soup.find_all('a') if link.get('href') and re.search(r'^/top-stories/', link.get('href'))}
            
            for x in links:
                j=j+1
                x = x.replace('/top_stories','')
                connection.execute(f"INSERT INTO top_stories_url(urlid,url)values('{j}','{x}')")

                if(j>=60):
                    flag=False
                    break

def get_url_data():
    connection.execute('delete from top_stories')
    data = connection.execute("select * from top_stories_url")
    for url in data:
        url = url[1]
        url = base_url + url

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            header = None
            for heading in soup.find_all('h1', class_='heading_for_first'):
                header = heading.decode_contents()
                break
            header = header.replace('\"',"\'")
            header= re.sub(r'[^\w\s]', '', header)

            author = None
            for author_tag in soup.find_all('a', class_='author-name'):
                h6_tags = author_tag.find('h6')
                author = h6_tags.decode_contents()
                break
            author = author.replace('\"',"\'")
            author= re.sub(r'[^\w\s]', '', author)

            date = None
            for _ in soup.find_all('p', class_='date'):
                date = _.decode_contents()
                break
            date = date.replace('\"',"\'")


            content_ = ''
            for author_tag in soup.find_all('div', class_='details-story-wrapper'):
                p_tags = author_tag.find_all('p')
                counter = 0
                for p in p_tags:
                    if counter > 2:
                        break
                    counter +=1
                    content_ += p.decode_contents()
                break
            content_ = content_.replace('\'',"\"")
            content_= re.sub(r'[^\w\s]', '', content_)
            

            src = None
            for image_tag  in soup.find_all('div', class_='news_details_img1'):
                content = image_tag.decode_contents()
                # img_tag = image_tag.find('img')

                # Regular expression pattern to match image URLs
                image_pattern = r'src="([^"]+)"[^>]*'
                # Find all matches of the pattern in the sample string
                matches = re.findall(image_pattern, content)
                src = matches[0].replace('\"',"\'")
                break
            connection.execute(f'''
            insert into top_stories(img_link, heading, author, date, content,url)
            values('{src}','{header}','{author}','{date}', '{content_[:269]}','{url}')
            ''')
        
get_url()
get_url_data()