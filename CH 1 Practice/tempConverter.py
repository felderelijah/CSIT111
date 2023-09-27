# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 12 temperature converter

#beginning of prompt
#Design a program that converts Celsius temperatures to Fahrenheit temperatures.
#The program should ask the user to enter a temperature in Celsius,
#and then display the temperature converted to Fahrenheit.
#end of prompt

celsius = int(input('Enter a temperature in Celsius: '))
print()

fahrenheit = (9/5 * celsius) + 32

print('The temperature converted to Fahrenheit is', fahrenheit)

