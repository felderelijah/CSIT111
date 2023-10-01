# Elijah Felder
# 09/28/23
# Programming Practice 2

# exercise 2 rectangles areas

#beginning of prompt
#The area of a rectangle is the rectangle’s length times its width.
#Design a program that asks for the length and width of two rectangles.
#The program should tell the user which rectangle has the greater area,
#or whether the areas are the same.
#end of prompt

# user input for both rectangles
length1 = int(input('Enter the length for the first rectangle: '))
width1 = int(input('Enter the width for the first rectangle: '))
print()
length2 = int(input('Enter the length for the second rectangle: '))
width2 = int(input('Enter the width for the second rectangle: '))
print()

# area formula for rectangles 
rect1 = length1 * width1
rect2 = length2 * width2

# conditions for determing which has a greater area
if rect1 > rect2:
    print('Rectangle #1 has the greater area.')
elif rect2 > rect1:
    print('Rectangle #2 has the greater area.')
else:
    print('The area for both rectangles are equal.')
