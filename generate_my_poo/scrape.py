import bs4
import requests


url = 'http://www.ratemypoo.com/xyzzy/search?search=10+am'
html = requests.get(url).text
# print html
soup = bs4.BeautifulSoup(html, "html.parser")

# items = soup.select('#wd_content')
results = soup.select('center center tr')
print results

# for result in results:
    # print result
    # description = result.select('font')[0]


# links = soup.select('a')
# for link in links:
#     if '/xyzzy' in link.get('href'):
#         next = link
#         break
