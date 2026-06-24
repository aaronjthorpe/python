fruits = ['apple','banana','cherry','date','elderberry']

# We can add to a list with append().  Append only supports 1 value at a time.
fruits.append('fig')
print(fruits)

# If you have a list (or other iterable) you can add it to a list with extend.
fruits.extend(['grape','honeydew'])
print(fruits)

# You can insert a value at a specific index.
fruits.insert(3,'dragonfruit')
print(fruits) # dragonfruit is inserted at index 3.  The current index 3 (date) is pushed to index 4.

# You can remove an item from a list with remove()
fruits.remove('date')
print(fruits)

# Remove produces no usable output.  The item is simply removed from the list.
deleted = fruits.remove('elderberry')
print(fruits)
print(deleted)  # deleted contains 'None'

# Pop allows you to 'pop an item off' the list.  Removing it, but also allowing the value to be saved.
# Pop requires the index, not the value.
deleted = fruits.pop(4)  # pop index 4 which should be 'fig' based on previous code ran.
print(fruits) # fig should be removed.
print(deleted) # deleted will contain 'fig'.  The 'popped' value is preserved if we save it to a variable.
deleted2 = fruits.pop() # the default is the last entry.
print(deleted2) # 'honeydew'


# You can remove all items from a list with clear()
fruits.clear()
print(fruits)  # []