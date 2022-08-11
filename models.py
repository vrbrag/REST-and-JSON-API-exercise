"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()

DEFAULT_IMG =  'https://tinyurl.com/demo-cupcake'
class Cupcake(db.Model):
   """Cupcakes"""

   __tablename__= "cupcakes"

   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   flavor = db.Column(db.Text, nullable = False)
   size = db.Column(db.Text, nullable = False)
   rating = db.Column(db.Float, nullable = False)
   image = db.Column(db.Text)

   def image_url(self):
      """Return image for cupcake"""

      return self.image or DEFAULT_IMG

def connect_db(app):
   db.app = app
   db.init_app(app)