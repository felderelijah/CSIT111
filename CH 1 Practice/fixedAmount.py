# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 10 amount paid over time

#beginning of prompt
#A person pays a fixed amount each month as a car payment.
#Design a program that asks the user to enter the amount paid each month,
#and the number of months the user has been making payments.
#The program should then display the total amount that the user has paid.
#end of prompt

amount = float(input('Enter the amount paid each month: '))
months = int(input('Enter the number of months payments made: '))
print()

total = amount * months

print('Transaction History: ')
print('Recurring Bill:', amount)
print('Months Paid:', months)
print('The total amount for payments made: $', total)

