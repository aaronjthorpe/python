"""
Write files demo
Aaron Thorpe 24/5/23
Write data to files,  write mode and append mode
"""


filename = "write_files_demo.txt"

#in our example data to write is stored in variables.
firstText = "This is some text"
secondText = "This is some more text"

f = open(filename,"w")  # write mode (destructive!!)
#f = open(filename,"a")  # append mode

f.write(firstText + "\n")
f.write("\n")
f.write(secondText + "\n")

f.close()