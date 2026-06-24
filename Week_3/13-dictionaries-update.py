user_emails = {
    'Homer':'homer@snpp.net',
    'Bob':'broberts@internet.com',
    'Sarah':'sarah@gmail.com'
    }

# To update a dictionary, you can use direct assignment:
user_emails['Bob'] = 'bob@newemail.com'

# If the specified key does not currently exist, it will be added to the dictionary, flexible but dangerous (typos etc.)
user_emails['Aaron'] = 'aaron.thorpe@academyit.edu.au'

print(user_emails)

# We can use the update() method.  # Update supports quite a few different processes
# Easiest is to use a dictionary
user_emails.update({'Sarah':'sarah@outlook.com','Jen':'jenny123@abc.com'})
print(user_emails) # {'Homer': 'homer@snpp.net', 'Bob': 'bob@newemail.com', 'Sarah': 'sarah@outlook.com', 'Aaron': 'aaron.thorpe@academyit.edu.au', 'Jen': 'jenny123@abc.com'}
# Sarah's e-mail address is updated, and Jen's is added.  Two-for-one!

# You can build a new dictionary from a list using the fromkeys() method.
# Each dictionary item will have a value of None.
list_of_users = ['Fred','Sally','James']
new_dict = dict().fromkeys(list_of_users)
print(new_dict) # {'Fred': None, 'Sally': None, 'James': None}