# Distance Between Two Points on Earth
---------------------------------
# Import math Library

import math

# Taking and converting coordinates from degrees to radians

t1 = (float(input('Give me the first latitude')) * 3.14 / 180)
g1 = (float(input('Give me the first longitude')) * 3.14 / 180)

t2 = (float(input('Give me the second latitude')) * 3.14 / 180)
g2 = (float(input('Give me the second longitude')) * 3.14 / 180)

# Putting values into the formula

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

# Printing the distance in kilometers

print(f'The distance between the points is {distance:.3f} km.')
