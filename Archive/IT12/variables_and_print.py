first = 'Aaron'
last = 'Thorpe'

print(first,last)

#expression (formula)
print(first + ' ' + last)

#f-strings (formatted) allow a blend of expressions inside {} and text
print(f"{first}##1324524u*^4w685{last}")
print(f"First Name: {first}")
print(f"Last Name: {last}")


#Adjust which quotation marks are used depending on content of strings.
print('Aaron said "Hello"')  #double quote in string, so use single quote to delimit.
print("It's a nice day today (I love winter)")  #single quote (apostrophe) in string, so use double quote to delimit.
print('''Aaron said "It's a nice day today"''')  #both single and double quotes in string, so triple quote to delimit.
