from math import sqrt

#We are able to store the result of the square root function in the variable answer
#because the sqrt function returns a float value
answer = sqrt(2)
print(answer)

def lame(a,b):
    #print(a + b)
    # print inside the function can be useful for troubleshooting
    # or debugging, but you don't want it in the final function.
    # a function should simply do the work - it is up to the caller to decide
    # if they wish to print the output
    return a + b # return will pass the result of a + b back to the place the function was called.

#def more_work(c): 

#add 1 and 2 using the lame function
lame(1,2) # running lame function by itself will add 1+2 but produce no output while print on line 9 is commented out
result = lame(1,2) # take returned value and store in variable
print(result) # display returned value
print(lame(1,2)) # same output as lines 20+21 combined, but we don't save result for future use.