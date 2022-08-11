"""Flask app for Cupcakes"""
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)
