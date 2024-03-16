
from flask_app import app
from config import *

app.config['SECRET_KEY'] = api_secret

if __name__ == '__main__':
    app.run(debug = True, port=8000)