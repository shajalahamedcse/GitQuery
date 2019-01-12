import redis
import os

class RedisCache:
    """RedisCache for config"""
    def __init__(self):
        self.redis_host = "localhost"
        self.redis_port = 6379
        self.redis_password = ""

    #create the Redis Connection object
    def connect(self):
        try:
            connection_pool = redis.ConnectionPool(host=self.redis_host, port=self.redis_port, password=self.redis_password)
            return redis.StrictRedis(connection_pool=connection_pool)
        except Exception as error:
            print(error)
