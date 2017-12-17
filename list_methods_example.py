# Methods in list are mostly in-place operations

spam = ['sonu', 'jon', 'khaleesi', 'valar', 'morghulis', 'winter']


## index()
k = spam.index('jon')
print(k)

# print('name to search: ')
# name = input()
#
# m = spam.index(name);
# print('Found at index ' + str(m))

## To add in list use 'append()' and 'insert()'

animals = ['cats', 'bat', 'dog']
animals.append('elephant')
print(animals)

animals.insert(2, 'mouse')
print(animals)

animals.remove('mouse')
print(animals)

del animals[1]

print(animals)
animals.append('bat')
animals.append('parrot')
animals.append('bat')
print(animals)

## see here, remove() method will only remove first bat element
animals.remove('bat')
print(animals)



###3 sort() method
#
#
# Note: Python uses 'ASCII - betical Order' i.e, UPPERCASE characters come befor LOWERCASE characters and not 'alphabetical order'
#
data = [3,5,8,1,0,-2,-1, 0.003]
print(data)
data.sort()
print(data)

#with strings too
print(animals)
animals.sort()
print(animals)

## To sort in the reverse order, simply pass the flag 'reverse' as true
animals.sort(reverse=True)
print(animals)

# Note: Python uses 'ASCII - betical Order' i.e, UPPERCASE characters come befor LOWERCASE characters and not 'alphabetical order'
print()
spam = ['alice', 'Bob', 'Ants', 'sonu', 'Shreya', 'Zensar', 'zoo']
print(spam)

spam.sort()   # Notice that capital Uppercase 'Z' comes befor lower case 'a'
print(spam)

spam = ['A', 'a', 'z', 'Z']
print(spam)
spam.sort()
print(spam)
## To sort in true alphabetical order, pass keyword argument
spam.sort(key=str.lower)
print(spam)
