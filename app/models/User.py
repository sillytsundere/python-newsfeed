from app.db import Base
from sqlalchemy import Column, Integer, String
# these classes from sqlalchemy are used to define table columns and their data types as well as options, (is it nullable? SQL NOT NULL)
from sqlalchemy.orm import validates
import bcrypt 

salt = bcrypt.gensalt()

# User class inherits from the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    # declare properties that the Base class will use to make the table

    @validates('email')
    def validate_email(self, key, email):
        # make sure email address contains @ character
        assert '@' in email
        # assert keyword automatically throws error if false, which prevents the return statement form happening

        return email
    
    @validates('password')
    def validate_pasword(self, key, password):
        assert len(password) > 4
        # checks length of the password and throws error if length is 4 characters or less

        #encrypt password
        return bcrypt.hashpw(password.encode('utf-8'), salt)
        # if assert doesnt throw an error the validate_pw function now returns an encrypted password