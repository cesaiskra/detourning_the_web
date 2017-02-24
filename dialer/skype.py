import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import creds


driver = webdriver.Chrome()
driver.get('https://web.skype.com')

username = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username.send_keys(creds.skype_username)
driver.find_element_by_id('signIn').click()
time.sleep(1)

password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "i0118"))
)
password.send_keys(creds.skype_password)
driver.find_element_by_id('idSIButton9').click()

dialpad = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "menuItem-dialpad"))
)
time.sleep(2)
dialpad.click()

number_box = driver.find_element_by_css_selector('.SkypeOutHeader-inner input')
number_box.send_keys('+1 8002420100')
password.send_keys(Keys.RETURN)

# number_keys = driver.find_elements_by_class_name('DialPad-key')

# nums = {}
# for key in number_keys:
#     nums[key.get_attribute('data-key')] = key

# print nums
