# check if entry already exists in data.dump separate from if the file exists
# argparse
# break into smaller functions

import bs4
import requests
import time
# from sys import argv
import re
import json
import string
import os.path
from pprint import pprint

poo_dir = '_img/'
if not os.path.exists(poo_dir):
    os.makedirs(poo_dir)

try:
    with open('data.json') as d:
        data = json.load(d)

    pprint(data)
except:
    # print 'json load error\n'
    # data = {
    #     'unsearched': [],
    #     # q: {
    #     #   hits: hit_count,
    #     #   results:
    #     #     [
    #     #         {
    #     #             index: ,
    #     #             title: ,
    #     #             votes: ,
    #     #             rating: ,
    #     #             matches: ,
    #     #             uploaded: ,
    #     #             filename: ,
    #     #         }
    #     #     ]
    #     # }
    # }

    data = {
        'searched': [],
        'unsearched': [],
        'dump': {
            # "32ffff7d679db5348792084a67a1d753.jpg": {
            #   "uploaded": "2005-12-03",
            #   "votes": "5106",
            #   "rating": "4.69 ",
            #   "title": "10 yr old goonar",
            #   "src": "http://216.218.248.240/datastore/32/ff/b/32ffff7d679db5348792084a67a1d753.jpg"
            # }
        }
    }


def download(url, path):
    # local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:   # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    # return local_filename


def update_searched(q):
    q_set = set(q.split(' '))
    searched = set(data['searched'])
    new_searched = q_set.union(searched)

    if searched != new_searched:
        print 'added \'' + ', '.join(q_set.difference(searched)) + '\' searched'
        data['searched'] = list(new_searched)

    unsearched = set(data['unsearched'])
    new_unsearched = unsearched.difference(q_set)

    if unsearched != new_unsearched:
        print 'removed \'' + ', '.join(unsearched.intersection(q_set)) + '\' from unsearched'
        data['unsearched'] = list(new_unsearched)


def add_unsearched(title):
    title_set = set(str(title).translate(None, string.punctuation).split(' '))
    searched = set(data['searched'])

    new_set = title_set.difference(searched)

    unsearched = set(data['unsearched'])
    new_unsearched = new_set.union(unsearched)

    if unsearched != new_unsearched:
        print 'added \'' + ', '.join(new_set.difference(unsearched)) + '\' to unsearched'
        data['unsearched'] = list(new_unsearched)


def scrape(q, page_start=0, page_stop=0):

    update_searched(q)

    url = 'http://www.ratemypoo.com/xyzzy/search'
    params = {
        'step': str(page_start * 10),
        'search': q
    }

    html = requests.get(url, params=params).text
    soup = bs4.BeautifulSoup(html, "html.parser")
    results = soup.select('tr')

    for result in results:
        # print result.text.strip()
        if result.text.strip().startswith('#'):
            content = result.select('font')[0]

            # if src already exists, it's a duplicate
            img = content.findNext('img')
            src = img.get('src').replace('/t/', '/b/')

            filename = poo_dir + src.split('/')[-1]

            if os.path.exists(filename) is False:
                download(src, filename)

                text = content.text.strip()
                lines = re.split(': |\n', text)
                title = lines[1].lower()

                datum = {
                    # 'index': lines[0].split(' ')[0].replace('#', ''),
                    'title': title,
                    'votes': lines[3].split(' ')[0],
                    'rating': lines[4],
                    # 'matches': lines[6],
                    'uploaded': lines[-1],
                    'src': src
                }
                # data[q]['results'].append(datum)
                data['dump'][filename.replace(poo_dir, '')] = datum

                print text
                print src
                add_unsearched(title)
                print ''

                time.sleep(0.2)

            else:
                print 'skipping duplicate: ' + filename

        # elif result.text.strip().startswith('Results') and data[q]['hits'] is None:
        #     hits = result.text.strip().split('\n')[1].split(' ')[0]
        #     print 'hits: ' + str(hits) + '\n'
        #     data[q]['hits'] = hits

    next_to_last_link = soup.select('a')[-2]
    if next_to_last_link.get('href').startswith('/xyzzy/search'):
        next_page = page_start + 1
        if page_stop == 0 or next_page < page_stop:
            scrape(q, next_page)
        else:
            print 'reached page stop ' + str(page_stop)
    else:
        print 'no more results'


scrape('10 am poo', 1, 2)
# queries = open(argv[1], 'r').readlines()[0]
# scrape(queries)
with open('data.json', 'w') as f:
    json.dump(data, f)
