# A set is a collection of unique values
# A set eliminates duplicates.  They will not produce an error, they will just be ignored.
# Sets do not keep track of index poistion; they are unordered.

fruits = {'apple','apple','banana','cherry','date','banana'}
print(fruits) # {'apple', 'cherry', 'banana', 'date'} order is random.

# fruits[0]  # this would produce an error.

# To create an empty set, you must use the set() function.  This is to distinguish from dictionaries {}
new_set = set()
print(new_set)  # set()
# Fruits can be added to update method.  Duplicates will be ignored.
fruits.update({'apple','orange'})
print((fruits)) # {'date', 'orange', 'cherry', 'apple', 'banana'} order is random

# The union method can join sets together, eliminating duplicates
set_1 = {'a','b','c'}
set_2 = {'c','d','e','f',1,2,3}  # Sets can contain multiple data types
combo = set_1.union(set_2)
print(combo) # {1, 2, 3, 'f', 'e', 'a', 'c', 'b', 'd'} order is random

# There are lots of other methods for sets including subset, superset, intersection, and difference
# That can be used to compare sets.  (Imagine a venn diagram and trying to determine which values appear in which segment)

# You can iterate through a set the same way as you can a list.
# Note that because a set is not ordered, the sequence will be different every time.  So enumerate() may be unuseful or even misleading!
print("----------")
for index, item in enumerate(set_2):
    print(index, item)
print("----------")