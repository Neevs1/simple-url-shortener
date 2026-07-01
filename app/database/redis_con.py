import redis

def get_redis_client():
    return redis.Redis(host='localhost', port=6379, db=0)

def set_key_value(key, value):
    r = get_redis_client()
    r.set(key, value)

def get_value(key):
    r = get_redis_client()
    return r.get(key)
'''
Testing phase code to check if Redis is working properly
r = get_redis_client()
r.set('test_key', 'test_value')
value = r.get('test_key')
print(value)
'''
