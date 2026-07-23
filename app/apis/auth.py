import sys
sys.path.append("..")
import models.user as user
from database.postgres import connect_to_db 
from pwdlib import PasswordHash

async def create_user(user: user.UserCreate):
    
    connection = connect_to_db()
    with connection.connect() as conn:
        conn.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (user.username, user.email, PasswordHash.recommended().hash(user.password))
        )

async def login(email: str, password: str):
    connection = connect_to_db()
    with connection.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = result.fetchone()
        if user and PasswordHash.recommended().verify(password, user.password):
            return user
    return None