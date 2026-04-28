my_string = "Hello, world!!"
fruits = ['apple','banana','cherry']

my_list = list(my_string) # Convert a string to list separates each char into its own list item
print(my_list)

#my_new_string = ''.join(my_list) # Join will take list items and combine them into a single string
my_new_string = '**'.join(my_list) # The string used with join (e.g. '**' will be inserted inbetween each joined list item)
print(my_new_string)

print("All of the fruits are:",', '.join(fruits)) # here we put a comma and space in between list items
