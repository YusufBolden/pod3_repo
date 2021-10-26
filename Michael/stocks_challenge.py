
print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
facebook = 250
google = 1400
microsoft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
Name = input('What is your name? ')
Savings = int(input('How much do you have in savings? '))
Stock =input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.  ")
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
if Stock == 'amzn': 
    amzn = Shares=(Savings/amazon)
    print(f'{Name} has ${Savings} in Savings and he can buy {Shares} shares of Amazon at the current price of 3000')
elif Stock == 'aapl':
    aapl = Shares=(Savings/apple)
    print(f'{Name} has ${Savings} in Savings and he can buy {Shares} shares of Apple at the current price of 100')
elif Stock == 'fb':
    fb = Shares=(Savings/facebook)
    print(f'{Name} has ${Savings} in Savings and he can buy {Shares} shares of Facebook at the current price of 250')
elif Stock == 'goog':
    goog = Shares= (Savings/google)
    print(f'{Name} has ${Savings} in Savings and he can buy {Shares} shares of Google at the current price of 1400')
elif Stock == 'msft':
    msft = Shares=(Savings/microsoft)
    print(f'{Name} has ${Savings} in Savings and he can buy {Shares} shares of Microsoft at the current price of 200')
else:
    print('Invalid Name, Please try again')

    

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()

