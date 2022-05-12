
import requests
from bs4 import BeautifulSoup
import json
import random


songs = []
#for songs in album, add more here
all_urls = ["https://www.leonardcohenfiles.com/album1.html","https://www.leonardcohenfiles.com/album2.html","https://www.leonardcohenfiles.com/album3.html","https://www.leonardcohenfiles.com/album5.html","https://www.leonardcohenfiles.com/album6.html","https://www.leonardcohenfiles.com/album7.html","https://www.leonardcohenfiles.com/album8.html","https://www.leonardcohenfiles.com/album9.html","https://www.leonardcohenfiles.com/album10.html"]


#additional album urls below because they were formatted differently from the previous 10 above
url_1 = ["https://www.leonardcohenfiles.com/tennewsongs.html"]

url_2 = ["https://www.leonardcohenfiles.com/dearheather.html"]

url_3 = ["https://www.leonardcohenfiles.com/oldideas.html"]
 
url_4 = ["https://www.leonardcohenfiles.com/popularproblems.html"]

url_5 = ["https://www.leonardcohenfiles.com/darker.html"]

url_6 = ["https://www.leonardcohenfiles.com/thanks19.html"]


for url in all_urls:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(0,len(all_lyrics)-1):

        lyrics = all_lyrics[inx].get_text()

        songs.append({

            "lyrics": lyrics

        })

        print(lyrics)
        print('---------')

for url in url_1:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")


    for inx in range(0,len(all_lyrics)):

        lyrics = all_lyrics[inx].get_text()

        songs.append({

            "lyrics": lyrics

        })

        print(lyrics)
        print('---------')


for url in url_2:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(0,len(all_lyrics)):

        lyrics = all_lyrics[inx].get_text()

        songs.append({

            "lyrics": lyrics

        })

        print(lyrics)
        print('---------')

for url in url_3:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(0,len(all_lyrics)-1):

        lyrics = all_lyrics[inx].get_text()
       
        songs.append({

           "lyrics": lyrics,
     
        })

        print(lyrics)
        print('---------')

for url in url_4:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(len(all_lyrics)):

        lyrics = all_lyrics[inx].get_text()

        songs.append({

            "lyrics": lyrics,

        })

        print(lyrics)
        print('---------')

for url in url_5:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(0,len(all_lyrics)-1):

        lyrics = all_lyrics[inx].get_text()

        songs.append({

            "lyrics": lyrics,

        })

        print(lyrics)
        print('---------')

for url in url_6:

    r = requests.get(url)

    soup = BeautifulSoup(r.text, features= "html.parser")

    all_lyrics = soup.find_all("blockquote")


    for inx in range(len(all_lyrics)):

        lyrics = all_lyrics[inx].get_text()
        
        songs.append({

            "lyrics": lyrics,

        })

        print(lyrics)
        print('---------')


with open('lc_lyrics.json', 'w') as out:
    json.dump(songs, out, indent=2)
