##
##  This demonstarates the 'Web Scraping'. In this, I am just printing the 'Share Price' of 'Quick Heal Technology' share.
##
## Prerequisite: pip intsall beautifulsoup4

import bs4, requests

def findSharePrice(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    bseElems = soup.select('#Bse_Prc_tick > strong')
    nseElems = soup.select('#Nse_Prc_tick > strong')
    Price = {
                'BSE': bseElems[0].text.strip(),
                'NSE': nseElems[0].text.strip(),
        }

    return Price

    # #
    # # print('Price of the item is: ' + price)
    # print(' BSE price: ' + bseElems[0].text.strip())
    # #
    # # print('Price of the item is: ' + price)
    # print(' NSE price: ' + nseElems[0].text.strip())

SharePrice = findSharePrice('http://www.moneycontrol.com/india/stockpricequote/computers-software/quickhealtechnologies/QHT')
print(' BSE price: ' + SharePrice['BSE'])
print(' NSE price: ' + SharePrice['NSE'])
