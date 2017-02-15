import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
symptom = None
factors_link = None


def diagnose():
    links = driver.find_elements_by_css_selector('div.adult li a')

    for link in links:
        global factors_link
        global symptom

        factors_link = link
        symptom = link.text

        link.send_keys(Keys.COMMAND + Keys.RETURN)
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])

        options = driver.find_elements_by_css_selector('.form li')
        for j in range(0, len(options)):
            print 'factor ' + str(j) + ' / ' + str(len(options))
            sel_factors(j)

        driver.close()
        driver.switch_to_window(tab1)


def sel_factors(j):
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

    factor_type = section.find_elements_by_css_selector('legend')[0].text
    factor = option.text

    checkbox = option.find_element_by_tag_name('input')
    checkbox.click()

    submit = driver.find_elements_by_css_selector('#FindCause')[0]
    submit.click()
    time.sleep(2)

    conditions = driver.find_elements_by_css_selector('.expandable.factors a:not([class])')

    for c in conditions:
        ailment = c.text
        print symptom + ', ' + factor_type + ' ' + factor + ' = ' + ailment

    print '------------------------------'
    driver.close()
    driver.switch_to_window(tab1)
    factors_link.send_keys(Keys.COMMAND + Keys.RETURN)
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[1])


url = 'http://www.mayoclinic.org/symptom-checker/select-symptom/itt-20009075'
driver.get(url)
tab1 = driver.current_window_handle
diagnose()
driver.quit()
