import os

class Config(object):
    REDIS_PORT=os.environ["REDIS_PORT"]
    REDIS_HOST=os.environ["REDIS_HOST"]
    REDIS_DB=os.environ["REDIS_DB"]
    REDIS_URL=os.environ["REDIS_URL"]
    CACHE_DEFAULT_TIMEOUT=os.environ["CACHE_DEFAULT_TIMEOUT"]
    CACHE_TYPE=os.environ["CACHE_TYPE"]
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]
