import json
import random

# {
#     'patterns': patterns,
#     'tags': {
#         tag: []
#     }
# }

with open('title_tp.json') as d:
    data = json.load(d)

patterns = data['patterns']
tags = data['tags']


def gen_title():
    pattern = random.choice(patterns)

    title = []
    for tag in pattern:
        words = tags[tag]
        title.append(random.choice(words))

    return ' '.join(title).replace(" '", "'")


if __name__ == '__main__':
    from sys import argv

    try:
        for i in range(int(argv[1])):
            print gen_title()
    except:
        print gen_title()
