from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
import apis.url, apis.auth
import database.postgres as postgres
import database.redis_con as redis_con
import models.user as user
app = FastAPI()

api_router = APIRouter(prefix="/api")
auth_router = APIRouter(prefix="/auth")

@app.get("/",response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head>
        <title>URL Shortener API</title>
    </head>
    <body>
        <h1>Welcome to the URL Shortener API</h1>
        <p>visit <a href="/docs">/docs</a> for API documentation.</p>
    </body>
    </html>
"""
@auth_router.post("/create_user")
async def create_user(user: user.UserCreate):
    await apis.auth.create_user(user)
    return {"message": "User created successfully"}

@auth_router.post("/login")
async def login(user: user.UserLogin):
    token = await apis.auth.login(user)
    if token:
        return {"access_token": token}
    return {"error": "Invalid credentials"}

@app.get("/{short_url}")
async def get_url(short_url: str):
    url = await apis.url.get_url_from_redis(short_url)
    if not url:
        return {"error": "URL not found"}
    return {"url": url}

@api_router.get("/testdbcon")
async def testdbcon():
    try:
        postgres.test_connection()
        return {"message": "Database connection successful!"}
    except Exception as e:
        return {"error": str(e)}

@api_router.get("/testrediscon")
async def testrediscon():
    try:
        redis_test = redis_con.get_redis_client()
        redis_test.set('test_key', 'test_value')
        value = redis_test.get('test_key')
        return {"message": "Redis connection successful!", "test_value": value}
    except Exception as e:
        return {"error": str(e)}

@api_router.post("/shorten_url")
async def shorten_url(original_url: str, user: user.User):
    short_url = await apis.url.save_url(original_url, user)
    return {"short_url": short_url}

app.frontend("/service", directory="frontend", fallback="index.html")

app.include_router(api_router)
app.include_router(auth_router)