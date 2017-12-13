print('How many cats you have')
num = input()
try:
    if int(num) >= 5:
        print('So many cats')
    else:
        print('Few cats')
except:
    print('Please enter the numeric value.')
