'''
For this challenge, you will work in groups of 2 to 'pair program'
You'll need to work together to complete this challenge!
In general, 1 person should be typing, and the other should be leading what to code
But, it is always okay to swap roles or for the typing person to add their ideas too

-------------------------------------------------------------------


Your challenge: Make a bank account!
In this challenge, we want to make a bank account with 3 crucial functions
-create_account() - this function will initialize a bank account
-deposit() - add money to the account
-withdraw() - remove money from the account


PART 1: create_account()
This function should make a bank account!
The function does not need to take any arguments
The function should prompt the user using input() for username/password
The function should return a dictionary with 3 key/value pairs:
-username (string, should be what the user inputs)
-password (string, should be what the user inputs)
-balance (float, initialize this to 0)
'''

print('PART 1\n')
# TODO: define the create_account() function here and make sure it works
# HINT: make sure it works by doing something like my_account = create_account()
# Then print out my_account to see whether it has the correct info
def create_account():
    username = input("Please create a username here,: ")
    password = input("Please create a password here,: ")
    balance = float(0)
    created_account = {"username" : username, "password" : password, "balance": balance}
    return(created_account)
my_account = create_account()
print(my_account)

'''
PART 2: deposit()
This function should make a deposit to add money to the account
The function should take 2 arguments
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to deposit)

The function does not need to return anything, but should increase the balance value by the appropriate amount

Test your function by making a few deposits to your account, then printing out your account
'''

print('PART 2\n')
# TODO define the deposit() function here and make sure it works

deposits = float(input(f"Please input how much you would like to deposit: $"))
#Variable names become local and only exist inside that function. So whatever gets put into the parameter will take the names place in the function.
# [+=] is equivallent of keeping the term in this case += will take the place of the second account["balance"].
def deposit(account, deposit_amount):
    account["balance"] = account["balance"] + deposit_amount
#deposit prints none because there is no return statement

print(deposit(my_account, deposits))

print(f'{my_account["balance"]}$ is your updated balance.' )


'''
PART 3: withdraw()
This function should make a withdrawal to take money out of the account
The function should take 2 arguments:
-account (a dicionary representing a bank account, aka the output of create_account())
-amount (a float representing the amount to withdraw)

FIRST, the function should check whether there is enough money in the account to withdraw the requested amount
-If there is enough money, the function should decrease the balance value by the appropriate amount
-If there is not enough money, the function should print a message about the balance and tell the user there is not enough available to make that withdrawal

Test your function by making several withdrawals to your account
-try some you think will work AND some you think will not be allowed (more than the balance)
'''

print('PART 3\n')
# TODO define the withdraw() function here and make sure it works
money_withdrawn = float(input(f"How much would you like to withdraw: $ "))
def withdraw(account, amount):
    account["balance"] = account["balance"] - amount
print(withdraw(my_account, money_withdrawn))
print(f'{my_account["balance"]}$ is your remaining balance.')



'''
BONUS QUESTION 4: Password-protect withdrawal and deposits
Make new deposit_secure() and withdraw_secure() functions that prompt the user for their username/password FIRST
Only let the transaction proceed if they enter the right info!
Otherwise, tell the user the info is wrong

Test out your new functions to make sure they accept correct info, and let the user know if the password/username is incorrect
'''


# TODO: define password-protected withdraw_secure() and deposit_secure() functions
# HINT: there are tons of ways to do this correctly
# HINT: you can write any additional functions if you like
def deposit_secure():
    secure_account = input("Please verify your username: ")
    secure_password = input("Please verify your password: ")
    while True:
        if secure_account == my_account["username"] and secure_password == my_account["password"]:
            deposits = float(input(f"Please input how much you would like to deposit: $"))
            deposit(my_account, deposits)
            print(f'{my_account["balance"]}$ is your updated balance.' )
            done = input("If you are done press 1: ")
            if done == "1":
                break
            
            
        else:
            print("Sorry you have entered the wrong information try again.")
            
    
print(deposit_secure())

def secure_withdrawl():
    securing_username = input("To make a withdrawl please confirm your username: ")
    securing_password = input("Now please confirm your password: ")
    while True:
        if securing_username == my_account["username"] and securing_password == my_account["password"]:
            money_withdrawn = float(input(f"How much would you like to withdraw: $ "))
            withdraw(my_account, money_withdrawn)
            print(f'{my_account["balance"]}$ is your remaining balance.')
            withdraws = input("If you are done with your withdrawls press 1: ")
            if done == "1":
                break
        else:
            print("You may have put in an unaccounted for variable please try again.")
print(secure_withdrawl())