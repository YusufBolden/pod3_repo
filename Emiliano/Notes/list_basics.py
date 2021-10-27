#grocery_list = ['apple', 'pasta', 'milk']
#print(grocery_list)

#integer_list = [-1, 0, 1]
#float_list = [1, 74, 99, 99, -0.23]
#boolean_list=[True, False]

#***********CLASS LECTURE***********

#apples = 'apples' #data type
#print(apples)

buyers = ['Emiliano', 'Johnathan', 'Yousef', 'Paola',]

groceries = ['milk','brocolli', 'chips', 'sauce', 'burgers', 'onions', 'beer', 'water']
print(groceries)
print(type(groceries))

groceries.append('buns')

groceries.remove('onions')
print(groceries)

num_buyers = 4 

#**************Len**************
num_groceries = len(groceries)

num_per_person= int(num_groceries / num_buyers)

print(num_per_person)

print(groceries[0:num_per_person])

print(groceries[num_per_person:num_groceries])
print(groceries)

print(groceries[3])
