import bs4
import urllib
import time
from string import ascii_uppercase
# from textblob import TextBlob

for letter in ascii_uppercase:
# for letter in ['a']:
    url = 'https://en.wikipedia.org/wiki/List_of_diseases_(' + letter + ')'
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    links = soup.select('#mw-content-text > ul li > a')

    for link in links:
        print link.text.encode('utf-8')

    time.sleep(.1)
