print("Challenge 3.1: Debug code snippets")
#Debug each snippet in order

print()

print("Code Snippet 1:")

u = 5
v = 2

# In this section an extra "=" was needed: it was (if u * v = 10:)
if u * v == 10:
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")

print()

print("Code Snippet 2:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

# The line below was missing a ":" after the y. I added one to correct it.
elif z > x and z < y:
    print("z is between x and y")

# The statement bellow is also missing a ":" after else so I added one.
else:
    print("z is greater than y")


print()

print("Code Snippet 3:")

#modify the comparison operator below so the assert statement passes
#update the print statement to reflect changes to the code

a = 1
b = 1
# added an "=" after '>' in the paranthesis in order to make it run
# also appended the print statement to correspond to the correction by stating that it is 'greater than or equal to'
c = (a >= b)

print(f"The value of c ({c}) is True since a ({a}) is greater than or equal to b ({b}).")
assert(c == True) #Do not change this line

print()

print("Code Snippet 4:")

#modify exactly one boolean operator in the assignment of d, so that d evaluates to False

# Both outputs must be false or there must be an "and" operator to a True and False output.
# solution is to change the "or" statment into an "and" statement in order for the "not(8<20)" to trigger as false.
d = (5 < 7) and not (8 < 20)
# TO DO: Explain how d is set to False in a print statement
# Adding a print statement
print("d is now set to false because while 5 is less than 7, the 'not'8 < 20 really states \nthat 8 is really greater than 20")
assert(d == False) #Do not change this line

print()


print("Code Snippet 5:")

#modify the comparison operator so o evalutes to true
#update the print statement to reflect the changes

m = "GOAT"
n = "goat"

#Needed add a "!" in place of the first "=" in order to make it True.
o = (m != n)

# Changed the "Python is case-sensitive" to " m is really not = to n"
print (f"The value of o ({o}) is True since m is not really = to n.")
assert(o == True) #Do not change this line

print()
print("CHALLENGE COMPLETE!")