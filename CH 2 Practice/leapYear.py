# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 11 leap year detector

#beginning of prompt
#Design a program that asks the user to enter a year,
#and then displays a message indicating whether that year is a leap year or not.
#Use the following logic to develop your algorithm:
#If the year is evenly divisible by 100 and is also evenly divisible by 400, then it is a leap year.
#For example, 2000 is a leap year but 2010 is not.
#If the year is not evenly divisible by 100, but it is evenly divisible by 4, it is a leap year.
#For example, 2008 is a leap year but 2009 is not.
#end of prompt

year = int(input('Enter a year: '))

if year % 4 == 0 and year % 100 != 0:
    print('This is a leap year')
elif year % 100 == 0 and year % 400 == 0:
    print('This is a leap year as well.')
else:
    print('This is not a leap year')
