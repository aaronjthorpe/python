#World's Worst Calculator - can only add two numbers together.

#string (str) = 'ordered sequence of characters'
#numbers = integer (int) (whole number) 
#           floating point number (float) - number with decimals (3.14159)
#  1.24564246346378


string = "Hello, world."

#print(string)

def worst_calculator():
    number_1 = int(input("Tell me the first number:  "))
    number_2 = int(input("Tell me the second number:  "))
    print(number_1 - number_2)

def less_worse_calculator(apple,banana):
    print("Addition:      ",apple + banana)
    print("Subtraction:   ",apple - banana)
    print("Multiplaction: ",apple * banana)
    print("Division:      ",apple / banana)

try:
    number_1 = input("Tell me the first number:  ")
    number_1 = int(number_1)
except ValueError:
    print("That's not a number, you doofus!!")
    print("So I'm setting the number to be 0.")
    number_1 = 0

try:
    number_2 = input("Tell me the first number:  ")
    number_2 = int(number_2)
except:
    print("That's not a number, you doofus!!")
    print("So I'm setting the number to be 0.")
    number_2 = 0

try:
    less_worse_calculator(number_1,number_2)
except ZeroDivisionError:
    print("The second number can't be zero.")
#less_worse_calculator(10,20)
#less_worse_calculator(4,5)
#less_worse_calculator(15,0)
