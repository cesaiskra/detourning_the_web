import bs4
import urllib
import time
import random
from string import ascii_uppercase
import json


def get_symptoms(letter):
    url = 'http://www.mayoclinic.org/symptoms/index?letter=' + letter
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    symptoms = soup.select('div#index li')

    for s in symptoms:
        if 'See:' in s.text:
            # print '    ' + s.text.strip() + '\n'
            continue

        symptom = s.text.strip().lower().encode('utf-8')
        url = 'http://www.mayoclinic.org' + s.select('a')[0]['href']
        print symptom

        dictionary[symptom] = {}
        dictionary[symptom]['url'] = url
        dictionary[symptom]['causes'] = []
        get_causes(symptom)


def get_causes(symptom):
    html = urllib.urlopen(dictionary[symptom]['url']).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    causes_url = 'http://www.mayoclinic.org' + soup.select('.page.content a')[0]['href']

    html = urllib.urlopen(causes_url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    causes = soup.select('ol.bullet li')

    for c in causes:
        cause = c.text.strip().lower().encode('utf-8')
        dictionary[symptom]['causes'].append(cause)

    print '    ' + str(len(dictionary[symptom]['causes'])) + ' causes'

dictionary = {}

# for letter in ['A']:
for letter in ascii_uppercase:
    if letter in 'OXZ':
        continue

    get_symptoms(letter)
    time.sleep(random.uniform(.1, .2))


with open('symptoms.json', 'w') as fp:
    json.dump(dictionary, fp, sort_keys=True, indent=4)
# print dictionary
