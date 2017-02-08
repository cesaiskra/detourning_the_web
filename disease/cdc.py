import bs4
import urllib
import re
import time
from string import ascii_lowercase
# from textblob import TextBlob

for letter in ascii_lowercase:
# for letter in ['a']:
    url = 'https://www.cdc.gov/diseasesconditions/az/' + letter + '.html'
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    links = soup.select('div.span16 a')

    for link in links:
        if not link.text.startswith('see also'):
            print re.sub(r' . see .*', '', link.text).encode('utf-8')

    time.sleep(.1)
