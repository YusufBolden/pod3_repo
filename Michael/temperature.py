#converting 100 degrees Farenheit to celsius 
celsius_100 = (100-32) * (5/9)
print(celsius_100)
print(type(celsius_100))

# It is a float. There is a decimal 

# Converting a temperature of 0 degrees Fanrenheit to Celcius

celsius_0 = (0-32) * (5/9)
print(celsius_0)

# Converting a temp of 34.2 degrees fanrenheit to celsius
print((34.2-32) * (5/9))

#Converting 5 degrees celsius to fanrenheit 
print((5 * 9/5) + 32)

#Answering if 30.2 degrees celsius is hotter than 85.1 degrees fanrenheit 
celsius_30 = (85.1-32) * (5/9)
farenheit_85 = (30.2 * 9/5) + 32
print(bool(celsius_30 < farenheit_85))

