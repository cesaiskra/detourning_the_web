import bs4
import requests
import time
import re
import json
import os.path
import sys


def loadJSON(filename):
    try:
        with open(filename) as d:
            data = json.load(d)

        print filename + ' loaded\n'

    except:
        data = {
            'searched': [],
            'unsearched': [],
            'blacklist': [],
            # 'errors': {

            # },
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

        print filename + ' load error - creating new file\n'

    return data


def writeJSON():
    with open(jsonfile, 'w') as f:
        json.dump(data, f)

    print 'wrote data to ' + jsonfile + '\n'


def download(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def update_searched(q):
    q_set = set(q.split(' '))
    searched = set(data['searched'])
    new_searched = q_set.union(searched)

    if searched != new_searched:
        print 'added \'' + ', '.join(q_set.difference(searched)) + '\' to searched\n'
        data['searched'] = list(new_searched)

    unsearched = set(data['unsearched'])
    new_unsearched = unsearched.difference(q_set)

    if unsearched != new_unsearched:
        print 'removed \'' + ', '.join(unsearched.intersection(q_set)) + '\' from unsearched\n'
        data['unsearched'] = list(new_unsearched)


def add_unsearched(title):
    title_set = set(title.lower().split(' '))
    searched = set(data['searched'])

    new_set = title_set.difference(searched)

    unsearched = set(data['unsearched'])
    new_unsearched = new_set.union(unsearched)

    if unsearched != new_unsearched:
        print 'added \'' + ', '.join(new_set.difference(unsearched)) + '\' to unsearched\n'
        data['unsearched'] = list(new_unsearched)


def get_poo_pic(info):
    src = info['src']
    filename = src.split('/')[-1]
    filepath = poo_dir + filename

    if os.path.exists(filepath):
        suffix = 2
        s = filename.split('.')
        while filename in data['dump']:
            filename = ''.join(s[0:-1]) + '-' + str(suffix) + '.' + s[-1]
            suffix += 1

    info['path'] = filepath
    download(info['src'], filepath)
    print 'downloaded ' + filepath
    time.sleep(0.2)


def get_poo_info(content):
    text = content.text.strip()
    lines = re.split('\n', text)
    split_0 = lines[0].split(':')
    title = ':'.join(split_0[1:]).strip()
    split_1 = lines[1].split(' ')
    votes = split_1[1]
    rating = split_1[3]
    uploaded = lines[3].split(' ')[1]

    img = content.findNext('img')
    src = img.get('src').replace('/t/', '/b/')
    filename = src.split('/')[-1]

    result_num = int(lines[0].split(' ')[0].replace('#', ''))
    if result_num % 10 == 0:
        print split_0[0] + '\n'

    if filename in data['dump'] and data['dump'][filename]['src'] == src or filename in data['blacklist']:
        return None

    # validate data

    info = {
        'title': title,
        'votes': votes,
        'rating': rating,
        'uploaded': uploaded,
        'src': src
    }

    data['dump'][filename] = info
    add_unsearched(title)
    return info


def scrape(q, page_start=0, page_stop=0):
    new_results = False
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
        if result.text.strip().startswith('#'):
            content = result.select('font')[0]

            info = get_poo_info(content)
            if not info:
                continue
            elif poo_dir:
                get_poo_pic(info)

            new_results = True
            for k, v in info.iteritems():
                print k + ': ' + v
            print ''

    if new_results:
        writeJSON()

    # next page
    next_to_last_link = soup.select('a')[-2]
    if next_to_last_link.get('href').startswith('/xyzzy/search'):
        next_page = page_start + 1
        if page_stop == 0 or next_page < page_stop:
            scrape(q, next_page)
        else:
            print 'reached page stop ' + str(page_stop) + '\n'
    else:
        print 'no more results\n'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('q', nargs='?', help='Search string.')
    parser.add_argument('-s', '--start_page', type=int, default=0, help='Start page.')
    parser.add_argument('-e', '--end_page', type=int, default=0, help='End page.')
    parser.add_argument('-f', '--query_file', help='Text file containing search string.')
    parser.add_argument('-w', '--download', action='store_true', help='Download images.')
    parser.add_argument('-d', '--directory', default='./', help='Directory for downloaded images.')
    parser.add_argument('-j', '--json', help='JSON file to read and write to.')
    args = parser.parse_args()

    if args.query_file:
        with open(args.query_file, 'r') as f:
            q = f.read().replace('\n', ' ')
    elif args.q:
        q = args.q
    else:
        print 'no query provided'
        sys.exit()

    print q + '\n'

    if args.download:
        poo_dir = args.directory

        if poo_dir[-1] != '/':
            poo_dir = poo_dir + '/'

        if not os.path.exists(poo_dir):
            os.makedirs(poo_dir)

        print 'image dir: ' + poo_dir + '\n'

    else:
        poo_dir = None
        print 'dry run\n'

    if args.json:
        jsonfile = args.json
        data = loadJSON(jsonfile)

    scrape(q, args.start_page, args.end_page)
