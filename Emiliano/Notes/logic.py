a=3
b=4
c=5
print(a==b)
#<=, >=, ==, !=, <, > (comparison operators can be used to compare ) 
a=3
b=3.00
print(a==b)
# to compare if something is equal use the == sign

#Compound logic 
#or 
a=3
b=4
c=9 
print(a<b or c>b)
# Statements with or will always be a boolean value. 
# If one side evaluates to true the statement is true

#and
print(a>b and c>b)
# in an and statement both sides have to evaluate to true, if not it is false

#not is paired with one statement
print(not 1>2)

#Compound logic statements can be used together. 
print(a<b and not b>c)

# Conditional statements
my_wallet=5
friend_wallet=2
bagel_price=7

if my_wallet>=bagel_price:
    print("buying a bagel")
elif friend_wallet >= bagel_price:
        print("use friends money")
elif friend_wallet + my_wallet >= bagel_price:
    print('share bagel together')
    if (bagel_price>6):
        print('complain to friend')
    

else:
    print('complain about NY prices')

    answer = input('do you want to eat a bagel(press y/n)')
    if answer== "y":
        print('here is you bagel')
    elif answer == 'n':
        elif
        print('not a valid character')


# assert 
assert(answer=='y')

