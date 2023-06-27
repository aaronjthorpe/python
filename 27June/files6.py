#Read contents of entire file as a list

fileName = "fruits.txt"

f = open(fileName, "r")

fileContents = f.readline()
print(fileContents.strip())

print("First line read")

fileContents = f.readline()
print(fileContents.strip())

print("Second line read")

fileContents = f.readline()
print(fileContents.strip())


f.close()



print(type(fileContents))