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
name = input("Enter full name: ")
print(name)
# TODO: Write code to ask the client his savings and save it to another variable.
savings = input("Enter savings: ")
savings = int(savings)
print(savings)
print()
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
amnt_stock = 0
if stock == "amzn":
    amnt_stock = savings/amazon
elif stock == "goog":
    amnt_stock = savings/google
elif stock == "fb":
    amnt_stock = savings/fb
elif stock == "msft":
    amnt_stock = savings/msft
elif stock == "aapl":
    amnt_stock = savings/apple
else:
    print("insufficient funds")
print(f'{name}, you can buy {amnt_stock} stocks of {stock}.')
print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
#savings_current = int(savings)
result = f"{name} has {savings} and he can buy {amnt_stock} shares of {stock} at the current price of ${savings/amnt_stock}."
print(result)