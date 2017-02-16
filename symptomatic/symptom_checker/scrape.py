import bs4
import urllib
import re
import time
import random
from string import ascii_uppercase


def get_symptoms():
    url = 'http://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075'
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    symptoms = soup.select('div.adult li a')

    for s in symptoms:
        url = 'http://www.mayoclinic.org/' + s['href']
        print s.text

        html = urllib.urlopen(url).read()
        soup = bs4.BeautifulSoup(html, "html.parser")

        sections = soup.select('fieldset')

        for section in sections:
            symptom_type = section.select('legend')[0].text
            # print symptom_type

            options = section.select('li')
            for opt in options:
                checkbox = opt.select('input')[0]
                label = opt.select('label')[0].text

                url = 'http://www.mayoclinic.org/' + s['href']
                html = urllib.urlopen(url).read()
                soup = bs4.BeautifulSoup(html, "html.parser")
                
                # print s.text + (symptom_type + ' ' + label).lower()

        # subdiseases = disease.select('ul li')
        # if not subdiseases:
        #     print disease.text.strip().encode('utf-8')


# get_links('0-9')
# time.sleep(random.uniform(.1, .2))

# # for letter in ['A']:
# for letter in ascii_uppercase:
#     get_links(letter)
#     time.sleep(random.uniform(.1, .2))

get_symptoms()
