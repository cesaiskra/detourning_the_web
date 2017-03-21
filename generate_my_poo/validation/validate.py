import re
import json
from pprint import pprint


with open('data.json') as f:
    data = json.load(f)

re_rating = r'\d\.\d{2}.??'
re_votes = r'\d+'

for filename, info in data['dump'].iteritems():
    rating = info['rating']
    match = re.match(re_rating, rating)
    try:
        if match.group() == rating:
            pass
        else:
            print info

    except:
        print info

    # votes = info['votes']
    # match = re.match(re_votes, votes)
    # try:
    #     if match.group() == votes:
    #         pass
    #     else:
    #         print info

    # except:
    #     print info

# with open('data.json', 'w') as f:
#     json.dump(data, f)