from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return "<h1>Landing</h1>"

@views.route('/home')
def home():
    return "<h1>Home</h1>"

@views.route('/stats')
def stats():
    return "<h1>Stats</h1>"

@views.route('/inspiration')
def inspiration():
    return "<h1>Inspiration</h1>"
