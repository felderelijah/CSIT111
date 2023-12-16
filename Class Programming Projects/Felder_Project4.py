# Elijah Felder
# 10/3/23
# Programming Project 4
# grocery store bottle tracker

totalBottles = 0
todayBottles = 0
counter = 1
PAY = .10

while counter <= 7:
    print('Enter the number of bottle for today: ')
    todayBottles = int(input())
    totalBottles = totalBottles + todayBottles
    counter = counter + 1

totalPayout = PAY * totalBottles

print('The total number of bottles returned this week is', totalBottles)
print('The total payout amount is', totalPayout)
