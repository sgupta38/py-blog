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



##  Deleting the file : unlin(), rmdir()
##
##  Note: These functions are often dangerous and permanently deltes the file from your hard disk.
##  Its a good practice to do a "dry run" before actual code.

os.unlink('hello2.txt')         # This is relative path i.e, it searches and deletes the file from current directory

## Deleting the directory. Note that to remove directory, it should be completely empty. If it has some files and sub-folders it will give error.
os.makedirs('core_modules')
os.rmdir('core_modules')

## How to delete directory having files and folders??
##
##   use shutil.rmtree()
import shutil
#shutil.rmtree('tutorials_backup')


##
##          **** Send2Trash ***** : Instead of permanently deleting file from hard disk, this utility moves to 'Trash' of operating system.
##
##     This utility doesnt come with python, you have to explicitly install it using 'pip.exe'
##      ==== pip.exe install send2trash ============

import send2trash
os.makedirs('tutorials')
send2trash.send2trash('tutorials')   ## Notice that this has been deleted and moved to 'Recycle bin'
