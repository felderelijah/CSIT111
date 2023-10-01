# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 5 color mixer

#beginning of prompt
#Design a program that prompts the user to enter the names of two primary colors to mix.
#If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message.
#Otherwise, the program should display the name of the secondary color that results.
#end of prompt

red = 'red'
blue = 'blue'
yellow = 'yellow'

Red = 'Red'
Blue = 'Blue'
Yellow = 'Yellow'

color1 = input('Enter one primary color: ')
color2 = input('Enter another primary color: ')
print()

redBlue = 'purple'
redYellow = 'orange'
blueYellow = 'green'

if (color1 == red or color1 == Red) and (color2 == blue or color2 == Blue):
    print('The secondary color would be', redBlue)
elif (color1 == red or color1 == Red) and (color2 == yellow or color2 == Yellow):
    print('The secondary color would be', redYellow)
elif (color1 == blue or color1 == Blue) and (color2 == yellow or color2 == Yellow):
    print('The secondary color would be', blueYellow)
elif (color1 == blue or color1 == Blue) and (color2 == red or color2 == Red):
    print('The secondary color would be', redBlue)
elif (color1 == yellow or color1 == Yellow) and (color2 == red or color2 == Red):
    print('The secondary color would be', redYellow)
elif (color1 == yellow or color1 == Yellow) and (color2 == blue or color2 == Blue):
    print('The secondary color would be', blueYellow)
else:
    print('Only primary colors can be entered.')
