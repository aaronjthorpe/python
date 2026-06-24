# A tuple is an ordered iterable similar to a list
# However a tuple is not mutable; once it is created and its value set it cannot be changed.

#to create an empty tuple
my_tuple = ()  # but this would be quite pointless because you cannot then change its value

adelaide_coordinates = (-34.9287,138.5986)
print(adelaide_coordinates)

# a tuple has only a few methods
print(adelaide_coordinates.index(138.5986))  # returns 1, that number is in index position 1.

# a tuple can contain duplicates and different data types
fruits = ('apple','banana','cherry','apple','apple','orange')
random_stuff = (123,True,'apple',(1,2,3),['a','b','c'])

print(fruits[-1])  # 'apple'
print(fruits[0:3])  # ('apple','banana','cherry')

#The count method will count the number of instances of a value
print(fruits.count('apple'))  # 3


# tuples are immutable
# fruits[0] = 'apricot'  # This would produce an error.

# You can iterate through a tuple the same way as you can a list.
for index, fruit in enumerate(fruits):
    print(index, fruit)




