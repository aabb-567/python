from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:0506@localhost/test'
db = SQLAlchemy(app)
from my_app.hello.views import hello
app.register_blueprint(hello)

db.create_all()