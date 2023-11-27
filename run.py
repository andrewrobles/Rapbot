import requests

from bs4 import BeautifulSoup

url = 'https://www.azlyrics.com/lyrics/eminem/rapgod.html'

result = requests.get(url)
src = result.content

soup = BeautifulSoup(src, 'html.parser')
page = soup.find_all('div', {'class': None})

lyrics = []

for rows in page:
	lyrics.append(rows.text)

words = [word for line in lyrics for word in line.split()]

import time

for line in words[1119:1219]:
	print(line)
	time.sleep(0.15)
