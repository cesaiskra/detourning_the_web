from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import creds


driver = webdriver.Chrome()

driver.get('https://hangouts.google.com/')
time.sleep(1)

sign_in = driver.find_element_by_id('gb_70')
sign_in.click()
time.sleep(1)

email = driver.find_element_by_id('Email')
email.send_keys(creds.email)
driver.find_element_by_id('next').click()
time.sleep(1)

netid = driver.find_element_by_id('netid')
netid.send_keys(creds.username)
password = driver.find_element_by_id('password')
password.send_keys(creds.password)
password.send_keys(Keys.RETURN)
time.sleep(2)

select_phone = driver.find_elements_by_css_selector('.g-Ue-b, .g-Ue-ua-b')[1]
select_phone.click()

iframe = driver.find_element_by_css_selector('#hangout-landing-chat iframe')
# print iframe
# innerDoc = driver.execute_script('return arguments[0].contentDocument || arguments[0].contentWindow.document;', iframe)
# print innerDoc

driver.switch_to.frame(iframe)
# print driver
number_button = driver.find_element_by_tag_name('button')
number_button.click()
time.sleep(1)
number_box = driver.find_elements_by_tag_name('button')[-1]
print number_box
# driver.execute_script("arguments[0].style.visibility='visible';", number_box)
# number_box.send_keys('8002420100')
# number_box.send_keys(Keys.RETURN)

# driver.switch_to.default_content()

# iframe = driver.find_element_by_css_selector('#hangout-landing-chat iframe')
# innerDoc = iframe.contentDocument || iframe.contentWindow.document
# number_button = innerDoc.find_element_by_tag_name('button')[0]
# number_button.click()
# number_box = innerDoc.find_element_by_tag_name('button')[-1]
# password.send_keys('8002420100')
# password.send_keys(Keys.RETURN)






# time.sleep(1)

# search_term = 'police'

# url = 'https://www.linkedin.com/search/results/index/?keywords=' + search_term
# driver.get(url)
# time.sleep(1)

# buttons = driver.find_elements_by_css_selector('.search-result--person button')
# buttons[0].click()

# time.sleep(5)
# driver.quit()
