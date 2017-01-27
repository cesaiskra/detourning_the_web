import bs4
import urllib

url = 'http://www.alibaba.com//Amusement-Park_pid100005611?spm=a2700.7848340.1997230041.442.1RiWO2'
html = urllib.urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")

titles = soup.select('h2.title')

for title in titles:
    print title.text.strip()
