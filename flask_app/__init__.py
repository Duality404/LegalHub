from flask import Flask, Blueprint
app= Flask(__name__, template_folder = 'templates', static_folder = 'static' )


from flask_app.routes import main
app.register_blueprint(main)

