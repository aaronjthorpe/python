#Exercise 4
#4.py
#Area of a rectangle/square

length = input("Type the length of the rectangle: ")
height = input("Type the height of the rectangle: ")

#input always produces a string, so data must be converted
area = float(length) * float(height)
print(f"The area of the rectangle is: {area}.")

#or
print(f"The area of the rectangle is {float(length) * float(height)}.")

#or
print("The area of the rectangle is",area,".") # This syntax will put a space inbetween the number and full-stop at the end.