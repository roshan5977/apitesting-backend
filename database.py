from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Set default values for local development
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "harbinger_apitesting_db"

# Override with AWS environment variables if available
if "DB_USER" in os.environ:
    DB_USER = os.environ["DB_USER"]
if "DB_PASSWORD" in os.environ:
    DB_PASSWORD = os.environ["DB_PASSWORD"]
if "DB_HOST" in os.environ:
    DB_HOST = os.environ["DB_HOST"]
if "DB_NAME" in os.environ:
    DB_NAME = os.environ["DB_NAME"]

SQLALCHEMY_database_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


engine = create_engine(url=SQLALCHEMY_database_URL)


Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
