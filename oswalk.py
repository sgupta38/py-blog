##
## os.walk() used to for file retrievals and manipulations. Its in-built function and you dont need to use combination of other 'list' functions.

## os.walk() functions return value is mainly used in 'for loops'. It returns 3 values on each iteration of loop.
##
##  using this we can do several file operations on a big database of files like rename, delete or modify particular files etc.
import os

for foldername, subfoldernames, filenames in os.walk('D:\\IP'):
    print('The folder is :' + foldername)
    print('The sub-folder in ' + foldername + ' are: ' + str(subfoldernames))
    print('The filenames in ' + foldername + ' are: ' + str(filenames))
    print()
