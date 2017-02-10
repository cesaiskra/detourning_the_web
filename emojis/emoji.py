import time
from selenium import webdriver

# brew install geckodriver
# driver = webdriver.Firefox()

# brew install chromedriver
# driver = webdriver.Chrome()

# brew install phantomjs
driver = webdriver.PhantomJS()


def get_emojis():
    emojis = driver.find_elements_by_css_selector('td.btn')

    for emoji in emojis:
        try:
            if emoji.get_attribute('data-clipboard-text') != '':
                print emoji.get_attribute('data-clipboard-text').encode('utf-8')
        except:
            print '*************no data-clipboard-text*************'


for num in range(1,20):
    url = 'http://japaneseemoticons.me/all-japanese-emoticons/' + str(num) + '/'
    driver.get(url)
    time.sleep(2)
    get_emojis()
    driver.quit()
