my_list = [0.3,3,5,1,-5123]
print(my_list)
my_list.sort() # sort will sort a list in memory
print(my_list)

#enumerate() is a function that will generate an int for the index (position) of the item in the list
for i,item in enumerate(my_list):
    print(f"The item at position {i + 1} in the list is {item}")

my_list = ['apple','banana','cherry']
print(my_list[1])
my_list.remove('banana') # remove an item from the list
print(my_list[1])
my_list.append('dragonfruit')

string = 'Hello, world! How are you today?'
for character in string:  # a string is kind of like a list of characters.  It is iterable.
    print(character.upper())

long_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#we can print specific items by specifying the index
print(long_list[0]) #first item
print(long_list[1]) #second item
print(long_list[-1]) #last item
print(long_list[1:4]) #from second item (index 1) to just before fifth item (index 4)
print(long_list[0:10:2]) #from first item (index 0) to just before 11th item (index 10), but only every 2nd item
print(long_list[5:]) #from index 5 to the end of the list
print(long_list[:11]) #from the start of the list to just before index 11
print(long_list[::-1]) #print the whole list with an interval of -1.  Prints the list backwards
