# This one gets a bit messy, but we can nest dictionaries, either with lists or more dictionaries

# Example 1, with list.
# Each user has their name for a key.
# The value is then a list containing 3 values each: [e-mail, username, password]
# So long as we maintain that sequence, we can store 3 values for each user.  Risk of user error, e.g. putting ['username','password','e-mail']

users = {
    'Aaron':['aaron@academyit.com.au','AARONT','Pa$$w0rd'],
    'Homer':['homer@snpp.net','HOMERS','12345'],
    'Gabe':['gaben@valve.com','GABEN','H@lfL!f3']
}

# To access someone's username (e.g.)
print(users['Homer'][1])

# To access all the info for all users we use a nested loop.
# The first loop gets the key and the value (the values are lists)
# The second loop iterates over the list and retrieves the individual items (e-mail, username, password)
for key, value in users.items():
    for item in value: # Note the 'in' here is the value from the outer loop in the line above
        print(f"Key: {key} Value: {item}")

# A variation on the above where we can keep track of the index of each item in the list
for key, value in users.items():
    for index, item in enumerate(value):
        print(f"Key: {key} Value {index}: {item}")

# One last variation where we can test the index value because we might be interested in only a particular value
for key, value in users.items():
    print(f"User: {key}") # Only runs once per key.
    for index, item in enumerate(value):
        if index == 0:
            print(f"    E-mail Address: {item}")
        elif index == 1:
            print(f"    Username: {item}")
        else:
            print(f"    Password: {item}")
    print("------------------------------------------")
# There are many more variations that you could do.


# Example 2, with nested dictionary.
# Each fruit is given a number for its key.
# The value is then a dictionary containing The name of the fruit and its price.

fruits = {
    1: {"Apple" : 2.50},
    2: {"Banana" : 1.99},
    3: {"Cherry" : 10.00}
}

# Access the price of a single fruit
print(fruits.get(2).values())
# The above is highlighted red in the editor because it doesn't know if the value of fruits.get(2) will be 2 or if it will be None (if it were a lookup on a key that didn't exist).  A None value does not have a values() method, but a dict_values() does.
# Output will be dict_values([1.99]).  To get the 'raw' value, we'll need to run a second get()  (There are other ways to do this, mostly using a loop):
print(fruits.get(2).get('Banana'))  # Get key 2 from outer dict, then get key 'banana' from inner dict.

# To loop through
for key, value in fruits.items():
    print(f"Key: {key}")
    for key2, value2, in value.items(): # value represents the nested dict.  key2 and value2 are the keys and values of those nested dicts.
        print(f"Inner Key: {key2} | Inner Value {value2}")
        if key2 == 'Cherry':
            print("           Price for Cherries is per box.")
    print("---------------------------")


