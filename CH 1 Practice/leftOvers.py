# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 11 left over pizza

#beginning of prompt
#You’re planning a pizza party and you plan to give each person three slices of pizza.
#Design a program that displays the number of slices that will be leftover.
#The program should ask for the following input:
#The number of pizzas you will have
#The number of slices that each pizza is cut into
#The number of people that will be attending
#The program should display the number of slices that will be left over.
#end of prompt

#constant concept
RECEIVED = 3

#user input
pizzas = int(input('Enter the number of pizzas you will have: '))
slices = int(input('Enter the number of slices that each pizza is cut into: '))
people = int(input('Enter the number of people that will be attending: '))
print()

#calculations for slices left
perPerson = people * RECEIVED
available = pizzas * slices
leftover = available - perPerson

print('Available:', available)
print('Slices missing:', perPerson)
print('Slices left:', leftover)

