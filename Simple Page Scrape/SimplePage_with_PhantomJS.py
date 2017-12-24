from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')

driver.get('http://python.org')
# gets the python webpage script

html_doc = driver.page_source

print html_doc