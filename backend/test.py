import redis
import os

PASSWORD = os.getenv("REDIS_PASSWORD", "")
if PASSWORD == "":
    raise Exception("REDIS_PASSWORD was not SET")

r = redis.Redis()

r.set("hey", "aaa")

print(r.get("hey"))
