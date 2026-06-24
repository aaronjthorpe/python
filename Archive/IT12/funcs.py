def boring():
    print(1+1)

def even_more_boring():
    print('abc')


#If you have code that is not contained within a function, it will run
#That code if you import the file.
#Best practice is to put ALL code in a function.
#Code that you wish to run when you run the file should be put in a function called
#main()
#We then use a 'dunder method' (double underscore) to check if we are running the file
#And if we are, call the main() function.

#The bad way - this code will run if this file is imported:
print("This code is here in the funcs file\n\
This code deletes all the files on your hard drive, by the way. (e.g.)")


#The correct way:
# def main():
#     print("This code is here in the funcs file")
#     print("This code deletes all the files on your hard drive, by the way. (e.g.)")
#     print("Now that it's in a main function and we have the dunder method below, this code would only run if the file itself was run directly, i.e. not on import")

# if __name__ == '__main__':
#     main()