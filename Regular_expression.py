## search() -> returns match objects
## findall() ->returns a list of strings

import re
message = 'Hey folks you can call me at my number 91-7057575757 or at office line 91-9999999999'

## use raw string cause, regular expressions often use '\' [backslash] characters
phoneNumRegex = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d') #\d--> digit

## Search()
#mo = phoneNumRegex.search(message) # mo = Match Object   Search()-->Finds first occurance
#print(mo.group()) # .group() --> tells actual text.


##findall()
print(phoneNumRegex.findall(message)) # mo = Match Object

## when regex is passed with grouping format, findall() functio returns the list of tuples of strings
phoneNumRegex = re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d)') #\d--> digit
print(phoneNumRegex.findall(message)) ## Notice the output, 2 tuples are returned based on grouping

phoneNumRegex = re.compile(r'((\d\d)-(\d\d\d\d\d\d\d\d\d\d))') #\d--> digit
print(phoneNumRegex.findall(message)) ## Notice the output, 3 tuples are returned based on grouping

## Character classes
#               \d digit
##              \D Anything except digit
##              \w Any letter, numeric, underscore character
##              \W Anything that is not letter, numeric, underscore character [mainly includes punctuation marks]
##              \s Any space, tab, newline character
##              \S Anything that is not space, tab, newline character

message = '10 cheese burger, 20 cokes, 7 dosas '

phoneNumRegex = re.compile(r'\d+\s\w+')
print(phoneNumRegex.findall(message))

### Creating own regex classes using []
vowelRegex = re.compile(r'[aeiouAEIOU]')
message = 'Robocop eats baby food'
print(vowelRegex.findall(message))

##      Two find two vowels in a row
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')   ## This will find the regex having two vowels in a row {2}
message = 'Robocop eats baby food'
print(vowelRegex.findall(message))


##     ^ Negative character classes --> This will match everything that is not in regex
vowelRegex = re.compile(r'[^aeiouAEIOU]')   ## This will find everything including punctuation marks and spaces except vowels
message = 'Robocop eats baby food'
print(vowelRegex.findall(message))

### Beginwith "^"" and Endwith "$""

beginWithRegex = re.compile(r'^Hello')  ## Notice that String should begin with 'Hello'
message = 'Hello jon how are you!'
print(beginWithRegex.findall(message))

endWithRegex = re.compile(r'world!$')  ## Notice that string should end with literal 'world!''
message = 'how beautiful this world!'
print(endWithRegex.findall(message))

#3 ^both$ means pattern must match entire string
allDigitRegex = re.compile(r'^\d+$') # one or more digit
message = '123445'
print(allDigitRegex.findall(message))

## r'.' --> means anything except newline "." character is looking for single character
atRegex = re.compile(r'.{1,2}at')
message = 'The cat in the hat sat on the flat mat'
print(atRegex.findall(message))


## Parsing
message = 'First Name: Sonu Last Name: Gupta'
nameRegex = re.compile('First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(message))

## (.*) ---> greedy mode (as much text as possible)
## (.*?) ---> Non greedy mode

serve = '<To server humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))   ## This is not greedy will stop after looking first angle bracket

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))


## (.*) --> searches pattern for everything except newline characters
message = 'hey folks.\n How are you?\n Winter is coming'
dotStar = re.compile(r'.*')
print(dotStar.search(message))    ## Notice that (.*) has matched everything till new line

## To match everything even including newline characters with (.*) we have to pass second parameter to compile function as 're.DOTALL'
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(message))    ## Notice that (.*) has matched everything including newline too

## Case insensitive match re.IGNORECASE / re.I
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
message = 'Robocop eats baby fOOd'
print(vowelRegex.findall(message))
