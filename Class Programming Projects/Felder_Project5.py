# Elijah Felder
# 10/3/23
# Project 5: For Loops
# Basic 'For Loop'

print('I will display the numbers 1 through 5')
for num in [1,2,3,4,5]:
    print(num)
print()

# 60 Second Counter Loop

print('I will display the numbers 1 through 60')
for num in range(1,61):
    print(num)
print()

# Accumulator Loop

total = 0

for counter in range(5):
    number = int(input('Enter a number: '))
    total = total + number
print('The total is', total)
print()

# The Average Age code

totalAge = 0
averageAge = 0

number = int(input('How many ages do you want to enter: '))
for counter in range(0, number):
    age = int(input('Enter an age: '))

    totalAge = totalAge + age

averageAge = totalAge / number
print('The average age is', averageAge)
