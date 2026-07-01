from fastapi import FastAPI

import apis.url 
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the URL Shortener API!"}

@app.get("/{short_url}")
async def get_url(short_url: str):
    url = await apis.url.get_url_from_redis(short_url)
    if not url:
        return {"error": "URL not found"}
    return {"url": url}