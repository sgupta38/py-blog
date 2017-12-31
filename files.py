##
##          Basic file related functions
##

print('C:\\Program Files\\hello.txt')   # Normal string with two \\

print(r'C:\Program Files\hello.txt')    # Raw String with single \

## We can also connect the full file path if we have list as follows:
## Note: This will work on windows only cos in Linux & Mac '/' is used for representing path
mypath = '\\'.join(['C:', 'Program Files', 'VLC', 'vlc.exe'])
print(mypath)


####  We need to make our python script generic so that it can on all operating systems.
####  Anything related to path can better be handled by using 'os' module

import os
mypath = os.path.join('C:','Program Files(x86)', 'Python') # https://docs.python.org/3/library/os.path.html#os.path.join
print(mypath)

## current working directory
cwd = os.getcwd()
print(cwd )

## change the working directory
os.chdir('c:\\')
print(os.getcwd())

os.chdir(cwd)
print(os.getcwd())

## Absolute file path vs relative file path
##

abspath = os.path.abspath('spam.png')   # Notice that we have passed relative path, it will be convefted to absolute path
print(abspath) ## This will simply append to original path

abspath = os.path.abspath('..\spam.png')   # Notice that we have passed relative path, it will be convefted to absolute path
print(abspath) ## This will simply come to parent directory one step ahead and will apend the name

print(os.path.isabs('..\spam.png'))    # FALSE
print(os.path.isabs('c:\\Program\\'))  # TRUE

##  This function provides the respective relative path, you need to privide full path as first para and second para whos rel path is needed.
relpath = os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
print(relpath)

## To find the dirname of given absolute path, use
dirname = os.path.dirname('c:\\folder1\\folder2\\sonu.png')
print(dirname)

## To find/get just the filename from absolute path use,
basename = os.path.basename('c:\\folder1\\folder2\\sonu.png')
print(basename)

## To find whether file exists in hard drive use this,

print(os.path.exists('c:\\folder1\\folder2\\sonu.png')) # Will return FALSE, since file doesnt exists

print(os.path.exists('c:\\windows\\system32\\calc.exe')) # Will return TRUE, since file actually exists

## To check whether its a foldername or filename use,
print()
print(os.path.isfile('c:\\windows\\system32\\calc.exe'))
print(os.path.isfile('c:\\folder1\\folder2'))

print(os.path.isdir('c:\\windows\\system32\\calc.exe'))
print(os.path.isdir('c:\\windows\\system32\\'))
print()

## To get the size of file use getsize which returns 'integer value' in no. of bytes
print(os.path.getsize('c:\\windows\\system32\\calc.exe'))
print(os.path.getsize('D:\\PrivateRepo\\py_blog\\browser.py'))

## To list the folders and files use this,
print(os.listdir('D:\\PrivateRepo\\py_blog\\'))

## We can find out the total sie of folder using following snippet,

totalsize = 0;
for filename in os.listdir('D:\\PrivateRepo\\py_blog'):
    if not os.path.isfile(os.path.join('D:\\PrivateRepo\\py_blog', filename)):
        continue
    print(os.path.join('D:\\PrivateRepo\\py_blog', filename) + ' ' + str(os.path.getsize(os.path.join('D:\\PrivateRepo\\py_blog', filename))))
    totalsize = totalsize + os.path.getsize(os.path.join('D:\\PrivateRepo\\py_blog', filename))

print('Total size of the above folder is: ' + str(totalsize) + 'bytes')


## We can create folders using this,
os.makedirs('c:\\winter\\is\\coming\\khaleesi') # Check new directory is created
