from pydantic import BaseModel

class ShortUrl(BaseModel):
    id: int
    original_url: str
    short_code: str
    created_at: str
    updated_at: str
    created_by: str
    clicks: int