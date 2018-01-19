## Youtube downloader for firefox

from selenium import webdriver
import time


print('Enter the url: ')
url = input()
downloadurl = url.replace('https://www.youtube', 'https://www.ssyoutube')
print('Modified URL ' + downloadurl)


browser = webdriver.Firefox()
browser.get(downloadurl)

downloadElem = browser.find_element_by_css_selector('.download-icon')
downloadElem.click()

print('Success..!!')
