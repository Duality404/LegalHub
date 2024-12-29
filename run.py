
# from gevent import monkey 
# monkey.patch_all()
# from gevent.pywsgi import WSGIServer
from flask_app import app
from config import *
import threading
from time import sleep
from news import *
from flask_app.database import connection

def get_top_news():
    connection.execute('delete from top_stories')
    print("Deleted the previous data")
    get_url()
    sleep(1000)

app.config['SECRET_KEY'] = api_secret

if __name__ == '__main__':
    
    # update_top_news = threading.Thread(target=get_top_news).start()
    app.run(debug = True,port=8000)
    # WSGIServer(("127.0.0.1",8000),app,log=None).serve_forever()