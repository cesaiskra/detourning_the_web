import bs4
import urllib
import time
import random
from string import ascii_uppercase


def get_links(letter):
    url = 'https://en.wikipedia.org/wiki/List_of_diseases_(' + letter + ')'
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    links = soup.select('#mw-content-text > ul li > a')

    for link in links:
        # print link.text.encode('utf-8')
        if not link.has_attr('class'):
            print 'https://en.wikipedia.org' + link['href']
            # normal_links.append(link['href'])

        # if link.has_attr('class'):
        #     if link['class'][0] == 'new':
        #         # log disease, no description

        #         # new_links.append(link['href'])
        #     elif link['class'][0] == 'mw-redirect':
        #         # figure out redirected disease
        #         # link them to the same description

        #         # redirect_links.append(link['href'])
        #     else:
        #         print 'unexpected class ' + link['class'][0]

        # else:
        #     # log disease and description

        #     normal_links.append(link['href'])


for letter in ascii_uppercase:
# for letter in ['A']:
    get_links(letter)
    time.sleep(random.uniform(.1, .2))
