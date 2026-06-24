# To work with plain text files in Python we can use the 'with open' file handler.
# We must specify:
#   - A file path (as a string).  If the file does not exist, an error will be produced.
#   - A mode (read, write, append) (as a string)
#   - A variable to use to reference the file for operations
# The file will remain open during the indented code block.  When the indentation ends, the file handler will automatically close the file.

# read() will read the entire contents of the file as a single string.
with open("file1.txt","r") as f:  # opens file1.txt in read mode and can be referenced by variable f
    file_text = f.read()

print(file_text)

# readlines() will read the whole text file and create a list with a separate item for each line
with open("file1.txt","r") as f:  # opens file1.txt in read mode and can be referenced by variable f
    file_text = f.readlines()

print(file_text) # ['This is a file\n', 'That has three very exciting\n', 'lines of text in it']
# Note that the above includes the new line character \n in each list item.
# We can remove with strip() method.
clean_file_text = []
for line in file_text:
    clean_file_text.append(line.strip())
print(clean_file_text) # ['This is a file', 'That has three very exciting', 'lines of text in it']

# We can access individual lines like we could any list
print(file_text[0]) # This is a file (prints extra new line because it still has \n)

print(file_text[0].strip()) # As above but with no extra blank line


# Last (and also probably least), we can read an individual line with readline()
# Python will remember the cursor position as long as the file remains open

with open('file1.txt','r') as f:
    line1 = f.readline() # will start at beginning of file and read one line, will leave 'cursor' at end of line
    print("First line:",line1.strip())
    f.readline()
    line3 = f.readline()
    print("I deliberately ignored the second line.  We ran f.readline() to run over it and move the 'cursor' but didn't save the data.")
    print("Third line:",line3)

# We can test for the existance of a file with the os module.
import os
if os.path.exists("fake file.txt"):
    print("The file exists, we can do with open()..... etc. here")
else:
    print("Error: File does not exist")