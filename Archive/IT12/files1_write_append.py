file_name = input("What do you want the file to be called???   ")

fruits = ['apple','banana','cherry','dragonfruit','elderberry']

lines_of_text = ['This is the first line\n','This is the second line\n','This is the third line\n']

import datetime   #This is not in such a good position.  Imports should always be at the top.
now = datetime.datetime.now().strftime("%dst of %B, %Y at %H:%M:%S")

#file_name = 'C:\\users\\aaronthorpe\\file9.txt'

# File Handler  w = write,  a = append
with open(file_name,"w") as f:
    f.write("I'm writing data to a file.") # f.write will write individual strings
    f.write("\n")
    f.write(now)  # Can use variable
    f.write("\n")
    f.writelines(lines_of_text) # Write list entries as lines in a file
    f.writelines(fruit + '\n' for fruit in fruits) # Can use for loop to manipulate list items (e.g. add '\n')

print("Finished!!!")
