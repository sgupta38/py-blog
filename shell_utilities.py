##
##  Demonstrates use of various shell utilities such as copy, rename using shutil module
##

import shutil

## copies the file to destined folder [make sure destination folder exists]
shutil.copy('files.py', 'tutorials')

## Also, u can copy wih renaming like this,
shutil.copy('files.py', 'tutorials\\myfile.py')

## To copy the whole folders and files, use 'copytree'
shutil.copytree('tutorials', 'tutorials_backup')

## To move the file from one location to another. Notice that file is no longer present at older location.
shutil.move('tutorials\\myfile.py', 'c:\\')

## However, there is no rename but u can use move() like this,
shutil.move('tutorials_backup\\files.py', 'tutorials_backup\\Yourfile.py')
