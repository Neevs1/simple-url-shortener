

import sys
sys.path.append("..")
import database.redis_con as rd
import database.postgres as pg

async def get_url_from_redis(short_url: str):
    value = rd.get_value(short_url)
    if value:
        return value.decode('utf-8')
    return None