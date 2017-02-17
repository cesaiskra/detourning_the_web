from selenium import webdriver
import time
from sys import argv


driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
driver.set_window_size(1200, 800)

driver.get('http://foxnews.com')


script = '''
var elements = document.querySelectorAll('h1, h2, h3');
for (var i = 0; i < elements.length; i++){
    elements[i].textContent = arguments[0];
}
'''

replacement_text = argv[1]

driver.execute_script(script, replacement_text)
time.sleep(2)
driver.save_screenshot(argv[1].replace(' ', '_') + '.png')
print 'screenshot saved'
time.sleep(5)
driver.quit()

'''
screenshotting lazy loading images
scroll to bottom or make window size == document size
'''
