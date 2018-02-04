Often it gets messy in larger projects to manage huge code.
By refactoring our code into different modules and later using the whole functionality in the form of 'package' can be very useful.
Whenever you create any package, make sure you have a 'folder' which lists all the module files. This folder name acts as 'package name'.

Also, always make sure to create a file named **'__init__.py'** which simply implicates that this particular folder is a 'package' and has multiple modules in it.

Here, this folder is acting as a 'package'. The file in previous directory named **'package_consumer.py'** is using math utility functions from this package.
You can see two functions have been later imported by our main file.
