from os import getenv
# getenv() function is part of Python's built in os module
from sqlalchemy.ext.declarative import declarative_base
# engine variable manages the overall connection to the database
from sqlalchemy import create_engine
# session variable creates temporary connections for performing CRUD operations
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# first call load_dotenv() from python-dotenv module as we've used the .env file to fake the environment variable
load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()