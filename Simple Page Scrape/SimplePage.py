from selenium import webdriver

driver = webdriver.Chrome(executable_path = r'/Users/sachinjose/Downloads/chromedriver')

driver.get('http://python.org')
# gets the python webpage script

html_doc = driver.page_source

print html_doc