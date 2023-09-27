# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 9 customer acquisition cost

#beginning of prompt
#Design a program that asks the user to enter each of the costs of the marketing campaign
#(advertising, marketing personnel salaries, and sales staff commissions).
#The program should also ask the user to enter the number of new customers that were acquired.
#Then, the program should calculate and display the customer acquisition cost.
#end of prompt


print('Enter the cost of the marketing campaign in the following fields.')
print()

advertising = float(input('Enter the cost for advertising: '))
marketing = float(input('Enter the cost for marketing personnel salaries: '))
sales = float(input('Enter the cost for sales staff comissions: '))
NC = int(input('Enter the number of new customers that were acquired: '))

CAC = (advertising + marketing + sales) / NC
print()

print('Results: ')
print('The customer acquisition cost is:', CAC)
