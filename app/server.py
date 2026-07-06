from fastapi import FastAPI, APIRouter

import apis.url 
import database.postgres as postgres
app = FastAPI()

api_router = APIRouter(prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the URL Shortener API!"}

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

app.include_router(api_router)