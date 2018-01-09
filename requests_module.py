##
##  This example covers the 'requests' module which is mainly used for downloading web pages and files provided that you have exact URL.

import requests

# requests.get() returns the 'Response Object'

res = requests.get('https://en.wikipedia.org/wiki/Conor_McGregor') # just pass the URL whose contents to be copied

# res.status_code gives the status code e.g, 200 OK, 404 Page not found etc.
print(res.status_code)
print(len(res.text))

print(res.text[:500])  # using slice : printing the first 500 characters of the file

# Simpler way to check for status is using raise_for_status() on response Object

res.raise_for_status()  # If all fine it returns nothing else throws an exception which can be handled in try--catch block.

### To Save the webpage on harddrive, use open()
#
# Note: u MUST open file in the 'Binary mode' in order to maintain the 'Unicode Encoding'
myFile = open('rj.html', 'wb')

##  We can write to the file in chunks using 'iter_content()'
##
## iter_content() returns the chunks in bytes, we can specify how many chunks we want.

for chunks in res.iter_content(10000):
    myFile.write(chunks)    # write() returns no of bytes written to file.

myFile.close()
