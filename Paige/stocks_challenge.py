print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name")
# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("How much is in your savings account"))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple,'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
number_of_stocks = 0
if stock == "amzn":
    number_of_stocks = ({savings} / {amazon})
elif number_of_stocks > 0:
    print(f'{name} has $ {savings} You can purchase {number_of_stocks} of amazon')
elif number_of_stocks < 0:
    print('You do not have enough money to buy amazon stock')
elif stock == 'aapl':
        number_of_stocks = (savings / apple)
elif number_of_stocks > 0:
    print(f'{name} has $ {savings} You can purchase {number_of_stocks} of apple')
elif number_of_stocks < 0:
    print('You do not have enough money to buy apple stock')
elif stock == 'fb':
    number_of_stocks = (savings / facebook)
elif number_of_stocks > 0:
    print (f('{name} has $ {savings} You can purchase {number_of_stocks} of facebook'))
elif number_of_stocks < 0:
    print('You do not have enough money to buy facebook stock')
elif stock == 'goog':
    number_of_stocks = (savings/ google)
elif number_of_stocks > 0:
    print(f'{name} has $ {savings} You can purchse {number_of_stocks} of google')
elif number_of_stocks < 0:
    print('You do not have enough money to purchase google stock')
elif stock == 'msft':
    number_of_stocks = (savings / microsoft)
elif number_of_stocks > 0:
    print(f'{name} has $ {savings} You can purchse {number_of_stocks} of microsoft')
elif number_of_stocks < 0:
    print('You do not have enough money to buy microsoft stock')
print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f'{name} has $ in {savings} You can purchse {number_of_stocks} of Apple ')
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()

