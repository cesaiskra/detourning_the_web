import json
from sys import argv
from pprint import pprint


files = argv[1:]

with open('data.json') as f:
    data = json.load(f)

print len(data['dump'])

data['blacklist'] = []
for filename in files:
    try:
        del data['dump'][filename]
        print 'deleted', filename
        # pprint(data['dump'][filename])
    except:
        pass

    data['blacklist'].append(filename)
    print 'added', filename, 'to blacklist\n'

print data['blacklist']

print len(data['dump'])

# del data['dump'][]

# for filename, info in data['dump'].iteritems():
        
    

with open('data.json', 'w') as f:
    json.dump(data, f)


# 973b15b90a05b0da4da7db8da04517bd.jpg 70684d6897b44e5f789f079a576d36d3.jpg 9d0bdad0864ebd72f119acc74a409139.jpg