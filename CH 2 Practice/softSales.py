# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 7 software sales

#beginning of prompt
#Design a program that asks the user to enter the number of packages purchased.
#The program should then display the amount of the discount (if any)
#and the total amount of the purchase after the discount.
#end of prompt

packages = int(input('Enter the number packages of packages purchased: '))
print()

# formula to apply discount and new price
d50 = packages * 0.50
d40 = packages * 0.40
d30 = packages * 0.30
d20 = packages * 0.20

NP50 = packages - d50
NP40 = packages - d40
NP30 = packages - d30
NP20 = packages - d20

# showcases the results of which discount is applied and the new price 
if packages >= 100:
    print('You receive a discount!')
    print('Discount: 50%')
    print()
    print("New Price: $", NP50)
elif packages >= 50 and packages <= 99:
    print('You receive a discount!')
    print('Discount: 40%')
    print()
    print("New Price: $", NP40)
elif packages >= 20 and packages <= 49:
    print('You receive a discount!')
    print('Discount: 30%')
    print()
    print("New Price: $", NP30)
elif packages >= 10 and packages <= 19:
    print('You receive a discount!')
    print('Discount: 20%')
    print()
    print("New Price: $", NP20)
else:
    print('No discount.')
