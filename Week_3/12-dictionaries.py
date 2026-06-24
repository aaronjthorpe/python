# A dictionary is a collection of key/value pairs.  In Python the data type is dict.
# A key is the information that you can use to look up the matching value
# To use the metaphor: if we look up a word in the English dictionary, we find the definition of that word.
# If we had a dictionary containing a collection of users, we could look up e.g. their e-mail address.
# If we had a dictionary of products, we could look up their price.

# Keys are used as the 'index' of the dictionary.

# Keys must be unique in a dictionary, but values can repeat.


# One challenge with dictionaries is that it is always 1 key -> 1 value.
# If we want to store multiple values, we can either use nested dictionaries, a dictionary where the value is a list, or we might need to use an external database.

# To create a new empty dictionary
empty_dict = {}

# Dictionaries are delimited with {}  Keys and Values are separated by :  Each item is separated by a comma
user_emails = {'Homer':'homer@snpp.net','Bob':'broberts@internet.com','Sarah':'sarah@gmail.com'}

# You can lay out a dictionary across multiple lines so long, but this is purely for aesthetics and legibility; personal preference
fruits = {
    "Apple" : 2.50,
    "Banana" : 1.99,
    "Cherry" : 10.00
}

print(fruits)

# There are several methods to access items in a dictionary.
# items() creates a dict_items object, which is *effectively* a list containing a tuple of each key and value
print(fruits.items())  # dict_items([('Apple', 2.5), ('Banana', 1.99), ('Cherry', 10.0)])

# keys() creates a dict_keys object, which is *effectively* a list of keys from the dict.
print(fruits.keys()) # dict_keys(['Apple', 'Banana', 'Cherry'])

# values() similar to keys(), creates a dict_values object, which is *effectively* a list of values from the dict.  
print(fruits.values()) # dict_values([2.5, 1.99, 10.0])

# To access an individual item, you can use its key.
print(fruits['Banana'])  #  1.99 (as float)

# This will produce an error if the key does not exist.
# print(fruits[1]) # Produces a KeyError because key index does not exist; can't use index the same as a list
# print(fruits['orange']) # Same error.  You can handle this with try/except or.....

# A 'safer' modern alternative is to use the get() method
print(fruits.get('Apple')) #  2.5 (as float)
print(fruits.get('orange')) # None (no result, but no error either)

# To iterate through items in dict, can use for loop in a couple of different ways
for key, value in fruits.items():
    print(f"The key is: {key}  |  The value is: {value}")

# The default if you only specify one iterator is keys
for keys in fruits:   # could also use for keys in fruits.keys(): to be explicit
    print(keys)  # Apple, banana, cherry (as separate strings)

# Despite the naming of the variable, this still produces keys.
for values in fruits:
    print(values) # Does not work as intended.

# To iterate over values only, use the values() method
for value in fruits.values():
    print(value)  #(2.5, 1.99, 10.0 as separate floats)

# We can test for the presence of an item with in
# Prints yes
if 'Cherry' in fruits:
    print('yes')

# Prints no
if 'Orange' in fruits:
    print('yes')
else:
    print('no')

# We can test values, too:
if 10 in fruits.values():
    print('Yes 10 is there')
    # This prints "Yes" even though the dict actually contains 10.0