import json
from sys import argv

jsonfile = argv[1]

with open(jsonfile) as d:
    data = json.load(d)

unsearched = ' '.join(data['unsearched']).strip().encode('utf-8')
print unsearched
