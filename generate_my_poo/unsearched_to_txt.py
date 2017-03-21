import json
import math
from sys import argv

jsonfile = argv[1]
outfile = argv[2]

with open(jsonfile) as d:
    data = json.load(d)

unsearched = data['searched']
word_count = len(unsearched)
chunk_count = int(math.ceil(word_count / 1000.0))

for i in range(chunk_count):
    f = open('%s_%d.txt' % (outfile, i + 1), 'w')
    f.write(' '.join(unsearched[i * 1000:(i + 1) * 1000]).strip().encode('utf-8'))
    f.close()
