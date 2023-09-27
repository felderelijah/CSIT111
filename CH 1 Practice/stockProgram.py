# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 13 stock transaction program

#beginning of prompt
#Last month Jaden purchased some stock in Acme Software, Inc.
#Here are the details of the purchase:
#The number of shares that Jaden purchased was 1,000.
#When Jaden purchased the stock, he paid $32.87 per share.
#Jaden paid his stockbroker a commission that amounted to 2 percent
#of the amount he paid for the stock.
#Two weeks later Jaden sold the stock.
#Here are the details of the sale:
#The number of shares that Jaden sold was 1,000.
#He sold the stock for $33.92 per share.
#He paid his stockbroker another commission that amounted to 2 percent
#of the amount he received for the stock.
#Design a program that displays the following information:
#The amount of money Jaden paid for the stock.
#The amount of commission Jaden paid his broker when he bought the stock.
#The amount that Jaden sold the stock for.
#The amount of commission Jaden paid his broker when he sold the stock.
#Display the amount of profit or loss after Jaden sold the stock
#and paid his broker (both times).
#end of prompt

#no user interface interaction
PURCHASED = 1000
PAID = 32.87
PERCENT = 0.02

#variables values are eqaul to each other
MARKETED = PURCHASED
SELL = 33.92

money = PURCHASED * PAID
commission = money * PERCENT

sold = MARKETED * SELL
commissionTwo = sold * PERCENT

print('The amount of money Jaden paid for the stock: $', money)
print('The amount of commission Jaden paid his broker when he bought the stock: $', commission)
print('The amount that Jaden sold the stock for: $', sold)
print('The amount of commission Jaden paid his broker when he bought the stock: $', commissionTwo)
print()


