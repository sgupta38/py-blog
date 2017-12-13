def myfunction(name):
    print('So this is your function ' + name)
    print('Congrats, you have successfully executed!!')

def addnumbers(number1, number2):
    return number1+number2

myfunction('babu')
myfunction('sonu')
k = addnumbers(4,6)
print('Addition is ' + str(k))


# print function has two keyword arguments 'END' and 'SEP'
# variants of print function

print('Jai')
print('Maharashtra')

# Notice print always addn new line
# To skip that,

print('Jai', end='')
print('Shivaji')

# print multiple spaces

print('cat', 'mouse', 'monkey')

# To add any separator other than ''
print('cat', 'mouse', 'monkey', sep='#')

ll = 99
print(ll)
