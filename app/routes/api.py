from flask import Blueprint, request, jsonify, session 
# here the request object is being imported to hold the information for the POST request
from app.models import User
from app.db import get_db
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    # print(data) # once the request.get_json() returns an object that then gets printed, we can then pass that object to a new User model instead
    db = get_db()

    try:
      # attempt creating a new user
      newUser = User(
          username = data['username'],
          email = data['email'],
          password = data['password']
      )

      # save in database
      db.add(newUser)
      db.commit()
    except:
       print(sys.exe_info()[0])
       # insert failed, so rollback and send error to front end
       db.rollback()
       return jsonify(message = 'Signup failed'), 500
       # response status code set to 500 to signify a server error occurred

    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True
    return jsonify(id = newUser.id)
# this post route will resolve in /api/users and will be a POST method so to receive data it needs to capture the data

@bp.route('/users/logout', methods=['POST'])
def logout():
   # remove session variables
   session.clear()
   return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
   data = request.get_json()
   db = get_db()

   try:
      user = db.query(User).filter(User.email == data['email']).one()
   except:
      print(sys.exc_info()[0])

      return jsonify(message = 'Incorrect credentials'), 400
   
   if user.verify_password(data['password']) == False:
      return jsonify(message = 'Incorrect credentials'), 400
   
   session.clear()
   session['user_id'] = user.id
   session['loggedIn'] = True

   return jsonify(id = user.id)