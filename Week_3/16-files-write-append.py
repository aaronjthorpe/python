# In write mode, files will be created if the don't exist.
# If the file does exist it will be OVERWRITTEN - It's contents will be destroyed and the file will be cleared.  CAUTION.

with open('file2.txt','w') as f:
    f.write("This will write some text to the file.")
    f.write("The cursor will keep track of position so long as the file is open.")
    f.write("Because I have not included any backslash-n characters, this text will all appear on one line.")

with open("file2.txt","r") as f: # reopen file in read mode to print contents
    print(f.read())

with open("file2.txt","w") as f:
    f.write("If I open the same file again in write mode\n")
    f.write("All previous content will be destroyed.  'Whoops!'")

with open("file2.txt","r") as f: # reopen file in read mode to print contents
    print(f.read())


# In append mode, a file will be created if it doesn't exist.
# If the file does exist, the 'cursor' will be opened at the bottem of the file and write operations will add to the bottom (append) the file.
with open('file3.txt','a') as file: # decided to use a different variable name because 'why not?'
    file.write("Adding some content\nTo the file.")
    file.write("\n______________________________")  # probably want another \n at the end of this string

with open("file3.txt","r") as file: # reopen file in read mode to print contents
    print(file.read())

with open('file3.txt','a') as file: # Reopening the file in append mode.  Note that we must be careful with position of \n
    file.write("Note that because we did not have a backslash-n at the end of the last line (code line 24), this will be added to the line with the --------\nAdd some additional content.")
    file.write("\n______________________________")

with open("file3.txt","r") as file: # reopen file in read mode to print contents
    print(file.read())