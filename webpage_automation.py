##
##  This covers the browser automation[i.e, opening URL, filling form, submitting] done using pythong script.
##
## Here, I am demonstrating the automated gmail login.


## Note: I was getting bunch of errors while doing this. Make sure you install all the following tools to their latest version.
##  I already had firefox with me. Since, it was not compatible with 'selenium' version, it was crashing the app. So keep all tools updated.
## Prereuisite:
## 1] pip install selenium
## 2] install 'geckodriver'
## 2] Mozilla Firefox installed


from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.google.co.in/')            # opens google.com

LoginElem = browser.find_element_by_css_selector('div.gb_Q:nth-child(1) > a:nth-child(1)')  #Finds 'gmail' link at upper right corner
LoginElem.click()

UsernameElem = browser.find_element_by_css_selector('#identifierId')    # Finds 'Username' edit box
UsernameElem.send_keys('jonsnow@gmail.com')                             # Writes to 'Username' edit box

NextElem = browser.find_element_by_css_selector('.CwaK9')               # Finds 'Next' button
NextElem.click()                                                        # Clicks on 'Next' button

## Sleep for some time till the page loads :D
time.sleep(5)

PasswordElem = browser.find_element_by_css_selector('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)') # Finds 'Password' edit box
PasswordElem.send_keys('**********')                                            # Writes to 'Password' edit box

NextElem = browser.find_element_by_css_selector('.CwaK9')    # Finds 'Next' button    Note: I tried using previously defined.However, you have to find again and click.
NextElem.click()                                             # Clicks on 'Next' button

## BOOOOOOMMM...!! Thats it you are done!!

##  Following are some automation with browser can be used for going 'back', 'forward', 'refresh', 'quit' the browser
browser.back()
browser.refresh()
browser.forward()
browser.quit()

##
##      To read the contents of webpage, do folowing.
browser = webdriver.Firefox()
browser.get('https://www.goodreads.com/')

readElem = browser.find_element_by_css_selector('.sellingPointBoxLeft > p:nth-child(2)')
print(readElem.text)
