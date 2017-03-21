import json
import os
from sys import argv
from pprint import pprint


jsonfile = argv[1]

with open(jsonfile) as d:
    data = json.load(d)

images = data['dump']

redo_words = ''
files = {
    # filename: src
}
for image, info in images.iteritems():
    if 'Rating' in info['rating']:
        redo_words += info['title'] + ' '
        files[image] = info['src']

print redo_words
print '\n'
pprint(files)
