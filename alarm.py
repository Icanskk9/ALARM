import requests
from bs4 import BeautifulSoup
import time

# Masukkan cookie dari browser
cookies = {
    'session': 'cross-site-cookie=name; _ga=GA1.1.376707733.1750685174; cross-site-cookie=name; one-ux=eyJpdiI6IjUrWEQybWVLNUNDdHNVaUJkc0xjU1E9PSIsInZhbHVlIjoiRDRtTFZFY0dkeHJqVHd3UVQ1Tlwvc3c9PSIsIm1hYyI6IjZiZmQ1OWE0ZmJmODc3ZDllMWFjYjc4ZTA2Y2Q4MzkyNTI2YTU2YWJhMzZiMmE5NWRhYWRlZjhmZjhmMjYwZmQifQ%3D%3D; source_site=eyJpdiI6IlRRNEtRQ0dVSUk5OVNkT2VnVndENUE9PSIsInZhbHVlIjoiUnFsVEdnRVVEUWNrd2ZzYnFoTEk4REFZTUhXVEV0VDROeFQyVlwvVXBCNEU9IiwibWFjIjoiZmQ1YTQzYzEzMmU0N2IzYmNjNjAzNDQ4Njk3OGYyN2RhZGFkMTFkYzRkODhhNjk1NzUzMWJiNTM4N2FhN2U4NyJ9; cf_clearance=ZcmntgTu1AU53XHMC.mqfjgmSyd9aDgQZSVcX8K74Mw-1750915248-1.2.1.1-YExYY67JTqYS0QVAC9aSy1HbSfeobyeOFkf7nMhlLR8WMJFhXB2a7GamGiAcnuFDHf0dAIYu5B9gv01KJ.n.zv9URDfc2I.e7BVnwNpHdKYQYANCQA.scCLh88m70JFEjd.kmY8MvIK.7m7QbaGn93BWXKNrO7mma6H_d9ZoY0Q.M65cGm8uevHQmeNbExQQs0OidaqaL8dhvF4B8DeP1vEqeLdkz3NW125D.vYX9OhzSPgdMoBPMbj5DVRfmwyjmPh11bkSmaYXOC8k3b1JMDSajZfA4sYEIaGVvpXDn0_EqPiGxeFt0lkONzLriGl0oXpm1P6FnF4EAite8iLwlgv3xCWjaLn4trtIKmF9bbaTek1jPC_afB1mHKlyEDOy; _ga_KT34JXK1TR=GS2.1.s1750915224$o3$g1$t1750915467$j30$l0$h0; _ga_Q0M8VSMG8Z=GS2.1.s1750915224$o3$g1$t1750915467$j30$l0$h0; XSRF-TOKEN=eyJpdiI6InpOeE1hVitCYTZxNjFOTjRMWlRxM1E9PSIsInZhbHVlIjoiWXhFM093blFXTjhCbUZoSFpodnkzeHVWUEE3VXFkcDh0UVZUUFBiQWk5RGtDbDFEdmFLWngxaFVcL05SeEF3YzAiLCJtYWMiOiI5MDdjZWExNjQ4NTU2Nzg1MzdjYjU1OTQxNjk2MmVkOGZlMWE1M2M0MGQ5Y2YwNzdlZGU0NDI5ODFkZDljZWE4In0%3D; aldmic_session=eyJpdiI6IjZWNmxuQ2tqb2I2cVg1R2NVSDR6VVE9PSIsInZhbHVlIjoiT0x6VEd2S01GcDV1ek00UVNncG5najIyVXkzWVFJaWpJTzdtQ3dGYWFsM09STFRWVVFKT3Jvbm5oYVlTMSs0eiIsIm1hYyI6ImQxNTE3NDFjNWVjMTc3MTBlMGJmM2FhNGYyZGUyODI5YTUzYTJkOTM0MTA0YWQ5MjljMmJiNTEzMmVhZDkyZjIifQ%3D%3D',
    # tambahkan lainnya jika perlu
}

headers = {
    'User-Agent': 'Mozilla/5.0',
    # 'Referer': 'https://loyalty.aldmic.com',
    # tambahkan header penting lainnya jika perlu
}

url = 'https://loyalty.aldmic.com/reward?cat=4'

def cek_stok():
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all("div", class_="product")  # sesuaikan class-nya
    for item in items:
        nama = item.find("h3").text.strip()
        if "Out of stock" not in item.text:
            print(f"[AVAILABLE] {nama}")
            # bisa tambahkan bunyi alarm atau notifikasi
        else:
            print(f"[Kosong] {nama}")

# Looping pengecekan tiap 2 menit
while True:
    print("Cek stok...")
    cek_stok()
    time.sleep(120)
