fruits = ['apple','banana','cherry','date']

# You can print a list, but it will include the list structure
print(fruits) # displays ['apple', 'banana', 'cherry', 'date']

# To access an item inside a list, place it's index in square brackets.  This will return the 'actual' data type
print(fruits[0])  # displays '  apple  '  a string.
print(fruits[-2]) # displays '  cherry  '

# You can change an item in a list by using it's index and the assignment operator (=)
fruits[0] = 'apricot'
fruits[3] = 'durian'
print(fruits) # ['apricot', 'banana', 'cherry', 'durian']

# lists can be sorted.
numbers = [901,123,656,234,-50,0]
numbers.sort() # the sort method produces no output, but sorts a list in memory.
print(numbers) # the list will now be sorted from smallest to biggest.  You can also sort strings (alphabetical)

numbers.sort(reverse=True) # You can sort the list from biggest to smallest instead with reverse.
print(numbers)


fruit = ['orange','cherry','apple','banana']
fruit.sort()
print(fruit)


mixed_list = ['orange','cherry',50,20]
#mixed_list.sort()  This line would cause an error if uncommented because you can not use < to sort str and int.

mixed_list2 = ['orange','cherry','50','20']
mixed_list2.sort() # this will work because the numbers here are stored as strings.  They will generally appear before letters, but this is OS / 'Code page' dependant.
print(mixed_list2)

#To temporarily sort an iterable for display purposes, but not make persistent changes, you can use the sorted() function
out_of_order = ['xyz','def','lmn','abc']
print(sorted(out_of_order))  # ['abc', 'def', 'lmn', 'xyz']
print(out_of_order) # the list in memory retains it's original order  # ['xyz', 'def', 'lmn', 'abc']
