import requests
import json
import re
from bs4 import BeautifulSoup

samadengan = "="*25
welcome = samadengan + " Brainly Question Grabber " + samadengan
welcome2 = "by kimak"
print("{:^80}".format(welcome))
print("{:^80}".format(welcome2))
print()
ask = input("Tuliskan pertanyaannya:\n")
payload = {"limit":10,
           "query":ask}
url = "https://brainly.co.id/api/28/api_tasks/suggester"
scrap = json.loads(requests.get(url, params=payload).text)
try:
    pertanyaan = scrap['data']['tasks']['items'][0]['task']['content']
    pertanyaan = pertanyaan.replace("<br />","\n").replace("<span>","").replace("</span>","")
    print("\nPertanyaan yang diambil:",pertanyaan)
    print("\nMengambil 5 jawaban pertama...\n")
    print("="*25)
except:
    print("Maaf, tidak ada jawabannya di Brainly. Coba lagi dengan kalimat yang spesifik.")
    input("Tekan enter untuk keluar")
    exit()
try:
    for x in range(4):
        jawaban = scrap['data']['tasks']['items'][0]['responses'][x]['content']
        jawaban = jawaban.replace("<br />","\n").replace("<span>","").replace("</span>","")
        print("Jawaban ke-" + str(x+1) + ":\n" + jawaban + "\n")
    print("="*25)
except:
    print("="*25)
    print("Terdapat kurang dari 5 jawaban")
    print()
