import requests
from bs4 import BeautifulSoup
import time

# Cookie hasil parsing
cookies = {
    'cross-site-cookie': 'name',
    '_ga': 'GA1.1.376707733.1750685174',
    'one-ux': 'eyJpdiI6IjUrWEQybWVL...',
    'source_site': 'eyJpdiI6IlRRNEtRQ0dVSUk5...',
    'cf_clearance': 'ZcmntgTu1AU53XHMC.mqfjgmSyd...',
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

url = 'https://loyalty.aldmic.com/reward?cat=11'

def cek_stok():
    res = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, 'html.parser')

    produk = soup.find_all("div", class_="reward-card")  # Sesuaikan dengan elemen asli
    kosong = True
    for p in produk:
        nama = p.find("h5").text.strip() if p.find("h5") else "Tanpa Nama"
        if "Out of stock" not in p.text:
            print(f"[✅ TERSEDIA] {nama}")
            kosong = False
        else:
            print(f"[❌ KOSONG] {nama}")
    
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
    time.sleep(120)
