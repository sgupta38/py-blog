def div42by(divideby):
    try:
        return 42/divideby
    except:     # Either you can specify specific error or not e.g, except ZeroDivisionError:
        print('You Tried divide by zero my buoy..!!')

print(div42by(2))
print(div42by(3))
print(div42by(21))
print(div42by(0))
print(div42by(1))
