#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

Radius = int(input("What is the radius of the sphere:"))
Radiuscubed=(Radius**3)
import math
pi_value = math.pi

Volume = 4/3*pi_value*Radiuscubed

print(f"The volume of the sphere is {Volume}")