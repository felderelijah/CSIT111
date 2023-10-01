# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 6 book club points

#beginning of prompt
#The points are awarded as follows:
#If a customer purchases 0 books, 0 points are awarded.
#If a customer purchases 1 book, 5 points are awarded.
#If a customer purchases 2 books, 15 points are awarded.
#If a customer purchases 3 books, 30 points are awarded.
#If a customer purchases 4 or more books, 60 points are awarded.
#Design a program that asks the user to enter the number of books
#they have purchased this month and displays the number of points awarded.
#end of prompt

print('Welcome to Serendipity Booksellers')
print()

books = int(input('Enter the number of books purhcased this month: '))

if books == 0:
    print('0 points are awarded')
elif books == 1:
    print('5 points are awarded')
elif books == 2:
    print('15 points are awarded')
elif books == 3:
    print('30 points are awarded')
elif books >= 4:
    print('60 points are awarded')
