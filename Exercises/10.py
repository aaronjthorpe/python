#Exercise 10
#10.py
#Functions

#Option 1
def area_of_rectangle(length,height):
    area = float(length) * float(height)
    print(f"The area of the rectangle is: {area}.")

#We can ask the user for inputs before calling the function (lines 12-15)
#Or, Just call the function with existing values (line 18)
user_length = input("What is the length of the rectangle? ")
user_height = input("What is the height of the rectangle? ")
print("Using inputted values: ",end='')   # end='' means that no new line will be created after the print function runs.
area_of_rectangle(user_length,user_height)

print("Using values passed directly to function: ",end='')
area_of_rectangle(5,5)

#triangle
def area_of_triangle(base_length,height):
    area = 0.5 * float(base_length) * float(height)
    print(f"The area of the triangle is: {area}.")

area_of_triangle(1,1)
area_of_triangle(7,12)

#Option 2
#Using 'print' in a function is generally a bad idea as we can't guarantee 
#that the 'caller' of the function will have access to the terminal
#'return' will pass a value back to the caller, who can then do what they
#want with that value, including - but not limited to - printing it.

def area_of_rectangle_2(length,height):
    return length * height

# This will produce no output as the function uses return not print
area_of_rectangle_2(5,5) 

# However, we can capture the returned output and then use it for... whatever
my_area = area_of_rectangle_2(10,10)
print(my_area)
#or all in one line
print(area_of_rectangle_2(10,10))

#If we use the first option again, but try to save that into a variable you will see the variable contains nothing (Data type: None)
another_area = area_of_rectangle(9,9)
print(another_area)

#Triangle
def area_of_triangle_2(base_length,height):
    return 0.5 * float(base_length) * float(height)

print(area_of_triangle_2(7,3))
user_base = input("What is the base of a triangle: ")
user_height = input("What is the height of a triangle: ")
user_area = area_of_triangle_2(user_base,user_height)
print(user_area)

#Option 3 - another file
from functions_exercise_10 import area_of_triangle as area_t,area_of_rectangle as area_r  #etc...  Aliases (e.g. 'as area_r') are optional but without them we would overwrite functions already defined in this file...
#or import functions_exercise_10

area_t(5,5)
area_r(100,100)





