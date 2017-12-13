print('Please enter the name')
name = input()
if name:            # If you enter anything, it is considered as 'TRUTHY' value
    print('Thanks for entering the name')
    print('You have entered: ' + name)
else:   # Blank string is considered as 'FALSEY' value
    print('Awwww....You should have entered you name')
