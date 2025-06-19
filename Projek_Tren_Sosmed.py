from collections import deque

def bfs_keyword_search(data, keyword):
    """
    Fungsi untuk mencari keyword dalam kumpulan teks menggunakan algoritma BFS.
    
    Args:
        data (list of str): List berisi teks (misalnya tweet).
        keyword (str): Kata kunci yang ingin dicari.
    
    Returns:
        list of str: Daftar teks yang mengandung kata kunci.
    """
    result = []
    queue = deque(data)  # Membuat queue untuk BFS

    while queue:
        current_text = queue.popleft()  # Mengambil item pertama dari queue
        if keyword.lower() in current_text.lower():  # Pencarian tidak case sensitive
            result.append(current_text)

    return result


# Data sosial media simulasi (bisa diganti dengan dataset Kaggle)
social_media_posts = [
    "Banjir besar melanda Bekasi sejak pagi.",
    "Harga beras naik tajam di pasar tradisional.",
    "Kemacetan parah terjadi di Jakarta Selatan.",
    "Banjir di Tangerang membuat aktivitas warga terganggu.",
    "Warga mulai mengeluhkan kenaikan harga bahan pokok.",
    "Cuaca hari ini sangat cerah dan mendukung aktivitas luar ruangan.",
    "Demo buruh terjadi di depan gedung DPR hari ini.",
    "Macet di jalur utama menuju Bekasi timur."
]

# Daftar kata kunci isu lokal
keywords = ["banjir", "beras", "kemacetan", "demo", "macet"]

# Eksekusi pencarian untuk tiap keyword
for keyword in keywords:
    print(f"\n📌 Hasil pencarian untuk keyword: '{keyword}'")
    matches = bfs_keyword_search(social_media_posts, keyword)
    if matches:
        for post in matches:
            print(" -", post)
    else:
        print(" - Tidak ditemukan.")
