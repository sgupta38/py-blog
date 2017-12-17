## Some many similarities in strings and lists

## Strings in python are IMMUTABLE.
## Note: In mutable values we save 'References'

print(list('Hello'))

name = 'Sonu Gupta'

for letter in name:
    print(letter)

print()

##  List value is 'Mutable' while, String values are 'Immutable'. That is string values cant be changed
name = 'Sonu'
print(name[2])

# You cant assign value to string
#name[2] = 'e'

# The only way is to create new string and do slice manipulations

## When list is applied to some variable, you are actually applying its 'REFERENCE'
spam = 42
cheese = spam
spam = 100
print(cheese)
print(spam)   # Value of spam is not changed

## Now, lets see lists
spam = [0,1,2,3,4,5]
cheese = spam
print(cheese)
cheese[1] = 'sonu'
print('cheese ' + str(cheese))

print('spam ' + str(spam))  # Notice that since its reference, value of spam is also changed


print()
print()
print()

## Notice with the local variable scope in functions, when we pass list to function, the work is in exactly opposite way.
#  We think local variable will be destroyed once it is out of scope.
# But, if we pass 'List' as parameter, in real 'Reference ' is passed.
# Thus folowing awkward result can be seen
def eggs(someParam):
    someParam.append('Hello')  # Though this variable scope is destroyed, reference is changed. This can include 'BUGS'

spam = [0,1,2]
eggs(spam)
print(spam)


## Deepcopy import copy
import copy


spam = [1,2,3,4]
cheese = copy.deepcopy(spam)  # This allows to create brand new reference instead of refering the previous reference

print('spam ' + str(spam))

cheese[2] = 5   #Changing this value doesnt change original 'spam' contents
print('cheese ' + str(cheese))
