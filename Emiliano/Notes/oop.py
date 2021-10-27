#Lesson Outline and Goals
#What are the attributes and methodes
#Whatis a porcedural vs. OOP

#inhertiance_example.py
# class Animal():
#     def __init__(self, name, species, food, movement):
#         self.name = name
#         self.species = species
#         self.food = food
#         self.movement = movement
#     def describe(self): #method is a function that belongs to a class
#         print(f"{self.name} the {self.species}")

#inherited class
# class Cat(Animal):
#     pass
# class Bird(Animal):
#     pass

#     animal1 = Animal('Max', 'cat', 'fish', 'walks')
#     print(animal1.describe()) # object.attribute
#     animal2 = ('Fritz', 'cat', 'fish', 'walks')
#     print(animal2.describe())
#     animal3 = ('Polly', 'parrot', 'seeds', )

#classes are executable statements. It doesn't do anything untiil it is called()/run
#pass is a place holder

# OOP allows us to wrap up data and functioanlity into a what is called an object> Objects are created from a blueprint
# called a class and classes dictate data and functionality that the object would contain. 
# 
#procedural programming is taking lots of logic and putting them inside functions to manipulate data.
#twitter profile dictionary
emiliano = {
'name' : 'Emiliano',
'bio' : 'Student at Columbia',
'tweets' : [] #empty array
} 

def add_tweet(user, text):
    user['tweets'].append(text) #this adds a tweet to the empty array using the user and text parameters. 

    add_tweet(emiliano, 'OOP is awesome!') #we're calling the add_tweet function by calling emiliano's dictionary and 
    print(emiliano['tweets'][0])           #appending 'OOP is awesome! into the tweets : [] empty array in the [0] index'


# initialization function sets the attributes of the persons class. Self refers back to the 
# class. Self referes to the object that will be created from the class blueprint. This is 
# called instatiating a class.


class Person():
    def __init__ (self, name, age): 
        self.name = str(name) 
        self.age = int (age)

# Adding methods and functions to manipulate data within the class, with this specific syntax
    def greeting (self):
        return f'Hello my name is {self.name} and I am {self.age} years of age'

person = Person("Emiliano", 44) 
print(person.name)
print(person.greeting())

person_2 = Person("Clair", 22)
print(person_2.name) 
print(person_2.greeting())    #calling the method

# Python allows to check the type of classes. 
# print(person)
# print(type(person))
# print(type(person) == Person)




#creating a new class

class Cart():
    def __init__(self):
        self.items = [] #will store a lid=st of dictionaries

    def add(self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)

#Adding loop into a class
#finding a total method 

    def total(self):
        cart_total = 0
        for item in self.items:
            cart_total += item['price']
        return f"${cart.total}"


cart = Cart()
cart.add('Oreos',12)
cart.add('pasta', 5)
cart.add('oranges', 5)
print(cart.items)
print(cart.total())




                           