'''
The math module in Python provides functions to convert between degrees and radians:

math.degrees(x): Converts an angle from radians to degrees.
math.radians(x): Converts an angle from degrees to radians.
'''

import math

# Define an angle in radians
angle_rad = math.pi / 4
# Convert radians to degrees
angle_deg = math.degrees(angle_rad)
print(f"{angle_rad} radians is equal to {angle_deg} degrees")

# Define an angle in degrees
angle_deg = 60
# Convert degrees to radians
angle_rad = math.radians(angle_deg)
print(f"{angle_deg} degrees is equal to {angle_rad} radians")