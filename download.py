from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4

# number of words = 141513

page_url_prefix = "https://mongoltoli.mn/dictionary/detail/"
audio_url_prefix = "https://mongoltoli.mn/audio/"

def get_page(url):
    try:
       page = urlopen(url)
       return page
    except Exception as e:
       print("Page failed::", e)

def get_audio(url):
    try:
       audio = urlopen(url)
       return audio
    except Exception as e:
       print("Audio failed:", e)
       return None

# # get_page(page_url)
# audio = get_audio(audio_url_prefix+str(141511)+".mp3")
# print(audio)
# exit()

def get_word(url):
    try:
        page = get_page(url)
        soup = BeautifulSoup(page, 'html.parser')
        content = soup.find('div', {"class": "title"})
        word = content.text
        word = word.strip().replace(":", "")
    except:
        word = "None"

    return word

import csv
import time

f_csv = open('toli.csv', 'a', encoding='utf-8-sig', newline='')
writer = csv.writer(f_csv)
writer.writerow(["number", "word"])

for i in range(141513,150000):
    #time.sleep(1)
    tag = str(i).zfill(6)
    w = get_word(page_url_prefix + str(i))
    writer.writerow([tag, w])
    f_csv.flush()



    a = get_audio(audio_url_prefix + str(i)+".mp3")
    if a != None:
        filename = w.replace(" ","-") + "-" + tag + ".mp3"
        f = open("./toli-mp3/" + filename, "wb")
        f.write(a.read())
        f.close()

    print(tag, '{0: >15}'.format(w), "MP3:", a)

f_csv.close()
