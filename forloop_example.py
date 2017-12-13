print('Demontsrating for loop')


# For the for loop: Number rmentioned in the range itself is never counted. e.g, 10
# Goes upto range.
# One argument for 'range(end)'
for i in range(10):
    print('Inside for loop at i = ' + str(i))


# You can also provide the index number to start with


#Two argumnets for 'range(start, end)' 
for i in range(12, 16):
    print('Inside for loop at index: ' + str(i))

#Three argumnets for 'range(start, end, step)' 
for i in range(0, 20, 2):
    print('Inside for loop at index: ' + str(i))

#Three argumnets for 'range(start, end, step)' ----> NEGATIVE numberf
for i in range(5, -1, -1):
    print('Inside for loop at index: ' + str(i))
