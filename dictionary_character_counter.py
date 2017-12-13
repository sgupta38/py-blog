## Normal display of count gives output which is not readable.
## Hence, using the functionality from module 'PPRINT'

import pprint   # Called as 'Pretty Print'


print('Enter the string ')
#message = input()

message = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="Package.xsd">
  <Name>LC-VAC1000</Name>
  <Type>Device</Type>
  <Description>OEM Smart Control</Description>
  <IsRemoveable>true</IsRemoveable>
  <FilePattern>LC-VAC1000-0(.+(xml|bin))?$</FilePattern>
  <BuildDateTime>@BUILD_DATETIME@</BuildDateTime>
  <BuildNumber>@BUILD_NUMBER@</BuildNumber>
  <Hash>@HASH@</Hash>
</Package>'''

count = { }

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#print(count)
pprint.pprint(count)

#Otherway:
# To get the above output in string format, we can use 'pformat' function from PPRINT

strmsg = pprint.pformat(count)
print(strmsg)
