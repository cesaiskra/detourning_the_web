import time
from selenium import webdriver


# driver = webdriver.Firefox()

# brew install chromedriver
# driver = webdriver.Chrome()

# brew install phantomjs
driver = webdriver.PhantomJS()

url = 'http://www.alibaba.com/products/round_flower_box.html'


def get_page():
    time.sleep(2)
    titles = driver.find_elements_by_css_selector('h2.title')

    for title in titles:
        print title.text

    driver.find_element_by_css_selector('a.next').click()
    get_page()


driver.get(url)
get_page()
driver.quit()
