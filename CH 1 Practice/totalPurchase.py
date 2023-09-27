# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 4 total purchase

#beginning of prompt
#A customer in a store is purchasing five items.
#Design a program that asks for the price of each item,
#and then displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 6 percent.
#end of prompt

# item count and prices
item1 = float(input('Enter the price for the first item: '))
item2 = float(input('Enter the price for the second item: '))
item3 = float(input('Enter the price for the third item: '))
item4 = float(input('Enter the price for the fourth item: '))
item5 = float(input('Enter the price for the fifth item: '))
print()

# calculation to find total with tax included
subTotal = item1 + item2 + item3 + item4 + item5
salesTax = 0.06
tax = subTotal * salesTax
total = subTotal + tax

#results
print('Recipt')
print('Subtotal:', subTotal)
print('Sales Tax:', salesTax)
print('Tax:', tax)
print('Your total is $', total)
