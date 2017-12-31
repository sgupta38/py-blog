##
## This covers the file operations and shelve module in python

import os

## hello.txt is the file having some contents.
filepath = os.path.join(os.getcwd(), 'hello.txt')


## 'open' function is by default in 'read mode'. Note that it always returns 'Handle'. And this 'Handle' further has many modules such as 'read, write etc.'
readFile = open(filepath)
print(readFile.read())      # will print read contents
readFile.close()            # Make sure to close the file when done.


## Once handle is closed and u wanna acess contents, u again need to open the file.
## So better store the contents in some variable and use it whenever you require
readFile = open(filepath)
content = readFile.read()
print(content)      # will print read contents
readFile.close()


## 'readlines()' returns the contents in the list format
readFile = open(filepath)
content = readFile.readlines()
print(content)
readFile.close()

##      Writing to the files.
##
##      You need to open the file in 'write(w)' or 'append(a)' mode.
##      If file doesnt exists, it will be created.

helloFile = open('hello2.txt', 'w')
helloFile.write('New file created!!!!!!!\n')   # Notice that unlike print(), write doesnt add new line. we have to give it explicitly
helloFile.write('New file created!!!!!!!')
helloFile.close()

print()

##
##      Using shelve module [This is similar to using INI files in windows which has format of key = value pair]
##      OR consider it as a 'database' entity which we can use to store complex objects.
##
##      Often it becomes necessary to store complex dictionaries, lists and data, we can use the shelve module similar to files
##      for storing our data and whenever in any prorgram we need it, we can open an access the same
import shelve
shelfFile = shelve.open('myData')
shelfFile['cats'] = ['Zophie', 'pooka', 'simon', 'Fat-tail']
shelfFile['hobbies'] = ['Trekking', 'Dancing', 'Games', 'Reading']
shelfFile.close()

shelfFile = shelve.open('myData')
print(shelfFile['cats'])
print(shelfFile['hobbies'])

print()

## We can use keys() and values() function also to get data in proper list format
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
