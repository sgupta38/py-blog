import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('Enter the url: ')
url = input()
downloadurl = url.replace('https://www.youtube', 'https://www.ssyoutube')
print('Modified URL ' + downloadurl)

driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
driver.get(downloadurl)
print(driver.title)

time.sleep(10)
#elem = driver.find_element_by_class_name('def-btn-box')
elem = driver.find_element_by_xpath(By.XPATH("//div[@class='def-btn-box']"));
elem.click()


print('Success..!!')
