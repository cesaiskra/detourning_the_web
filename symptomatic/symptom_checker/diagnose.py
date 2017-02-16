import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


driver = webdriver.Firefox()
symptom = None
factors_link = None


def diagnose():
    links = driver.find_elements_by_css_selector('div.adult li a')

    # for link in links:
    for i in range(0, len(links)):
        link = links[i]
        print 'link ' + str(i) + ' / ' + str(len(links))

        global factors_link
        global symptom

        factors_link = link
        symptom = link.text.lower().encode('utf-8')
        data[symptom] = {}

        link.send_keys(Keys.COMMAND + Keys.RETURN)
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])

        options = driver.find_elements_by_css_selector('.form li')
        while len(options) == 0:
            print '    options == 0'
            time.sleep(1)
            options = driver.find_elements_by_css_selector('.form li')

        for j in range(0, len(options)):
            print '    factor ' + str(j) + ' / ' + str(len(options))
            sel_factors(j)

        driver.close()
        driver.switch_to_window(tab1)


def sel_factors(j):
    sections = driver.find_elements_by_css_selector('fieldset')
    while len(sections) == 0:
        print '        sections == 0'
        time.sleep(1)
        sections = driver.find_elements_by_css_selector('fieldset')

    count = 0
    for section in sections:
        length = len(section.find_elements_by_css_selector('li'))
        if j >= count and j < count + length:
            break
        else:
            count += length

    options = driver.find_elements_by_css_selector('.form li')
    option = options[j]

    factor_type = section.find_elements_by_css_selector('legend')[0].text.lower().encode('utf-8')
    factor = option.text.lower().encode('utf-8')

    data[symptom][factor_type] = {}
    data[symptom][factor_type][factor] = []

    checkbox = option.find_element_by_tag_name('input')
    checkbox.click()

    submit = driver.find_elements_by_css_selector('#FindCause')[0]
    submit.click()
    time.sleep(2)

    conditions = driver.find_elements_by_css_selector('.expandable.factors a:not([class])')

    print '        ' + str(len(conditions)) + ' conditions'

    for c in conditions:
        ailment = c.text.lower().encode('utf-8')
        data[symptom][factor_type][factor].append(ailment)
    #     print symptom + ', ' + factor_type + ' ' + factor + ' = ' + ailment

    # print '------------------------------'
    driver.close()
    driver.switch_to_window(tab1)
    factors_link.send_keys(Keys.COMMAND + Keys.RETURN)
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[1])

data = {}
url = 'http://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075'
driver.get(url)
tab1 = driver.current_window_handle
diagnose()
driver.quit()

print data
with open('diagnoses.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
