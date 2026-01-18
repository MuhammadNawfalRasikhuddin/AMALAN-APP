from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import feedparser # Library untuk ambil berita real-time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "API Amanah Real-Time Active"}

@app.get("/news")
def get_real_news():
    # Mengambil RSS Feed berita Muslim (Contoh: Republika Khazanah)
    url = "https://www.republika.co.id/rss/khazanah/"
    feed = feedparser.parse(url)
    
    real_news = []
    for i, entry in enumerate(feed.entries):
        # Mengambil link gambar dari entry jika ada, jika tidak pakai placeholder
        image_url = "https://picsum.photos/800/400" 
        if 'links' in entry:
            for link in entry.links:
                if 'image' in link.get('type', ''):
                    image_url = link.get('href')

        real_news.append({
            "id": i + 1,
            "title": entry.title,
            "category": "Kabar Muslim",
            "summary": entry.summary[:100] + "...", # Potong ringkasan agar rapi
            "content": entry.summary,
            "image": image_url,
            "link": entry.link
        })
    
    return real_news

# Jalankan: uvicorn main:app --reload