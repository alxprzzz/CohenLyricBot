from bs4 import BeautifulSoup
import json
import random


with open('lc_lyrics.json') as out:
    all_songs = json.load(out)

all_lines=[]

for song in all_songs:

    #print(song['lyrics'])

    song['lyrics'] = song['lyrics'].replace('\r\n\r\n', '\r\n\r\n')
    song['lyrics'] = song['lyrics'].strip()
    song['lyrics'] = song['lyrics'].lower()

    lines = song['lyrics'].split('\n')
    lines = song['lyrics'].split('\r\n')
    all_lines = all_lines + lines

#print(len(all_lines))

for y in range(1,100):

    for x in range(1,6):

        random_line = all_lines[ random.randint(0, len(all_lines)-1)]

        print(x, random_line)


json.dump(all_lines,open('total_lyrics.json','w'),indent=2)



for y in range(1,1000):

    all_lines = f"{all_lines}"

    if len(all_lines) <= 280:
        #all_lines.append(all_lines)
        print(random_line)

#print(all_lines)

    #print(random_line)

json.dump(all_lines,open('all_lines.json','w'),indent=2)