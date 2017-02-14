import bs4
import urllib
import re
import time
import random
from string import ascii_uppercase


def get_links(letter):
    url = 'https://en.wikipedia.org/wiki/List_of_diseases_(' + letter + ')'
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    # links = soup.select('#mw-content-text > ul li > a')
    diseases = soup.select('#mw-content-text > ul li')

    for disease in diseases:
        # rematch = re.findall(r'\[.+]', disease.text)
        # if rematch:
        #     print disease.text
        #     print rematch

        # rematch = re.findall(r'rare', disease.text)
        # if rematch:
        #     print disease.text
        #     print rematch

        # links = disease.select('a')
        # for link in links:
        #     if 'http' in link['href']:
        #         print disease.text
                # link.decompose()

        # subdiseases = disease.select('ul li')
        # if subdiseases:
        #     for subd in subdiseases:
        #         if len(subd.text.strip()) > 140:
        #             print subd.text.strip().encode('utf-8')
        #             print len(subd.text.strip())
        # else:
        #     if len(disease.text.strip()) > 140:
        #         print disease.text.strip().encode('utf-8')
        #         print len(disease.text.strip())

        subdiseases = disease.select('ul li')
        if not subdiseases:
            print disease.text.strip().encode('utf-8')
            # for subd in subdiseases:
            #     print subd.text.strip().encode('utf-8')
        # else:
            # print disease.text.strip().encode('utf-8')

        # if len(disease.text) > 140:
        #     print disease.text.encode('utf-8')


        # print disease.text.encode('utf-8')


get_links('0-9')
time.sleep(random.uniform(.1, .2))

# for letter in ['A']:
for letter in ascii_uppercase:
    get_links(letter)
    time.sleep(random.uniform(.1, .2))
