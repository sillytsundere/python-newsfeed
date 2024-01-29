# import functions Blueprint and render_template from Flask module
from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# add the @bp.route decorator to turn the following function into a route
# whatever the function returns will be the response for the route
# the render template function returns a template instead of a string like the "hello world" variation
@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')

# this route takes a parameter
@bp.route('/post/<id>')
# to capture the value we include it as a function parameter
def single(id):
    return render_template('single-post.html')

