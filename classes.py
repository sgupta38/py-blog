##
# This demontrates how classes are used inside python.
##


# This is our class
class Planet:

    # This is called as 'Class Level Attribute'. This is accesses by Class and its instances too
    shape = 'round'

    ## This __init__ acts as a constructor. Whenever we create object of class, this method is invoked. ('self' is similar to 'this' in c++).
    #
    #
    #   Note: Any method that has 'self' as its parameter is called as 'Instance Method'. Because this method is invoked by all the instances of class.
    #
    def __init__(self, name , radius):
        self.name = name                  # These are instance level attribute
        self.radius = radius

    def info(self):
        print(f'{self.name} has radius: {self.radius}')


    #
    # CLASS METHODS:  These methods are accessed by Classes and its Instances too!!
    #
    #
    #  Note: Any method that contains 'cls' as its parameter is called as 'Class level method'.
    @classmethod
    def common(cls):
        print(f'All planets are {cls.shape} in shape.')

    # Static methods neither have access to 'self' (Instance Level attribute) nor 'cls'(Class Level attributes).
    # They have access to only values that we pass.
    # However, these methods are 'Accesible' at 'Class' & 'Instance' Level
    @staticmethod
    def spin(speed = '2000 miles per hour'):  # here we have passed default parameter
        print('planet spins at ' + speed)


earth = Planet('Earth', 200000)
print(f'Planet is: {earth.name}')
print(f'Radius is: {earth.radius}')
earth.info()
print('Eaths shape is: ' + earth.shape)   # class level attribbute accessed by instance too.

sun = Planet('Sun', 200000000)
print(f'Planet is: {sun.name}')
print(f'Radius is: {sun.radius}')
sun.info()
print('Suns shape is: ' + earth.shape)

print(Planet.shape)     # class level attribute
Planet.common()         # class level method

## Accessing static method
Planet.spin()                       # printed default parameter
earth.spin('very high speed')       # Notice, default parameter was overriden
sun.spin('vey very high speed')     # Notice, default parameter was overriden
