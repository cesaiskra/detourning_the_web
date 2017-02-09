import bs4
import urllib
import time
import random
from string import ascii_uppercase
# from textblob import TextBlob


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


def get_description(path):
    url = 'https://en.wikipedia.org' + path
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    try:
        name = soup.select('#firstHeading')[0].text
        print name.encode('utf-8')
        print ''

        desc = soup.select('p')[0].text
        print desc.encode('utf-8')
        print ''
    except IndexError as e:
        print url
        print e
        print ''

normal_links = []
# redirect_links = []
# new_links = []


for letter in ascii_uppercase:
# for letter in ['A']:
    get_links(letter)
    time.sleep(random.uniform(.1, .2))


# print normal_links
# print redirect_links
# print new_links


# for link in normal_links:
#     get_description(link)
#     time.sleep(random.uniform(.1, .2))
