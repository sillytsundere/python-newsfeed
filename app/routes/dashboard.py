from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
# with this url prefex, every route in this blueprint will begin with '/dashboard'
# the routes will then be /dashboard and /dashboard/edit/<id> when registered with the app

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')

# this file is a module, like the home.py file/module
#thus every variable or function can be imported elsewhere