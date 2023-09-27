# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 6 sales tax

#beginning of prompt
#Design a program that will ask the user to enter the amount of a purchase.
#The program should then compute the state and county sales tax.
#Assume the state sales tax is 4 percent and the county sales tax is 2 percent. The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
#HINT: Use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.
#end of prompt

purchase = float(input('Enter the amount of the purchase: '))
print()

# calculation to find total with tax included
state = 0.04
county = 0.02
stateTax = purchase * state
countyTax = purchase * county
totalTax = stateTax + countyTax

total = purchase + totalTax

print('Receipt')
print('Purchase Amount:', purchase )
print('State Tax:', stateTax)
print('County Tax:', countyTax)
print('Total Sales Tax:', totalTax)
print ('Your total is $', total)
