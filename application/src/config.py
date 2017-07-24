from pymongo import MongoClient
from redis import ConnectionPool
from redis import StrictRedis
import cherrypy

client = None
cache_pool = None


def get_db_connection():
    if not globals()['client']:
        globals()['client'] = MongoClient(host='localhost',max_pool_size=1)
    db = globals()['client']["BIOMARKERS"]
    return db

def get_cache_connection():
    return StrictRedis(connection_pool = globals()['cache_pool'])

def configure(max_db_pool_size = 2, max_redis_connections = 2):
    if not globals()['client']:
        cherrypy.log("Starting DB Connection Pool, host: " + cherrypy.config["server.mongo_host"])
        client = MongoClient(host = cherrypy.config["server.mongo_host"], port = cherrypy.config["server.mongo_port"], max_pool_size = max_db_pool_size)
        globals()['client'] = client
        
    if not globals()['cache_pool']:
        cherrypy.log("Connecting to Redis Cache Server....")
        cache_pool = ConnectionPool(host = 'localhost', port = 6379, db = 0, max_connections = max_redis_connections)
        globals()['cache_pool'] = cache_pool