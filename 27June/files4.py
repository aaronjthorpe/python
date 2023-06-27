#Read contents of entire file as single string

fileName = "fruits.txt"

f = open(fileName, "r")

fileContents = f.read()

f.close()


print(fileContents)
print(type(fileContents))