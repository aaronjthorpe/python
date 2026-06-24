number = int(input("Tell me a number:  "))

print("Checking the number....")
if number == 10:    # if tests an expression and if True, will run the indented code
    print("The number is exactly 10!!!")
elif number > 10:   # elif only runs if the previous if or elif was False.  If expression is true, run the indented code
    print("That's bigger than 10")
elif number >=5 :
    print("The number is between 5 and 10")
elif number >=3:
    print("The number is between 3 and 5")
else:   # else only runs if all previous if and elif(s) are False
    print("That's smaller than 3.")