# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 8 tip, tax, total

#beginning of prompt
#Design a program that calculates the total amount of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food,
#and then calculate the amount of a 15 percent tip and 7 percent sales tax.
#Display each of these amounts and the total.
#end of prompt

charge = float(input('Enter the charge for the food: '))
print()

#calculations
TIP = 0.15
salesTax = 0.07
service = charge * TIP
tax = charge * salesTax
total = charge + service + tax

#results
print('Receipt')
print('Charge:', charge)
print('Tip:', service)
print('Sales Tax:', tax)
print('Total:', total)
