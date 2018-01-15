##
##  Author: Sonu Gupta
##  Name: lazyme.py

##  Data: 12-jan-18
##

## Note:    I use chrome, so I needed to install 'chromedriver' explicitly and provide its path. If you are using firefox, it is very simple to use it.
##          For chrome, there is bug in swicting 'tabs'.
##          So following is the workaround for getting things done: "JavaScript + using chrome windows handle for travesrsing within tabs"
##

import time
from selenium import webdriver

browser = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
browser.get('https://www.google.co.in')

# ## Opening the new tab: GMAIL

browser.execute_script("window.open('');")                              # This will open the new tab
browser.switch_to.window(browser.window_handles[1])                  # This will shift the focus to newly opened tab
browser.get('https://mail.google.com')                                 # This will open the URL.

# ## Opening the new tab: Facebook

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[2])
browser.get('https://www.facebook.com')

# ## Opening the new tab: jci.github.com

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[3])
browser.get('https://github.com/')

# Notice that, after opening so many tabs, I wanted to return to the first tab(index 0). So, this will simply shift the focus to first tab
browser.switch_to.window(browser.window_handles[0])

quit()
