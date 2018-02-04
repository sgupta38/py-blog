
# This is our class
class Planet:
    shape = 'round'

    def __init__(self, name , radius, gravity):
        self.name = name                  # These are instance level attribute
        self.radius = radius
        self.gravity = gravity

    def info(self):
        print(f'{self.name} has radius: {self.radius}')

    @classmethod
    def common(cls):
        print(f'All planets are {cls.shape} in shape.')

    @staticmethod
    def spin(speed = '2000 miles per hour'):  # here we have passed default parameter
        print('planet spins at ' + speed)
