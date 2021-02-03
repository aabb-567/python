from flask import Blueprint , render_template
hello = Blueprint ( 'hello' , __name__ )
@hello.route ('/')
def index ():
  return render_template ('index.html')

@hello.route ('/nba')
def nba ():
  return render_template('nba.html')