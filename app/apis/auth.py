import sys
sys.path.append("..")
import models.user as user
from database.postgres import connect_to_db 

async def create_user(user: user.User):
    connection = connect_to_db()
    with connection.connect() as conn:
        conn.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (user.email, user.password)
        )

async def login(email: str, password: str):
    connection = connect_to_db()
    with connection.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        return result.fetchone()