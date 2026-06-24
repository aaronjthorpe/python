#To access a file we need 4 things.
# 1. filename  2. mode ("w"rite, "a"ppend, "r"ead)  3. variable to access file (f).  4.  data.

file_name = 'test.txt'  # 'Relative path' - file will be created in the current folder
# file_name = './data/test.txt'  # 'Relative path' - file will be in subfolder of current folder
# file_name = 'C:/PythonCode/test.txt'  # 'Absolute path' - full path

with open(file_name,"w") as f:  # open file in (over)write (will create if not exist). Access via f
    f.write("Aaron")
    f.write(";")
    f.write("50")
    f.write(";")
    f.write("40")
    f.write(";")
    f.write('80%')
    #This will write 4 pieces of data on one line, separated by semicolons.  We could use \n instead of ; for separate lines.
    #Here the data is hardcoded but could instead be retreived using expression or variable.

with open(file_name,"r") as f: #open file in read mode. Access via f
    data = f.read().split(';')  #read whole contents of file, split on ; Will create list object in data 
    print(data)

print("Done")