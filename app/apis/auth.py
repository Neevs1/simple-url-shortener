import sys
sys.path.append("..")
import models.user as user
from database.postgres import connect_to_db 
from pwdlib import PasswordHash
from sqlalchemy import text

async def create_user(user: user.UserCreate):
    connection = connect_to_db()
    with connection.connect() as conn:
        conn.execute(
            text("""
            INSERT INTO users (username, email, password_hash)
            VALUES (:username, :email, :password_hash)
        """),
        {
            "username": user.username,
            "email": user.email,
            "password_hash": PasswordHash.recommended().hash(user.password),
        },
        )
        conn.commit()

async def login(email: str, password: str):
    connection = connect_to_db()
    with connection.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM users WHERE email = :email"),
            {"email": email}
        )
        user = result.fetchone()
        if user and PasswordHash.recommended().verify(password, user.password):
            return user
    return None