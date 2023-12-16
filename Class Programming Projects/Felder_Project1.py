# Elijah Felder
# 09/10/23
# Programming Project 1
# Calculates the user credits needed to graduate from their degree program

# user input
studentName = input('Enter student name: ')
print()

degreeName = input('Enter degree name: ')
print()

creditsDegree = float(input('Enter credits required for degree: '))
print()

creditsTaken = float(input('Enter credits taken: '))
print()

# calculation formula to see the amount of credits needed
creditsLeft = creditsDegree - creditsTaken

print('The students name is', studentName)
print('The degree name is', degreeName)
print('This means there are', creditsLeft, 'credits left until graduation.')
