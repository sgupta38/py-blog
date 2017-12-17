for i in [2,4,6,8]:
    print(i)

print(range(4))
print(list(range(4)))

#print the step 2 till 100
print(list(range(0, 100, 2)))
spam = list(range(0,100,2))
print(spam[10])

#print list elements
supplies = ['pen', 'pencils', 'staplers', 'notebooks']
for i in range(len(supplies)):
    print(supplies[i])

#
#Multiple assignments in python
#

# Traditional way
cat = ['fat', 'meow', 'cruel']

size = cat[0]
sound = cat[1]
nature = cat[2]

print(size)
print(sound)
print(nature)

## Python way multiple assignments
cat1 = ['fat1', 'meow1', 'cruel1']

size1, sound1, nature1 = cat1

print('')

print(size1)
print(sound1)
print(nature1)

########
print('Assign multiple values to multiple variable at the same time')
name, age, sex = 'sonu', 24, 'male'
print(name)
print(age)
print(sex)

#########
print(' Swapping two variables')

a = 'AAA'
b = 'BBB'

print('   Befor Swap   ')
print('a = ' + a)
print('b = ' + b)

a,b = b,a

print('   After Swap   ')

print('a = ' + a)
print('b = '+ b)
