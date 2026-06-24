#Exercise 8
#8.py
#Calculate Sphere Dimensions

from math import pi
radius = float(input("What is the radius of the sphere? "))

diameter = 2 * radius
circumference = 2 * pi * radius
surface_area = 4 * pi * (radius ** 2)
volume = (4/3) * pi * (radius ** 3)

print(f"Sphere Dimensions:\n\nRadius: {radius}\nDiameter: {diameter}\nCircumference: {circumference}\nSurface Area: {surface_area}\nVolume: {volume}")