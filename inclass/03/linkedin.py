from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/uas/login')

login = driver.find_element_by_id('session_key-login')
login.send_keys('lavigne@saaaam.com')

password = driver.find_element_by_id('session_password-login')
password.send_keys('rudyrudy')
password.send_keys(Keys.RETURN)
time.sleep(3)

search_term = 'police'

url = 'https://www.linkedin.com/search/results/index/?keywords=' + search_term
driver.get(url)
time.sleep(3)

buttons = driver.find_elements_by_css_selector('.search-result--person button')
buttons[0].click()

# time.sleep(5)
# driver.quit()
