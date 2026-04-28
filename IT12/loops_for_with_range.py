import math

# a for loop iterates through an iterable such as a list.
# e.g. if I have a list with three items ['a','b','c'] a for loop will run 3 times
# we use the syntax   for x in y:   where x is a variable that represents the current iteration, and y is an iterable such as a list or range
# generally the 'x' can be a made up variable name, the letter i is common
# and the 'y' must be something that exists.

numbers = [112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634,112423,457457,25436,42653764,3463456457,84685634]
#for i in numbers:   OR
#for number in numbers:   OR
for whateverIwantIttoBe in numbers:
    print(whateverIwantIttoBe)
    print(whateverIwantIttoBe / 2)
    print(whateverIwantIttoBe * math.pi)
    print("___________________________")


#the range() function will create a sequence starting at 0 by default and stopping just before the given argument
#e.g. range(5) will create a range from 0 - 4; 5 items.
#range() does not actually create each of those numbers, but understands the sequence and position.  It is extremely useful for loops.
#range() solves the need to create and maintain an artificial counter

loops = int(input("How many loops???  "))

for i in range(loops):
    print(i + 1, 'Hello')  # We add 1 to i because it starts counting at 0, but we might like to start counting at 1
   

#The range function supports up to three arguments.
start_point = 0  #default start_point is 0
end_point = 10   #there is no default end point, this must be specified
interval = 2   #default interval is 1

for i in range(start_point,end_point,interval):
    print(i)

my_range = range(5)

print(my_range)
# A range does not actually create all of the numbers from start point to end point
# It simply knows what the start and end point is, and can run through the range
# efficient for memory