"""
Read files demo
Aaron Thorpe 24/5/23
Three methods for reading data from files.  f.read(),  f.readline(),  f.readlines()
"""


"""f.read() -  Reads whole file into one string
"""
filename = "read_files_demo.txt"

f = open(filename, "r")   # open file in read mode.  logical access via f
data = f.read()           # read ALL file data and store in variable named data (str)
print(data)               # print data
f.close()                 # don't forget to close the file!!



"""f.readline() - Reads one line into one string. Keeps track of position.
				  Run again to get next line.
				  Returns empty string ("") at end of file.
"""
filename = "read_files_demo.txt"

f = open(filename, "r")   # open file in read mode.  logical access via f
data = f.readline()       # read one line from file and store in variable named data (str)
print(data)               # print read data
data = f.readline()       # read next line of file data. note how readline keeps track of position
print(data)               # print read data
f.close()                 # don't forget to close the file!!


# another example using lines of data to build a new string
filename = 'basketball_score.txt'  
f = open(filename, "r")
playerName = f.readline().strip()  # first line of file contains player name.  .strip() removes "\n"
playerScore = f.readline()         # second line of file contains player score.
f.close()                          # now that we have retrieved data we can close file.
print("The basketball player",playerName,"got a score of",playerScore)   # build new string.


#alternative
"""f.readlines() - reads whole file into list
				   each line is separate string as list entry
				   eg. myList = f.readlines()
                       myList[0] = contents of line 1
				       myList[1] = contents of line 2
"""

filename = 'basketball_score.txt'
f = open(filename, "r")             # open file in read mode.  logical access via f
filedata = f.readlines()            # read whole file into filedata (list).  Each index contains 1 line.
f.close()                           # close file because we have data
playerName = filedata[0].strip()    # save list position 1 to playerName.  strip "\n"
playerScore = filedata[1]           # save list position 2 to playerScore.  Because last line in file no need to strip.
print("The basketball player",playerName,"got a score of",playerScore)   # generate new string for output.