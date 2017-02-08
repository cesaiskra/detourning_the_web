import bs4
import urllib
# from string import ascii_lowercase

# for letter in ascii_lowercase
# url = 'https://www.cdc.gov/diseasesconditions/az/' + letter + '.html'
# url = 'https://www.skinsight.com/skin-conditions'
# url = 'http://www.euphemismlist.com'

url = 'http://www.goodbadjokes.com/'
html = urllib.urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")
# pagination = soup.select('div.pagination')[0]

pages = soup.select('li.next')[0].previous_sibling.previous_sibling.text

for i in range(0, int(pages) + 1):
    url = 'http://www.goodbadjokes.com/?page=' + str(i)
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    jokes = soup.select('div.post.index > a')

    for joke in jokes:
        try:
            print joke.select('dt')[0].text
            print joke.select('dd')[0].text
            print ''
        except:
            pass
