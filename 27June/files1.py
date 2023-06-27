#import os

fileName = "demofirst.txt"

firstLine = "This is a line of text."
secondLine = "A second line of text."
#thirdLine = input("What should the third line of text be?  ")


f = open(fileName,"w")

f.write(firstLine)
f.write("\n")
#f.write(secondLine)
#f.write("\n")
#f.write(thirdLine)

f.close()




