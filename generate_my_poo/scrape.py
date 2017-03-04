import bs4
import requests
import time


url = 'http://www.ratemypoo.com/xyzzy/search?search=10+am'
html = requests.get(url).text
# print html
soup = bs4.BeautifulSoup(html, "html.parser")
# print soup
# items = soup.select('#wd_content')
results = soup.select('tr')
for result in results:
    print '---'
    print result.text
    print '----'
    # print len(result.children)
    # for child in result.children:
    #     print child

# for result in results:
    # print result
    # description = result.select('font')[0]


# links = soup.select('a')
# for link in links:
#     if '/xyzzy' in link.get('href'):
#         next = link
#         break
