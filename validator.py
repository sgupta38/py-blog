 #Checking mobile number format 91-7057343434

def isPhoneNuber(text):
    if len(text) != 13:
        return False # Total len should be equal to 13
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False #Checking Country code
    if text[2] != '-':
        return False # No '-'

    for i in range(3, 13):
        if not text[i].isdecimal():
            return False # not valid numbers

    return True

print(isPhoneNuber('91-7057343243'))

## Checking whether the given message contains phonenumber or not
foundnumber = False;
message = 'Hey folks you can call me at my number 91-7057575757 or at office line 91-9999999999'

for i in range(len(message)):
    chunk = message[i:i+13]
    if isPhoneNuber(chunk):
        print('Phone number found: ' + chunk)
        foundnumber = True;

if not foundnumber:
    print('Couldnt found any number')
