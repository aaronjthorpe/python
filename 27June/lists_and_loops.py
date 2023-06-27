import os

counter = 1

while counter <= 5:
    print("Hello")
    counter += 1

print("Loop complete")


endpoint = int(input("how many loops?   "))

for i in range(1,endpoint + 1):
    print ("Loop" + str(i))



myList = ['apple','banana','grape','orange','anotherone','yetanotherfruit']

for anythingyoulike in myList:
    print(anythingyoulike)
    print("loop again")



if os.path.exists('C:\\hello.py'):
    print("the file exists")
else:
    print("the file does not exist!")


