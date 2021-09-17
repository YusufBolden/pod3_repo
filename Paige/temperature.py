# converting 100 degrees farenheit to celsius.
celsius_100 = (100-32) * (5/9)
print(celsius_100)
#The result is the a float which can be determined by the decimal. 

#Converting 0 eegrees farenheit to celsius 
celsius_0 = (0-32) * (5/9)
print(celsius_0)

# Converting 34, 2 degrees farenheit to celsius in one print statement 
print((34.2-32) *(5/9))

# convert a temperature of 5 degrees celsius to farenheit f= 9/5 *(c+32) 
print((5*9/5)+(32))

# Answering the question: which is hotter 30.2 degrees celsius or 85.1 degrees farenheit 
farenheit_conversion = (30.2 *9/5)+32
celsius_conversion = (85.1-32) * (5/9)
print(bool(farenheit_conversion > celsius_conversion))
print("85.1 degrees_farenheit is hotter than 30.2 degrees celsius")
