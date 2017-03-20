import json


with open('data.json') as d:
    data = json.load(d)

names = []
for dump in data['dump'].itervalues():
    names.append(dump['title'].strip().encode('utf-8'))

print '\n'.join(names)
