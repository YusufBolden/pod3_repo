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
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

name = input('First Name and Last Name:')
savings = float(input('Savings Amount: '))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.


if stock == "amzn":
    print(f'{name} you have currently chosen to purchase Amazon stock and want to spend {savings} for this purchase.')
elif stock == "appl":
    print(f'{name} you have currently chosen to purchase Apple stock and want to spend {savings} for this purchase.')
elif stock == "fb":
     print(f'{name} you have currently chosen to purchase Facebook stock and want to spend {savings} for this purchase.')
elif stock == "goog": 
    print(f'{name} you have currently chosen to purchase Google stock and want to spend {savings} for this purchase.')
elif stock == "msft":
     print(f'{name} you have currently chosen to purchase Microsoft stock and want to spend {savings} for this purchase.')
else:
    print(f'I want to purchase a different stock.')

if stock == "amzn":
    purchase:float(savings/amazon)
elif stock == "appl":
    purchase: float(savings/apple)
elif stock == "fb":
     purchase: float(savings/facebook)
elif stock == "goog": 
    purchase: float(savings/google)
elif stock == "msft":
     purchase: float(savings/microsoft)
else:
    print(f'I want to purchase more of that stock')
    
'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f'Excellent!{name} for {savings} you can purchase {purchase} shares of {stock}.')

