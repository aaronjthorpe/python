#Read contents of entire file as a list

fileName = "fruits.txt"

f = open(fileName, "r")

fileContents = f.readlines()

f.close()


print(fileContents)
print(fileContents[0].strip())  #strip removes extra characters eg space and "\n"
print(fileContents[3].strip())
print(type(fileContents))