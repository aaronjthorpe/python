file_name = "file1.txt"

#File handler - "r" = read
with open(file_name, "r") as f:
    #file_contents = f.read() # Read method will read whole file contents into one string
    #file_contents = f.read().splitlines() # Splitlines will create a list separated by '\n' character
    #file_contents = f.readlines() # Sames as .read().splitlines() 'two for one!'
    file_contents = f.readline()   # Readline reads one line at a time, remembers position so long as file is open
    print(f"The first line is {file_contents}")
    file_contents = f.readline()
    print(f"This should now be the second line: {file_contents}")

with open(file_name) as f:
    print(f.readline()) # Because we've closed and re-opened the file, we're now back to line 1 again


print("Finished")


with open(file_name, "r") as f:
    file_contents = f.readline(-1) # Read method will read whole file contents into one string

print(f"File contents: {file_contents}")
print("Finished")