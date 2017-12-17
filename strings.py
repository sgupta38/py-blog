#String Methods always returns the new Strings unlike modifyings strings in place.

# Since strings are immutable, impossible to modify in place
spam = 'Hello World'
print(spam)

caps = spam.upper()
print(caps)
print(spam)

low = caps.lower()
print(low)


#isupper(), islower()
print(spam.islower())

# we can also do like this
print('hello'.upper())
print('WORLD'.lower())

spam = "Jai Maharshtra"
print('above string is title string: ' + str(spam.istitle()))

print('helloisaplha'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print()
print('hello world! '.isspace())
print('hello world!'[5].isspace())
print('hello world!'[5])

print()
print("Similar to upper(), lower() you can use title()")
spam = 'the champ is here'
print(spam.title())

print()
print("startswith()")
spam = 'the champ is here'
print(spam.startswith('the'))
print(spam.startswith('t'))

print(spam.endswith('the'))
print(spam.endswith('here'))
print(spam.endswith('e'))
print()


print('WORLD'.lower().isupper())
print('WORLD'.lower().islower())

# join() methos is used when we have lots of strings that needs to be joined on single strings
spam = ', '
animals = ['cats', 'bats', 'rats']
print(spam.join(animals))

print('\n\n'.join(['cats', 'bats', 'rats']))

# split() method is exactly opposite of join(), it gives the list of strings
print('my name is sonu'.split()) # bydefault spliyts on white space chgaracter
print('my name is sonu'.split('m')) # cuts out 'm'
print('my name is sonu'.split('s')) #cuts out 's'

## ljust(), rjust(), center() These gives the padded version of strings.[Right justify or left justify the string]

print('Hello'.rjust(10))
#Tu put the atrericks instead of spaces;
print('Hello'.rjust(10, '*'))


#you can see the length is 10
print('Hello'.ljust(10, '-'))
print(len('Hello'.ljust(10)))

#center() will puth the code in center
print('Hello'.center(20))
print('Hello'.center(20, '='))

## strip(), rstrip(), lstrip() sometimes u might want to strip oput the characters like spaces, newlines, tabs from left / right
spam = 'Hello'.rjust(20)
print(spam)
spam = spam.strip() # will remove the white space [returns brand new string]
print(spam)

print('Normal strip()') # removes whitespace from the both side of the string
spam = '       *****          '
print(spam)
spam = spam.strip()
print(spam)

print('lstrip()') # removes whitespace from the left side of the string
spam = '       *****          '
print(spam)
spam = spam.lstrip()
print(spam)

print('rstrip()')  # removes whitespace from the right side of the string
spam = '       *****          '
print(spam)
spam = spam.rstrip()
print(spam)

##3 You can remove any characters from the string
spam = 'spamspameggsspamspamspamspam'
spam = spam.strip('spam')
print(spam)

##replace()
spam = 'Hello World!'
spam = spam.replace('World', 'Nature')
print(spam)

spam = spam.replace('H', 'Be')
print(spam)

### String formatting: Sometimes it gets tedious  to concat the strings using + operator
## But, python has made this task easy. You just have to write %s[Conversion specifiers] like you use in c/c++
name = 'sonu'
place = 'Irani Cafe'
time = '6 pm'

## Normal way
spam = 'Hello ' + name + ', you are invited for party at ' + place + '. Please Come by ' + time + '.'
print(spam)

## Another useful way: Lot easier to read.
## This technique truly makes your code more readable.
spam = 'Hello %s, you are invited for party at %s. Please come by %s.' % (name, place, time)
print(spam)







############################################################
print('Do you want to continue?')
answer = input()
# This can be useful while taking inputs from user. [user might enter Yes, YES, yEs, or any other variant but meaning wont be changed]
if answer.lower() == 'yes':
    print('You can continue')
else:
    print('Good Bye!')
############################################################
