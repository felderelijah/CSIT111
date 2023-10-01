# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 4 magic dates

#beginning of prompt
#Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year.
#The program should then determine whether the month times the day equals the year.
#If so, it should display a message saying the date is magic.
#Otherwise, it should display a message saying the date is not magic.
#end of prompt

month = int(input('Enter a month (in numeric form): '))
day = int(input('Enter a day (in numeric form): '))
year = int(input('Enter a two-digit year (in numeric form): '))
print()

magic = month * day

if magic == year:
    print('The date is a magic number.')
else:
    print('The date is not a magic number.')
