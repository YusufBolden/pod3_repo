#converting farenheit 100 to celsius and saving it to the variable celsius_100
celsius_100 = ((100 - 32) * 5/9)
#printing celsius_100
print(celsius_100)
#converting 0 degrees farenheit to celsius and saving to variable celsius_0
celsius_0 = ((0 - 32) * 5/9)
#printing celsius_0
print(celsius_0)
#converting and printing temperature of 34.2 degrees farenheit to celsius
print((34.2 - 32) * 5/9)
#converting 5 degrees celsius to farenheit
print((5 * 9/5) + 32)
#conversion of 30.2 degrees celsius to farenheit and adding to variable farenheit_conversion
farenheit_conversion = (30.2 * 9/5) + 32
#printing 30.2 degrees celsius to farenheit conversion
print(farenheit_conversion)
#conversion of 85.1 degrees farenheit to celsius and adding to variable celsius_conversion
celsius_conversion = ((85.1 - 32) * 5/9)
#printing celsius_conversion
print(celsius_conversion)
#printing boolean statement regarding which temperature is hotter
print(bool(farenheit_conversion < celsius_conversion))