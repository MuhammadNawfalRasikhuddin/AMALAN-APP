from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import feedparser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/news")
def get_real_news():
    # Daftar berbagai sumber berita Muslim agar jumlahnya banyak
    sources = [
        "https://www.republika.co.id/rss/khazanah/",
        "https://www.republika.co.id/rss/dunia-islam/",
        "https://www.antaranews.com/rss/lifestyle/haji-umroh",
        "https://www.tempo.co/rss/dunia"
    ]
    
    all_combined_news = []
    
    for url in sources:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            # Gunakan gambar placeholder jika RSS tidak menyediakan gambar
            image_url = "https://picsum.photos/seed/" + entry.title[:5] + "/800/400"
            
            all_combined_news.append({
                "id": len(all_combined_news) + 1,
                "title": entry.title,
                "category": "Kabar Muslim",
                "summary": entry.summary[:100] + "..." if 'summary' in entry else "",
                "content": entry.summary if 'summary' in entry else entry.title,
                "image": image_url,
                "link": entry.link
            })

    # Mengembalikan semua berita yang terkumpul (bisa puluhan hingga ratusan)
    return all_combined_news