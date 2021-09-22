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
client_name = input("What is your name? : ")
# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = input(f"{client_name} what is the amount of your savings?: ")
#print statments added to add spaces.
print()
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
# Changinge the above variables that are to match the shorten versions bellow. such as "amzn = amazon" in order to make if statements.

print()
#stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
# Virtually emulated the above given code and added the ':' at the end to make it work.

stock = input("Which stock would you like to buy? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. : ")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# need to define amzn aapl and google in order for conditional statements to run... 
#amzn = amazon
#aapl = apple
#goog = google
'''
Your code should look like this:

if stock == amzn:
    ...
elif ...
else ...
'''
# making number of stock variable
number_of_stocks = 0 

# making if statements with the inputs above.
if stock == 'amzn':
    number_of_stocks = (int(client_savings) / amazon)
elif stock == 'aapl':
    number_of_stocks = (int(client_savings) / apple)
elif stock == 'fb':
    number_of_stocks = (int(client_savings) / fb)
elif stock == 'goog':
    number_of_stocks = (int(client_savings) / google)
elif stock == 'msft':
    number_of_stocks = (int(client_savings) / msft)

if number_of_stocks > 0:
    print(f"{client_name} since you have ${client_savings} you can buy {number_of_stocks} stock(s) in {stock}")
elif number_of_stocks < 0: 
    print("Unfortunately you cannot afford a full {stock} stock at this time.")
'''
#elif number_of_stocks > 0:
    print(f"{client_name} it seems you can buy {number_of_stocks} stock(s) of {stock}")
#elif number_of_stocks < 0:
    print("Unfortunately {stock} seems to expensive for you at this time.")
#elif number_of_stocks > 0:
    print(f"{client_name}, it turns you can purchase {number_of_stocks} stock(s) of {stock} at this time.")
#elif number_of_stocks < 0:
    print("Please try to save more money in order to invest it wisely")
#elif number_of_stocks > 0:
    print(f"{client_name}, good news! You can buy {number_of_stocks} stock(s) of {stock}!")
#elif number_of_stocks < 0:
    print("I dont know how to tell you this...but you will not be investing today.")
#lif number_of_stocks > 0:
    print(f"{client_name}, as it turns out you'll be able to buy {number_of_stocks} stock(s) of {stock} today.")
#elif number_of_stocks < 0:
    print("Well you can try investing when you have more money saved up.")
# All this was a mistake in coding but kept it becuase I make be able to play with it to say different things 
  depending on the number of stocks bought.
''' 




print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()

