import json
import os
from sys import argv
from pprint import pprint


jsonfile = argv[1]

source_dir = 'src/'
target_dir = 'sorted/'

with open(jsonfile) as d:
    data = json.load(d)

images = data['dump']

for filename, info in images.iteritems():
    origin = source_dir + filename
    rating = int(round(float(info['rating'])))
    if rating < 1:
        print filename
        pprint(info)

    # folder = target_dir + str(rating) + '/'
    # target = folder + filename

    # if not os.path.exists(folder):
    #     os.makedirs(folder)

    # try:
    #     os.rename(origin, target)
    #     # print origin, target
    #     pass
    # except:
    #     print 'error', filename
