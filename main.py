from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Agar bisa diakses oleh aplikasi HTML kamu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulasi 100 data berita (Saya buatkan contoh polanya, kamu bisa menggandakannya)
news_data = []

# Loop untuk membuat 100 data berita dengan topik berbeda
categories = ["Ekonomi Syariah", "Haji & Umroh", "Dunia Islam", "Gaya Hidup", "Pendidikan"]
for i in range(1, 101):
    cat = categories[i % len(categories)]
    news_data.append({
        "id": i,
        "title": f"Berita Muslim Terkini Ke-{i}: Perkembangan Umat di Era Digital",
        "category": cat,
        "summary": f"Ini adalah ringkasan berita ke-{i} mengenai perkembangan komunitas muslim global yang semakin adaptif dengan teknologi.",
        "content": f"Konten lengkap berita ke-{i} membahas secara mendalam bagaimana integrasi nilai-nilai keislaman dalam kehidupan modern saat ini, mencakup aspek sosial dan ekonomi.",
        "image": f"https://picsum.photos/seed/{i+10}/800/400", # Gambar otomatis unik tiap berita
        "link": "https://www.republika.co.id/khazanah" # Link menuju web asli
    })

@app.get("/news")
def get_all_news():
    return news_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)