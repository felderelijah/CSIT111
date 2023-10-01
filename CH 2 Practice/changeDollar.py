# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 8 change for a dollar game

#beginning of prompt
#Design a change-counting game that gets the user to enter the number of coins required to make exactly one dollar.
#The program should ask the user to enter the number of pennies, nickels, dimes, and quarters.
#If the total value of the coins entered is equal to one dollar,
#the program should congratulate the user for winning the game.
#Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar.
#end of prompt

Q = 0.25
D = 0.10
N = 0.05
P = 0.01

quarters = int(input('Enter the number of quarters: '))
dimes = int(input('Enter the number of dimes: '))
nickels = int(input('Enter the number of nickels: '))
pennies = int(input('Enter the number of pennies: '))
print()

QT = quarters * Q
DM = dimes * D
NK = nickels * N
PE = pennies * P

total = QT + DM + NK + PE

if total == 1.00:
    print('Congratulations you WON the game!')
elif total > 1.00:
    print('Amount was more than $1.00, Try again :)')
elif total < 1.00:
    print('Amount was less than $1.00, Try again :)')
