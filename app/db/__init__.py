from os import getenv
# getenv() function is part of Python's built in os module
from sqlalchemy.ext.declarative import declarative_base
# engine variable manages the overall connection to the database
from sqlalchemy import create_engine
# session variable creates temporary connections for performing CRUD operations
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# first call load_dotenv() from python-dotenv module as we've used the .env file to fake the environment variable
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)

# def get_db():
#     return Session()
#     # when this function is called it returns a new session-connection object
    
def get_db():
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()

    return g.db
# now the get_db() function saves the current connection on the g object, if it is not already there
# then it returns the connection from the g object instead of creating a new Session instance each time

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# pop method attempts to find and remove db from the g object
# if db exists (if db doesnt equal None) then db.close will end the connection
# need to tell flask to run close_db when a context is destroyed