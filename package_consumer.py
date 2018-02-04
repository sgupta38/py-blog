##
## This file is demonstrating the usage of 'package' in python

## For this particular file, 'package_usage' folder is acting as a package which is having multiple modules.


## syntax: from package.filename import class [or functions]

from package_usage.Planet import Planet
from package_usage.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000, 8)
naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_volume = planet_vol(naboo.radius)

print('naboo mass is: ' + str(naboo_mass))
print('naboo volume is: ' + str(naboo_volume))
