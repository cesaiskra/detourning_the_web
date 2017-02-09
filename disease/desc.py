import sys
import bs4
import urllib
import time
import random


def get_description(url):
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    try:
        name = soup.select('#firstHeading')[0].text
        print name.encode('utf-8')

        desc = soup.select('p')[0].text
        print desc.encode('utf-8').replace('\n', '')
        print ''
    except IndexError:
        print ''


filename = sys.argv[1]
links = []
with open(filename) as f:
    links = f.readlines()
    links = [x.strip() for x in links]


for link in links:
    get_description(link)
    time.sleep(random.uniform(.1, .2))
