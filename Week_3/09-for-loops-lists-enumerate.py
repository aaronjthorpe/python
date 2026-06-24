# We can iterate through a list using a for loop.
fruits = ['apple','banana','cherry','date','elderberry']

for fruit in fruits:  # remember with a for loop, the first variable is created here and represents the current loop, the second is an iterable.
    print(fruit.upper())
    if fruit in ['apple','cherry']:  # alternative: if fruit == 'apple' or if fruit == 'red':
        print("That fruit is red!")
    print("-----")


# There is a function called enumerate() which can be used to create a value representing the index of an itme in the list
# when using enumerate, there are two variables used to represent the current loop
# the first is the index, the second is the value.

for i, fruit in enumerate(fruits):
    print(f"index: {i} value: {fruit}")
print("--------------------------")

# By default, enumerate() starts counting the index at 0, which aligns with the list index.
# Sometimes though, we'd prefer to start counting at 1.  We can do this in two ways:
# a) We can use an expression to manipulate the value created by enumerate, or
# b) We can use the 'start' argument for the enumarate function.

# a
for i, fruit in enumerate(fruits):
    print(f"index: {i + 1} value: {fruit}")
print("--------------------------")
# b
for i, fruit in enumerate(fruits, start=1):
    print(f"index: {i} value: {fruit}")


