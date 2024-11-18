import requests
from bs4 import BeautifulSoup
import json
import time

# Fungsi untuk melakukan scraping
def scrape_data():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ambil data yang diinginkan
    quotes_data = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quotes_data.append({'text': text, 'author': author})

    # Simpan data ke file JSON
    with open('quotes.json', 'w') as json_file:
        json.dump(quotes_data, json_file, indent=4)

    print(f"Data berhasil disimpan ke quotes.json, jumlah kutipan: {len(quotes_data)}")

# Fungsi untuk menjalankan scraping secara berkala
def run_scraper(interval):
    while True:
        scrape_data()
        time.sleep(interval)  

# Jalankan scraper dengan interval 1jam
run_scraper(3600)