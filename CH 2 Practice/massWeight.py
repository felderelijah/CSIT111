# Elijah Felder
# 09/28/23
# Programming Practice 2

# exercise 3 mass and weight

#beginning of prompt
#Design a program that asks the user to enter an object’s mass, and then calculates its weight.
#If the object weighs more than 1,000 Newtons, display a message indicating that it is too heavy.
#If the object weighs less than 10 Newtons, display a message indicating that it is too light.
#end of prompt

#constants because the value will not change for this exercise
MULT = 9.8
LIGHT = 10
HEAVY = 1000

#user input
mass = int(input('Enter the object mass: '))
weight = mass * MULT
print()

# results displayed with message below
print('Weight:', weight)
if weight > HEAVY:
    print('The object is too heavy.')
elif weight < LIGHT:
    print('The object is too light.')
else:
    print('This is a good weight.')

