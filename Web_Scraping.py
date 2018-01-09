##
##  This demonstarates the 'Web Scraping'. In this, I am just printing the 'Share Price' of 'Quick Heal Technology' share.
##
## Prerequisite: pip intsall beautifulsoup4

import bs4, requests

res = requests.get('http://www.moneycontrol.com/india/stockpricequote/computers-software/quickhealtechnologies/QHT')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#Bse_Prc_tick > strong')
# price = elems[0].text.strip()
#
# print('Price of the item is: ' + price)
print(elems[0].text.strip())
