import bs4
import urllib
import time

for num in range(1, 41):
# for num in range(1, 2):
    time.sleep(2)
    url = 'http://dongerlist.com/page/' + str(num)
    html = urllib.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    emojis = soup.select('div.copy-donger')

    for emoji in emojis:
        try:
            print emoji['data-clipboard-text'].encode('utf-8')
        except:
            print '*************no data-clipboard-text*************'
