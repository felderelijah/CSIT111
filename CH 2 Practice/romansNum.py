# Elijah Felder
# 09/28/23
# Programming Practice 2

# exercise 1 roman numerals

#beginning of prompt
#Design a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number.
#If the number is outside the range of 1 through 10, the program should display an error message.
#end of prompt

#user input
number = int(input('Enter a number within the range of 1-10: '))
print()

# if/else translation for roman numerals 
if number == 1:
    print('Translated as a Roman Numeral: I')
elif number == 2:
    print('Translated as a Roman Numeral: II')
elif number == 3:
    print('Translated as a Roman Numeral: III')
elif number == 4:
    print('Translated as a Roman Numeral: IV')
elif number == 5:
    print('Translated as a Roman Numeral: V')
elif number == 6:
    print('Translated as a Roman Numeral: VI')
elif number == 7:
    print('Translated as a Roman Numeral: VII')
elif number == 8:
    print('Translated as a Roman Numeral: VIII')
elif number == 9:
    print('Translated as a Roman Numeral: IX')
elif number == 10:
    print('Translated as a Roman Numeral: X')
else:
    print('ISSUE: You did not enter a number between 1-10.')
