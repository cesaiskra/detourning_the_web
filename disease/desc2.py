import sys
import bs4
import urllib
import time
import random


names = []
descs = []


def get_description(url):
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    try:
        name = soup.select('#firstHeading')[0].text
        names.append(name.encode('utf-8'))
        # print name.encode('utf-8')
        # print ''

        desc = soup.select('p')[0].text
        descs.append(desc.encode('utf-8'))
        # print desc.encode('utf-8')
        # print ''
    except IndexError as e:
        print url
        print e
        print ''


filename = sys.argv[1]
links = []
with open(filename) as f:
    links = f.readlines()
    links = [x.strip() for x in links]

for link in links:
    get_description(link)
    time.sleep(random.uniform(.1, .2))


print "Writing names to file..."
data = open("names.txt", "w")
for name in names:
    data.write("%s\n" % name)
data.close()

print "Writing descs to file..."
data = open("descs.txt", "w")
for desc in descs:
    data.write("%s\n" % desc)
data.close()
