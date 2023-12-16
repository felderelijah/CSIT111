# Elijah Felder
# 09/17/23
# Programming Project 3
# Dual Alternative Decision structure

# welcome message
print ('Welcome to the program')

# user input
monthlySales = float(input('Enter the monthly sales $'))
print ()

salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100
print ()

# if-elseif-else clauses for store bonuses  
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# if-elseif-else clauses for empliyee bonuses
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# outcome messages displayed depending on metrics 
print ('The store bonus amount is $', storeAmount)
print ('The employee bonus is $', empAmount)
print ()

if storeAmount == 6000 and empAmount == 75:
    print ('Congrats! You have reached the highest bonus amounts possible!')
