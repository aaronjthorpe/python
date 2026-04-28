import datetime
import time

# While loop with an artificial counter
counter = 5   #counter is created and starts at 5
while counter > 0:  #loop will continue while counter is greater than 0
    print(counter, "Hello - counting down!")
    time.sleep(0.5)
    counter -= 1   # counter decrements by 1 each loop

print("Finished loop!")
time.sleep(3) #wait three seconds

#Same as above but incrementing instead of decrementing.  Stop when counter hits 5.
counter = 0  
while counter < 5:
    print(counter, "Hello - counting up!")
    time.sleep(0.5)
    counter += 1
print("Finished loop!")
time.sleep(3) #wait three seconds


counter = 0
while True: # while True will run forever (infinite loop) unless we break
    print(counter, 'Hello.  The time is:', datetime.datetime.now().strftime("%H:%M:%S.%f"))
    time.sleep(0.5)
    counter = counter + 1  # Counter is not used to control loop here, just literally to count how many loops have occurred.
    #counter += 1  #This does the same as line above, but in shorthand
    if datetime.datetime.now().strftime("%H") > '10': #Stop at 11:00 - a bit dodgy, but it works!
        print("It's after 11 O'Clock.  Ending loop.")
        break