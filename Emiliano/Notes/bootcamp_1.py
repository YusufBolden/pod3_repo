# This is a comment that python ignoresclear
print('Hi, this is your computer speaking')
# This is a second print statement that python will ignore
print('I can run lots of print functions')
#variables are containers for your data. 
firstname = 'Emiliano'
print(firstname)
firstname = 'Paul'
print(firstname)

full_name = 'Emiliano Lopez'
print(full_name)

# Integers 
my_int = 4
print(my_int)

#Floats
my_float =4.0
print(my_float)
print(type(my_float))

#Math with integers / floats
print(my_int + my_float)
print(my_int - my_float)
print(my_int * 100)
print(my_int / 3.2)

#Exponents

my_num = 13**13
print(my_num)

#Follow order of operations

# Type conversion form float to int

my_float2 = 4.68
my_int2 = int(my_float2)
print(my_int2)
print(round(my_float2))

print(float(9))

print(round(my_float2, 5))

'''
What's important about strings? quotes!

QUOTES

"" or ''

strings can have spaces

'''
my_string = 'Hello World!'
my_string2 = "HELLO WORLD!"
print(my_string)
print(type(my_string))
print(my_string2)

my_space_case = '       '
print(my_space_case)
lyrics = 'At first I was afraid, I was petrified, \
    Kept thinking I could never live without you by my side, \
        but then I spent so many nights thinking how you dod me wrong, \
            and I grew strong'

# with escape character \n \
print(my_space_case)
lyrics = 'At first I was afraid, I was petrified, \
    Kept thinking I \ncould never live without you by my side, \
        but then I spent so many nights thinking how you dod me wrong, \
            and I grew strong'
# f-strings = Formatted strings
#way to insert code (avariable) into a string

profit = 120

my_f_string = ('the profit todsay is $ {profit*100})
print(my_f_string)

# MAth wirh strings


strings_plus = 'apples' + 'oranges'
print('apples'/'oranges')

# the calulation of strings combines them 

print('apples'+str(100))

#UPper and Lower Case

my_name = 'emiliano lopez'

my_middle_name ='De La Hoya'

print(my_name.upper())
print

#Boolean
my_bool = True
print(my_bool)
print(type(my_bool))
print(my_bool + 10)

#True == 1 False == 0
# Booleans CAN BE CONVERTED TO INTEGERS AND FLOATS
x = int(98.6)
