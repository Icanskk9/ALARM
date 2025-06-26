import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# === Setting Telegram ===
TELEGRAM_TOKEN = 'ISI_API_TOKEN_BOT_KAMU'
TELEGRAM_CHAT_ID = 'ISI_CHAT_ID_KAMU'

def kirim_telegram(pesan):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': pesan,
        'parse_mode': 'HTML'
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"[ERROR] Gagal kirim ke Telegram: {e}")

# === Cookie login ===
cookies = {
    'cross-site-cookie': 'name',
    '_ga': 'GA1.1.376707733.1750685174',
    'one-ux': '...potong untuk ringkas...',
    'source_site': '...',
    'cf_clearance': '...',
    '_ga_KT34JXK1TR': '...',
    '_ga_Q0M8VSMG8Z': '...',
    'XSRF-TOKEN': '...',
    'aldmic_session': '...'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://loyalty.aldmic.com/'
}

url = 'https://loyalty.aldmic.com/reward?cat=11'
log_file = "log_stok.txt"

def log(pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{waktu}] {pesan}\n")

def cek_stok():
    res = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, 'html.parser')

    produk = soup.find_all("div", class_="reward-card")
    kosong = True
    for p in produk:
        nama = p.find("h5").text.strip() if p.find("h5") else "Tanpa Nama"
        if "Out of stock" not in p.text:
            pesan = f"🎉 <b>STOK TERSEDIA</b>\nProduk: <b>{nama}</b>\n{url}"
            print(pesan)
            log(f"TERSEDIA - {nama}")
            kirim_telegram(pesan)
            kosong = False
        else:
            print(f"[KOSONG] {nama}")
            log(f"KOSONG - {nama}")
    
    if kosong:
        print("Belum ada stok yang tersedia...\n")

# Loop per 2 menit
while True:
    print("="*40)
    print("Mengecek stok di Aldmic Reward...")
    try:
        cek_stok()
    except Exception as e:
        print(f"[ERROR] {e}")
        log(f"ERROR - {e}")
    time.sleep(120)
