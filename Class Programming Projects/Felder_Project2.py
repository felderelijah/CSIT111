# Elijah Felder
# 09/17/2023
# Programming Project 2
# Decision structure for monthly sale goals

# welcome message
print ('Welcome to the program')

#user input
monthlySales = float(input('Enter the monthly sales $'))
print ()

print ('You reported that your monthly sales were $', monthlySales)
print ()

# rewards depending on results from monhtly sales
if monthlySales >= 100000:
    print ('You earned a $5000 bonus!')
if monthlySales >= 112500:
    print ('All employees get one day off!!!')

