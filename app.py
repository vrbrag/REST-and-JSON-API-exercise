"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app=Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def list_all_cupcakes():
   """Show list of all cupcakes"""

   cupcakes = Cupcake.query.all()
   serialized = [cupcake.serialize_cupcake() for cupcake in cupcakes]
   return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
   """Get data on single cupcake"""

   cupcake = Cupcake.query.get_or_404(cupcake_id)
   return jsonify(cupcake=cupcake.serialize_cupcake())