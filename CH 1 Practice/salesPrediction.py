# Elijah Felder
# 09/14/23
# Programming Practice CH 1

#exercise 2 sales information

#beginning of prompt
#A company has determined that its annual profit is typically 23 percent of total sales.
#Design a program that asks the user to enter the projected amount of total sales,
#and then displays the profit that will be made from that amount.
#HINT: Use the value 0.23 to represent 23 percent.
#end of prompt

# percent variable is in the form of a constant
PERCENT = 0.23

#user input 
totalSales = int(input('Enter the total amount of sales: '))

# formula for annual profit
annualProfit = totalSales * PERCENT
print()

print('Your annual profit is', annualProfit)
print()
