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
            print("\u2705 Notifikasi terkirim ke Telegram.")
        else:
            print(f"❌ Gagal kirim. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"[ERROR] Gagal kirim ke Telegram: {e}")

# === COOKIE LOGIN DARI BROWSER ===
cookies = {
    'cross-site-cookie': 'name',
    '_ga': 'GA1.1.376707733.1750685174',
    'one-ux': 'eyJpdiI6IjUrWEQybWVLNUNDdHNVaUJkc0xjU1E9PSIsInZhbHVlIjoiRDRtTFZFY0dkeHJqVHd3UVQ1Tlwvc3c9PSIsIm1hYyI6IjZiZmQ1OWE0ZmJmODc3ZDllMWFjYjc4ZTA2Y2Q4MzkyNTI2YTU2YWJhMzZiMmE5NWRhYWRlZjhmZjhmMjYwZmQifQ==',
    'source_site': 'eyJpdiI6IlRRNEtRQ0dVSUk5OVNkT2VnVndENUE9PSIsInZhbHVlIjoiUnFsVEdnRVVEUWNrd2ZzYnFoTEk4REFZTUhXVEV0VDROeFQyVlwvVXBCNEU9IiwibWFjIjoiZmQ1YTQzYzEzMmU0N2IzYmNjNjAzNDQ4Njk3OGYyN2RhZGFkMTFkYzRkODhhNjk1NzUzMWJiNTM4N2FhN2U4NyJ9',
    'cf_clearance': 'ZcmntgTu1AU53XHMC.mqfjgmSyd9aDgQZSVcX8K74Mw-1750915248-1.2.1.1-YExYY67JTqYS0QVAC9aSy1HbSfeobyeOFkf7nMhlLR8WMJFhXB2a7GamGiAcnuFDHf0dAIYu5B9gv01KJ.n.zv9URDfc2I.e7BVnwNpHdKYQYANCQA.scCLh88m70JFEjd.kmY8MvIK.7m7QbaGn93BWXKNrO7mma6H_d9ZoY0Q.M65cGm8uevHQmeNbExQQs0OidaqaL8dhvF4B8DeP1vEqeLdkz3NW125D.vYX9OhzSPgdMoBPMbj5DVRfmwyjmPh11bkSmaYXOC8k3b1JMDSajZfA4sYEIaGVvpXDn0_EqPiGxeFt0lkONzLriGl0oXpm1P6FnF4EAite8iLwlgv3xCWjaLn4trtIKmF9bbaTek1jPC_afB1mHKlyEDOy',
    '_ga_KT34JXK1TR': 'GS2.1.s1750915224$o3$g1$t1750915467$j30$l0$h0',
    '_ga_Q0M8VSMG8Z': 'GS2.1.s1750915224$o3$g1$t1750915467$j30$l0$h0',
    'XSRF-TOKEN': 'eyJpdiI6InpOeE1hVitCYTZxNjFOTjRMWlRxM1E9PSIsInZhbHVlIjoiWXhFM093blFXTjhCbUZoSFpodnkzeHVWUEE3VXFkcDh0UVZUUFBiQWk5RGtDbDFEdmFLWngxaFVcL05SeEF3YzAiLCJtYWMiOiI5MDdjZWExNjQ4NTU2Nzg1MzdjYjU1OTQxNjk2MmVkOGZlMWE1M2M0MGQ5Y2YwNzdlZGU0NDI5ODFkZDljZWE4In0=',
    'aldmic_session': 'eyJpdiI6IjZWNmxuQ2tqb2I2cVg1R2NVSDR6VVE9PSIsInZhbHVlIjoiT0x6VEd2S01GcDV1ek00UVNncG5najIyVXkzWVFJaWpJTzdtQ3dGYWFsM09STFRWVVFKT3Jvbm5oYVlTMSs0eiIsIm1hYyI6ImQxNTE3NDFjNWVjMTc3MTBlMGJmM2FhNGYyZGUyODI5YTUzYTJkOTM0MTA0YWQ5MjljMmJiNTEzMmVhZDkyZjIifQ=='
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,application/xhtml+xml',
    'Referer': 'https://loyalty.aldmic.com/'
}

url = 'https://loyalty.aldmic.com/reward?cat=11'
log_file = "log_voucher_cat11.txt"

def log(pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{waktu}] {pesan}\n")

def cek_stok():
    try:
        res = requests.get(url, headers=headers, cookies=cookies)
        if res.status_code != 200:
            log(f"ERROR: Status code {res.status_code}")
            print(res.text)
            return
        with open("debug_response_cat11.html", "w", encoding="utf-8") as f:
            f.write(res.text)
            print("[DEBUG] Halaman disimpan ke debug_response_cat11.html")
    except Exception as e:
        log(f"ERROR: Gagal request - {e}")
        return

    soup = BeautifulSoup(res.text, 'html.parser')
    produk = soup.find_all("a", class_="card")
    tersedia = False

    for p in produk:
        print("\n===== DEBUG PRODUK HTML =====")
        print(p.prettify())

        nama = p.find("h5").text.strip() if p.find("h5") else "Tanpa Nama"
        tombol_redeem = p.find("button", string=lambda t: "Redeem Now" in t if t else False)

        if tombol_redeem:
            pesan = f"🏡 <b>VOUCHER TERSEDIA</b>\n<b>{nama}</b>\n👉 <a href='{url}'>Tukar Sekarang</a>"
            print(f"[TERSEDIA] {nama}")
            log(f"TERSEDIA - {nama}")
            kirim_telegram(pesan)
            tersedia = True
        else:
            print(f"[HABIS] {nama}")
            log(f"HABIS - {nama}")

    if not tersedia:
        print("\u2705 Semua produk dicek. Tidak ada yang tersedia saat ini.")

while True:
    print("=" * 60)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Mengecek produk kategori 11...")
    cek_stok()
    time.sleep(120)
