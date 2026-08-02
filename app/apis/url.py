import sys
sys.path.append("..")
import database.redis_con as rd
import database.postgres as pg
import models.user as user

async def get_url_from_redis(short_url: str):
    value = rd.get_value(short_url)
    if value:
        return value.decode('utf-8')
    return None

async def get_url_from_postgres(short_url: str):
    connection = pg.connect_to_db()
    with connection.connect() as conn:
        result = conn.execute("SELECT original_url FROM urls WHERE short_code = %s", (short_url,))
        row = result.fetchone()
        if row:
            return row[0]
    return None

async def get_url(short_url: str):
    url = await get_url_from_redis(short_url)
    if url:
        return url
    url = await get_url_from_postgres(short_url)
    if url:
        rd.set_key_value(short_url, url)
        rd.expire(short_url, 604800)
        return url
    return None

async def save_url(original_url:str, user:user.User):
    connection = pg.connect_to_db()
    with connection.connect() as conn:
        result = conn.execute("INSERT INTO urls (original_url, user_id) VALUES (%s, %s) RETURNING short_code", (original_url, user.id))
        short_code = result.fetchone()[0]
        rd.set_key_value(short_code, original_url)
        rd.expire(short_code, 604800)
        return short_code