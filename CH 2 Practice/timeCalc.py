# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 10 time calculator

#beginning of prompt
#Design a program that asks the user to enter a number of seconds,
#and works as follows:
#end of prompt

m = 60
h = 3600
d = 86400

secs = int(input('Enter the number of seconds: '))

mins = secs / m
hours = secs / h
days = secs / d

if secs >= m and secs < h:
    print('The number of seconds converted to minutes would be: ', mins)
elif secs >= h and secs < d:
    print('The number of seconds converted to hours would be: ', hours)
elif secs >= d:
    print('The number of seconds converted to days would be: ', days)
else:
    print('It is just', secs, 'seconds.')
