# A recap of Week 2.
# A 'while' loop driven by a counter variable.  While loops run so long as the condition remains True.
# 'if' conditional to ask user if they wish to continue.
# 'break' will exit from loop

import time  # import time module so that we can 'sleep' the program between loops


counter = 5  # set counter

while counter > 0: # So long as counter value is more than 0, indented code will run
    print(counter, "Hello")
    time.sleep(1)
    counter -= 1 # must adjust counter value or it will stay at initial value and loop will be infinite.
    answer = input("Do you want to keep looping?")
    if answer == 'No' or answer == 'no': # we could also use, e.g. answer.lower() == 'no'
        break # exit loop but continue running program.  Could use quit() but that will exit Python and no further code will run.
    else:
        print("Okay, going around again...")

print("Loop is finished") # This line will run after all loops are completed.
    