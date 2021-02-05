from my_app import db

class Product(db.Model):
  id = db.Column(db.Integer , primary_key = True)
  name = db.Column(db.String(255))
  
  def __name__ (self,name):
    self.name=name