# We can test if an item is in an iterable using the 'in' operator.

fruits = ['apple','banana','cherry','date','elderberry']

print('apple' in fruits)  # True
print('orange' in fruits)  # False

# We can use this in a conditional
selection = 'orange'
if selection in fruits:
    print(f"Yes, we have {selection}.  You can have that.")
else:
    print(f"Sorry, no.  Out of stock of {selection}.")


# To look up the first position an item appears in a list, we can use the index() function
print(fruits.index('cherry'))  # returns 2

# This method cannot handle values that are not in the list.  We would need try/except.
# print(fruits.index('orange'))  # produces a ValueError
try:
    print(fruits.index('orange'))
except ValueError:
    print("Not in the list.")


# If an item appears in the list multiple times, index() will only return the first position.
# You would need to iterate through the list with for to collect each position.
more_fruits = ['apple','banana','apple','apple','cherry']
print(more_fruits.index('apple')) # returns 0, despite apple also appearing at 2 and 3.