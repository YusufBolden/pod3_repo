print("Challenge 3.2: Playing with the stock market")
import math 

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

# Input values



# Tickers
# amazon = "amzn"
# apple = "aapl"
# fb= "Facebook"
# google = "goog"
# msft = "microsoft"





print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_1 = input("Please enter your name: ")
# print(f'Hi! Whats your name?{client_1}')
print(client_1)

# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = int(input("How much have you saved: "))
print(f"you saved {client_savings}")

# # TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")


# print(stock(type(amazon, apple, fb, google, msft)))


# print("Challenge 3.2.2: Perform user-specific calculations")
# # TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

if stock == 'amzn':
  stock = client_savings / amazon
  stock = math.floor(stock)
  print("User wants to purchase Amazon")
  print(f"you just bought{stock}")
  print("Congratulations on your purchase!")
elif stock == 'aapl':
    stock = client_savings / apple
    print("Congratulations on your Apple purchase!")
    print(f"you just bought{stock}")
elif stock == 'fb':
    stock = client_savings / fb
    print("User wants to purchase Facebook")
    print(f"you just bought{stock}")
    print("Congratulations on your purchase!")
elif stock == 'goog':
    stock = client_savings / google
    print("User wants to purchase Google")
    print(f"you just bought{stock}")
    print("Congratulations on your purchase!")
elif stock == 'msft':
    stock = client_savings / msft
    print("User wants to purchase MicroSoft")
    print(f"you just bought{stock}")
    print("Congratulations on your purchase!")
else: 
    print("sucka you ain't got no money to invest!")

# if the stock is equal to amazon then deduct the cost of amzn from savings. 



# '''
# Your code should look like this:

# if stock == "amzn":
#     ...
# elif ...
# else ...
# '''

# print()

# print("Challenge 3.2.3: Output for the user the result")
# # TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

 # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

# print()