import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# === KONFIGURASI TELEGRAM ===
TELEGRAM_TOKEN = '7439886198:AAF-Vluj0XrDlghI8QdFcHwJi0aOI3Yy9AI'
TELEGRAM_CHAT_ID = '1801962339'

def kirim_telegram(pesan):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': pesan,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Notifikasi terkirim ke Telegram.")
        else:
            print(f"❌ Gagal kirim. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"[ERROR] Gagal kirim ke Telegram: {e}")

# === COOKIE LOGIN ===
cookies = {
    'cross-site-cookie': 'name',
    '_ga': 'GA1.1.376707733.1750685174',
    'one-ux': 'eyJpdiI6IjUrWEQybWVLNUND...',
    'source_site': 'eyJpdiI6IlRRNEtRQ0dVS...',
    'cf_clearance': 'ZcmntgTu1AU53XHMC.mqfjg...',
    '_ga_KT34JXK1TR': 'GS2.1.s1750915224...',
    '_ga_Q0M8VSMG8Z': 'GS2.1.s1750915224...',
    'XSRF-TOKEN': 'eyJpdiI6InpOeE1hVitCY...',
    'aldmic_session': 'eyJpdiI6IjZWNmxuQ2tqb2I2...'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://loyalty.aldmic.com/'
}

# === KONFIGURASI LAIN ===
url = 'https://loyalty.aldmic.com/reward?cat=4'
log_file = "log_semua_voucher.txt"

def log(pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{waktu}] {pesan}\n")

def cek_stok():
    try:
        res = requests.get(url, headers=headers, cookies=cookies)
    except Exception as e:
        log(f"ERROR: Gagal request - {e}")
        return

    soup = BeautifulSoup(res.text, 'html.parser')
    produk = soup.find_all("div", class_="reward-card")
    tersedia = False

    for p in produk:
        nama = p.find("h5").text.strip() if p.find("h5") else "Tanpa Nama"
        tombol_redeem = p.find("a", string=lambda t: t and "Redeem" in t)
        daily_limit = p.find(string=lambda t: "Daily Limit Reached" in t if t else False)

        if tombol_redeem and not daily_limit:
            pesan = f"🎉 <b>STOK TERSEDIA</b>\n<b>{nama}</b>\n👉 {url}"
            print(pesan)
            log(f"TERSEDIA - {nama}")
            kirim_telegram(pesan)
            tersedia = True
        elif daily_limit:
            print(f"[LIMIT] {nama}")
            log(f"LIMIT - {nama}")
        else:
            print(f"[HABIS] {nama}")
            log(f"HABIS - {nama}")

    if not tersedia:
        print("✅ Tidak ada voucher tersedia saat ini.")

# === LOOP TIAP 2 MENIT ===
while True:
    print("=" * 60)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Mengecek semua voucher...")
    cek_stok()
    time.sleep(120)
