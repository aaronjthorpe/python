#This program opens the file and then uses a for loop with readlines() to
#iterate through each line in the file and print the output.
#It uses a counter to keep track of line number.
#strip() is used to remove "\n" from end of lines.

fileName = "fruits.txt"

f = open(fileName, "r")

counter = 1

for line in f.readlines():
    print("The contents of line " + str(counter) + " is " + line.strip())
    counter += 1

f.close()



