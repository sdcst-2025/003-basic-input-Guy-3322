#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
radius = float(input("what is the radius:"))
hight = float(input("what is the hight:"))
cSquare = hight**2+radius**2
slant = math.sqrt(cSquare)
pi_value = math.pi

sa = pi_value*(radius**2)+pi_value*radius*slant
print(f"The surface area is {sa}")