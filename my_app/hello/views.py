from flask import Blueprint , render_template , request
from my_app.hello.models import Product
from my_app import db

hello = Blueprint ( 'hello' , __name__ )
@hello.route ('/')
def index ():
  return render_template ('index.html')

@hello.route ('/nba')
def nba ():
  return render_template('nba.html')

@hello.route ('create-product' , methods=['POST'])
def create_product():
  name = request.form.get('name')
  product = Product(name)
  db.session.add(product)
  db.session.commit()
  return"创建成功"