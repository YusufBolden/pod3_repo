print('Question 1')
# TODO: Fix error(s) so that the if/else blocks runs without issues
a = 1
b = 2
#to fix the code bellow I fixed the indentation issue
if a < b:
    print(f'{a} is less than {b}')
else:
    print(f'{a} is greater than {b}')

print('')

print('Question 2')
# TODO: Fix error(s) so that a list of sandwiches with unique combinations of meats and cheeses is printed at line 22

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

sandwiches = []

# The block bellow will corrected by adding a colon as well as correcting the variable that was meet to meat.
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')

print(sandwiches)

print('')

print('Question 3')
# TODO: Fix error(s) in the the print statements to repeat a string

# To fix the issue I put the quotations around the dictionary brakets to create a string rather then a dictionary.
def repeat(str, times):
    return str * times


print(repeat('python', 3))
print(repeat('[]', 3))
print(repeat('//', 3))
print(repeat('{}', 5))
print(repeat('{[', 3))

print('')

print('Question 4')
# TODO: Fix error(s) in the print statements to look up all 5 fruits by their index

fruits = ['apples', 'oranges', 'bananas', 'tomatoes', 'cherries']
# Need to reorganize the indexes, lists index start at zero not one.
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])


print('')

print('Question 5')

num = input("Enter a number to compute it's square value: ")

# Line 65 currently error out if you provide an input like a dictionary instead of a number
# TODO: Rewrite line 65 with try/except blocks to handle all exceptions. If an exception exists, print 'Something Went Wrong!'
# TODO: Bonus: Add a finally block to print 'The End'

try:
    print(int(num) * int(num))
except:
    print("Something Went Wrong!")
finally:
    print('The End')


print('Question 6')

# TODO: Change the code here so that the 'NameError' exception block runs.
# Just commented out the "name" variable in order to get the desired 'except' print statement.
#name = 'Yusuf'

try:
    print(name.capitalize())
except NameError:
    print('You got to run this exception block! Your challenge is completed!')
except:
    print('You should not be seeing this print statement. Try a different solution!')
