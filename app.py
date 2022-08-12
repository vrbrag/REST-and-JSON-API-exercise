"""Flask app for Cupcakes"""
from crypt import methods
import json
from flask import Flask, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app=Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def route():
   """Homepage"""
   cupcakes = Cupcake.query.all()
   return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def list_all_cupcakes():
   """Show list of all cupcakes"""

   cupcakes = [cupcake.serialize_cupcake() for cupcake in Cupcake.query.all()]
   return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
   """Get data on single cupcake"""

   cupcake = Cupcake.query.get_or_404(cupcake_id)
   return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
   """Create a new cupcake"""

   new_cupcake = Cupcake(
      flavor=request.json["flavor"],
      size=request.json["size"],
      rating=request.json["rating"],
      image=request.json["image"] or None)

   db.session.add(new_cupcake)
   db.session.commit()
   return (jsonify(cupcake=new_cupcake.serialize_cupcake()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
   """Update cupcake of the id passed"""

   cupcake = Cupcake.query.get_or_404(cupcake_id)

   cupcake.flavor = request.json.get('flavor', cupcake.flavor)
   cupcake.size = request.json.get('size', cupcake.size)
   cupcake.rating = request.json.get('rating', cupcake.rating)
   cupcake.image = request.json.get('image', cupcake.image)

   db.session.add(cupcake)
   db.session.commit()
   return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
   """Delete cupcake of the id passed"""

   cupcake = Cupcake.query.get_or_404(cupcake_id)
   db.session.delete(cupcake)
   db.session.commit()
   return jsonify(message = "Deleted")