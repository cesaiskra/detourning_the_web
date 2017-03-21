from textblob import TextBlob as tb
# from pprint import pprint
import json


lines = open('names.txt', 'r').readlines()

tags = {}
patterns = []
for line in lines:
    name = line.rstrip()

    tagged = tb(name.decode('utf-8')).tags
    pattern = []
    for tup in tagged:
        pattern.append(tup[1])
        if tup[1] not in tags:
            tags[tup[1]] = []

        tags[tup[1]].append(tup[0].encode('utf-8'))

    patterns.append(pattern)

# pprint(tags)

tp = {
    'patterns': patterns,
    'tags': tags
}

with open('title_tp.json', 'w') as f:
    json.dump(tp, f)
