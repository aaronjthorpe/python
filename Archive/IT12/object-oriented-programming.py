# Object Oriented Programming (OOP)
# Objects can have attributes (properties), methods (something they can do)
# Objects are instances of a 'class'
# A class is a type of thing e.g. Class = Person, Object = Aaron
# Classes can be derived from other class.  e.g. teacher and student classes can be derived from person.  Derived or 'child' classes can inherit properties from their 'parent'.  E.g. all Person object have a name, but Student objects can have a StudentID attribute and Teacher objects can have an EmployeeID attribute

# A very simple example of a custom class for a Dog object.

class Dog:
    legs = 4 # variables defined here will be attributes shared by all objects in the class
    
    def __init__(self,breed,colour,name):  # the init function is run when a new instance of the class is created. It sets attributes for that specific instance/object
        self.breed = breed
        self.colour = colour
        self.name = name
    
    def bark(self):  # a function within the class is a method.  the self parameter references the specifc object of the class
        print(f"{self.name} said 'Woof!'")

my_dog = Dog(breed='Boston Terrier',colour='Black',name='Bob')  # my_dog is an instance of class dog

my_dog.bark() #run bark method.  The specifc object my_dog will be passed into the self parameter of the function

#Access attributes using syntax object.attribute
print(my_dog.name)
print(my_dog.breed)
#Print a sentence making use of attributes (f-string)
print(f"{my_dog.name} is a {my_dog.__class__.__name__}. {my_dog.name} has {my_dog.legs} legs and is {my_dog.colour}. \
{my_dog.name} is a {my_dog.breed}.")

#Attribute values can be changed
old_name = my_dog.name
my_dog.name = 'Larry'
print(f"{old_name}'s name changed to {my_dog.name}.")