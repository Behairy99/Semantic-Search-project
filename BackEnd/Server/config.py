from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    #### DATABASE
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOSTNAME = os.getenv('DATABASE_HOSTNAME')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    SQLALCHEMY_DATABASE_URI = F'postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    #### Caching
    CACHE_TYPE = os.environ['CACHE_TYPE']
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    # CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
