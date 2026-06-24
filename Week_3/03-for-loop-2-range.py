"""
We can use a function called range() to create an artificial iterable to loop through.
The range() function creates an object of data type range.
A range has a start point (default 0), exclusive end point (no default, must specifiy), and interval (default 1)
'exclusive end point' means that the range will not include the end point.  e.g. range(5) will include 4 but not include 5.
You could also refer to it as a 'stop before' point.  i.e. range(5) = 'stop before 5'
A range does not actually 'create' all the values between it's start and end (e.g. as ints)
It merely knows it's start and end point and can keep track of it's position.
This can make it very efficient in terms of memory usage; a range from 0 to 5 will use just about
the same amount of memory as a range from 0 to 1000000"""
range(5) # values 0,1,2,3,4
range(10) # values, 0,1,2,3,4,5,6,7,8,9
range(10,15) # two arguments are start and stop-before.  values 10,11,12,13,14
range(1,6) # values 1,2,3,4,5
range(0,10,2) # three arguments are start, stop-before, and interval.  values 0,2,4,6,8

#examples
for iteration in range(5):
    print("This will run 5 times!")

for i in range(0,10,2):
    print(i)

for i in range(100,0,-5):
    print(f"{i} is running backwards by 5 until it gets to zero, because the interval is -5!")

for i in range(-100,-50,3):
    print(f"You can use negative numbers so long as the start, end, and interval are in order.  * {i} *")

#we can use variables and expressions if we want.
start = 1
end = 10
interval = 1
for i in range(start, end + 1, interval): # here I have used 'end + 1' to make sure the number in the variable is included.  If we just used 'end', the range would exclude 10, so would run 1 to 9.  This is valid, but it's all about expectations and assumptions;  what does 'end' mean to the user??
    print(i) 


# a for loop with range() is a common alternative to while loop with counter.
# The below two examples effectively do the same thing!!  A while loop is more manual, but gives more control and perhaps flexibility...
# for loop has minimum of 2 lines including code to loop
# while loop has minimum of 4 lines including code to loop
print("Start of for loop")
for i in range(5):
    print(i)
print("End of for loop")

counter = 0
print("Start of while loop")
while counter < 5:
    print(counter)
    counter += 1
print("End of while loop")