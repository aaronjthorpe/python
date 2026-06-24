#Exercise 5
#5.py
#Area of a triangle

base_length = input("Type the length of the base of the triangle: ")
height = input("Type the height of the triangle: ")

#input always produces a string, so data must be converted
area = 0.5 * float(base_length) * float(height)
print(f"The area of the triangle is: {area}.")

#or
print(f"The area of the triangle is {0.5 * float(base_length) * float(height)}.")

#or
print("The area of the triangle is",area,".") # This syntax will put a space inbetween the number and full-stop at the end.