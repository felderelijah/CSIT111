# Elijah Felder
# 11/08/23
# Programming Project 8
# Track a grocery store total number of bottles collected for recycling for seven days

# Initialized variables for the program
totalBottles = 0
todayBottles = 0
counter = 1

# while loop with a counter iteration
while counter <= 7:
    # input from user
    todayBottles = int(input("Enter the total number of bottles for today: "))
    totalBottles = totalBottles + todayBottles
    counter = counter + 1
    # while loop for input validation
    # any number below 0 will not be accepted
    while todayBottles < 0:
        print("Invalid Entry.\nTry again.")
        todayBottles = int(input("Enter the total number of bottles for today: "))

# CONSTANT variable for the percentage
# that will be multiplied by the total amount of bottles for the week
BASE = .10
#formula to the find the how much will be paid
totalPayout = BASE * totalBottles
# display results 
print('\nThe total numbers of bottles collected were', totalBottles)
print('The total amount to be paid is', totalPayout)

