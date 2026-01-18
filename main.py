from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Izinkan Frontend (HTML kamu) mengakses API ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATA MODELS ---
class News(BaseModel):
    id: int
    title: str
    category: str
    summary: str
    content: str
    image: str

class Reply(BaseModel):
    user: str
    text: str

class Post(BaseModel):
    id: int
    author: str
    content: str
    replies: List[Reply] = []

# --- DATABASE SEDERHANA (In-Memory) ---
db_news = [
    {
        "id": 1, 
        "title": "Kemenangan Diplomatik PBB 2026", 
        "category": "Kabar Gembira", 
        "summary": "Dukungan dunia meningkat.",
        "content": "Laporan dari markas besar PBB menunjukkan hasil positif...",
        "image": "https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?w=800"
    }
]

db_forum = []

# --- ENDPOINTS ---

@app.get("/")
def home():
    return {"status": "AMANAH API is Running", "version": "1.0"}

@app.get("/news", response_model=List[News])
def get_news():
    return db_news

@app.post("/forum")
def create_post(post: Post):
    db_forum.append(post.dict())
    return {"message": "Post success", "data": post}

@app.get("/forum")
def get_forum():
    return db_forum

@app.post("/forum/{post_id}/reply")
def add_reply(post_id: int, reply: Reply):
    for post in db_forum:
        if post["id"] == post_id:
            post["replies"].append(reply.dict())
            return {"message": "Reply added"}
    return {"error": "Post not found"}