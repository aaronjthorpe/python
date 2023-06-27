import os

fileName = "demoSecond.txt"

   
firstLine = "This is a line of text."
secondLine = "A second line of text."
#thirdLine = input("What should the third line of text be?  ")


f = open(fileName,"a")  # append mode

f.write(firstLine)
f.write("\n")
f.write(secondLine)
f.write("\n")
#f.write(thirdLine)

f.close()

