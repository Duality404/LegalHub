
from flask_app import app
from config import *
import threading
from time import sleep
from news import get_url, get_url_data

# def get_top_news():
#     print("Getting urls")
#     get_url()
#     print("Url loaded..., loading url data")
#     get_url_data()
#     print("All data loaded and uploaded")
#     time = 60*60*24
#     print("Sleeping for a day")
#     sleep(time)

app.config['SECRET_KEY'] = api_secret

if __name__ == '__main__':
    # update_top_news = threading.Thread(target=get_top_news).start()
    app.run(debug = True, port=8000)