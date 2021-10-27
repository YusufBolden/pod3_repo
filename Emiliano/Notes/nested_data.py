# cart = {
#     'friuts': ['mangos', 'apples', 'pears', 'aapples',],
#     'vegtables':['spinich', 'peas'],
#     'total_price' : 23.21
# }

# print(cart)

# print(type(cart))

# print(type(cart['vegatables']))

#******************Lecture Nesting Data*************************
# Talking about lists and dictionaries
#Data inside other data
#For example a dictionary inside another dictionary, 
# lists inside dictionarys
#lists inside lists
#dictionary inside a list inside a dictionary

#HOW TO GET ? UPDATE INFORMATTION within nested data structures

#Best practices: depends on what kind of data 
#Shopping cart with lists insode a dictionary

#cart is the disctionary
cart = {
    #cleaning products is the list
    'cleaning_products':['soap', 'broom']
}

print(cart)
print(cart['cleaning_prducts'])

print(type('cleaning_products')
print(cart)

cart['cleaning_products'].append('mop')
cart['cleaning_products'].append('lysol')

#adding a new list as a value in a dictionary
cart['tooth_care'] = ['toothbrush', 'floss', 'mouthwash']

#remove floss .pop is to remove from a dictionary. .remove to remove items from a list
cart['tooth_care'].remove('floss')
cart.pop('cleaning_products')

print(type(cart['tooth_care']))

cart['home_imporvement'] = {'shovel':27.99, 'duct_tape': 2.17, 'paint': 17.43}

print(cart)
#The difference between dic and list. 
# 
# List is ORDERED -- index 
print(type(cart['tooth_care'])) #Indexed
print(['tooth_care'][1]) #Keyed
#  DIC is not ORDERED --- key
print(type(cart['home_improvement']))
print(cart['home_improvement']['paint'])

cart['total_price'] = 29.99

print(cart)

a = [] #List 
b = {} #Dictionary

#another level of nesting
cart['tooth_care'].append{'floss': 2.39}

