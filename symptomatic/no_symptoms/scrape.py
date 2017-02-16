import bs4
import urllib


url = 'http://www.rightdiagnosis.com/symptoms/no_symptoms/causes.htm'
html = urllib.urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")

# items = soup.select('#wd_content')
sibs = soup.select('#generalinfolinks')[0].previous_siblings

for sib in sibs:
    if sib.name == 'ul':
        break

items = sib.select('li')

for item in items:
    condition = item.select('a')[0].text.lower().strip()
    print condition



# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import json


# driver = webdriver.Firefox()
# symptom = None
# factors_link = None


# def diagnose():
#     sib = driver.find_elements_by_css_selector('div#generalinfolinks')

#     # for link in links:
#     for i in range(0, len(links)):
#         link = links[i]
#         print 'link ' + str(i) + ' / ' + str(len(links))

#         global factors_link
#         global symptom

#         factors_link = link
#         symptom = link.text.lower().encode('utf-8')
#         data[symptom] = {}

#         link.send_keys(Keys.COMMAND + Keys.RETURN)
#         time.sleep(2)
#         driver.switch_to_window(driver.window_handles[1])

#         options = driver.find_elements_by_css_selector('.form li')
#         while len(options) == 0:
#             print '    options == 0'
#             time.sleep(1)
#             options = driver.find_elements_by_css_selector('.form li')

#         for j in range(0, len(options)):
#             print '    factor ' + str(j) + ' / ' + str(len(options))
#             sel_factors(j)

#         driver.close()
#         driver.switch_to_window(tab1)



# url = 'http://www.rightdiagnosis.com/symptoms/no_symptoms/causes.htm'
# driver.get(url)
# diagnose()
# driver.quit()

# print data
# with open('diagnoses.json', 'w') as fp:
#     json.dump(data, fp, sort_keys=True, indent=4)
