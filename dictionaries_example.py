##      DICTIONARIES
mycat = {'name':'zophie', 'color':'grey', 'noise':'meow'}

print(mycat['name'])
print(mycat['color'])
print(mycat['noise'])

## Content order matters for 'LISTS'
## Content order doesnt matter for 'DICTIONARIES'

print([1,2,3] == [1,2,3])
print([1,2,3] == [3,2,1])

info = {'name':'sonu', 'age':24, 'job':'developer'}
print(info['age'])

emp = {'age':24, 'job':'developer', 'name':'sonu'}

#Notice that order of contents in two dictionaries are different. But they are equal and gives 'True' as o/p
print(info == emp)


## in and not in
print('sonu' in info)
print('developer' in info)
print('job' not in info)


## Dictionaries are MUTABLE i.e, uses references

## keys(), values() , items()
print()

print(info.keys())
print(info.values())
print(info.items())


## To get the above values in list format
print()
print(list(info.keys()))
print(list(info.values()))
print(list(info.items()))

print()
for k in info.keys():
    print(k)

print()
for v in info.values():
    print(v)

print()
for k, v  in info.items():
    print(k,v)

## TUPLES are similar to LISTS, they just print the data in paranthesis and with comms
print()
print('TUPLE format:')
for i in info.items():
    print(i)


print()
## if key doesnt exists in dictionary, application is crashed
## To prevent that use if statement

if 'salary' in info:
    print(info['salary'])

print()

## we van use get() method to return default value if some key doesnt exists.
print(info.get('name'))
print(info.get('salary', 25000))

## setdefault() method [opposite of get()]
print(info)
info.setdefault('salary', 90000)
print(info)

## Now if yoy tr to re-insert salary , it wont change. cos its already existing in dictionary
print()
info.setdefault('salary', 100000)
print(info)

## This can be useful for verifying whether particular key exists or not in dictionary
