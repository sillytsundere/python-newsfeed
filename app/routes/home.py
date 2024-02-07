# import functions Blueprint and render_template from Flask module
from flask import Blueprint, render_template, session, redirect

from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

# add the @bp.route decorator to turn the following function into a route
# whatever the function returns will be the response for the route
# the render template function returns a template instead of a string like the "hello world" variation
@bp.route('/')
def index():
    # get all posts
    db = get_db()
    # get a session connection that is tied to this route's context
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    # query method is used on the connection object to query the Post model for all posts in descending order and saved in posts variable

    return render_template(
        'homepage.html',
        posts=posts,
        loggedIn=session.get('loggedIn')
    )

@bp.route('/login')
def login():
    # not logged in yet
    if session.get('loggedIn') is None:
        return render_template('login.html')
    
    return redirect('/dashboard')

# this route takes a parameter
@bp.route('/post/<id>')
# to capture the value we include it as a function parameter
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()
    # here the filter method is used on the connection object to specify the SQL WHERE clause, and the one() method is used, instead of all()

    # render single post template
    return render_template(
        'single-post.html',
        post=post,
        loggedIn=session.get('loggedIn')
    )
    # here the single 'post' object is passed to the single-post.html template

# once the template is rendered and the response sent the contect for this route terminates and the teardown function from init_db() closes the database connection

