import re
message = 'my phone number is 91-8080809011. What is  yours?'


phoneNumRegex = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())


##
## We can also group the regular expression. For instance, we will group country code and actual phone number and will print it.
##
## Paranthesis have special meaning in regular expression as they decide start and end
phoneNumRegex = re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1)) # This will print country code
print(mo.group(2)) # This will print actual phone number

## Phone number may also include paranthesis, use escape character for that '\'
##
## (91) 7070707070
phoneNumRegex = re.compile(r'(\(\d\d\)) (\d\d\d\d\d\d\d\d\d\d)')
message = 'my phone number is (91) 8080809011. What is  yours?'
mo = phoneNumRegex.search(message)
print(mo.group())
print(mo.group(1)) # This will print country code
print(mo.group(2)) # This will print actual phone number


##
## Pipe will match one or more possible groupss
## This will search for keyword starting with bat
batRegex = re.compile(r'bat(man|cat|copter|bat)')
message = 'Hey batboy, batcopter lost a wheel to batman'
print(batRegex.findall(message)) # Lists all the occurences specified in regualr expression. And ignores those are out of context like batboy

##
##Note: Notice that 'search()' Method returns 'None' if no matched pattern was found. Tying to print it will throw an exception
mo = batRegex.search('badboy doing bash')
#print(mo.group())
