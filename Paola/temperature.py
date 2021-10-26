# Converting 100 degrees fahrenheit to celsius
celsius_100 = (100-32) * (5/9)
print(celsius_100)
# The result is the a float which can be determined by the decimal. 

# Converting 0 degrees fahrenheit to celsius
celsius_0 = (0-32) * (5/9)
print(celsius_0)

# Converting 34.2 degrees fahrenheit to celsius in one print statement
print((34.2-32) * (5/9))

# Converting 5 degrees celsius to fahrenheit (formula = (celsius * 9/5) + 32) 
print((5 * 9/5) + 32)

# Answering the question: what is hotter 30.2 degree celsius or 85.1 degress fahrenheit? 
fahrenheit_conversion = (30.2 *9/5)+32
celsius_conversion = (85.1-32) * (5/9)
print(bool(fahrenheit_conversion == celsius_conversion))

