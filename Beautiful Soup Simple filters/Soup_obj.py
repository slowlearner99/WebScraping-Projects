from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'/Users/sachinjose/Downloads/phantomjs/bin/phantomjs')
driver.get('http://python.org')
html_doc=driver.page_source
soup=BeautifulSoup(html_doc,'lxml')
print soup.prettify()
driver.quit()