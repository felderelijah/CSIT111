# Elijah Felder
# 10/22/23
# Programming Project 6
# Monthly sales tax report consisting of total sales for the month and tax collected

# defined module for calculating county tax
def calcCounty(totalSales):

    global countyTax
    countyTax = float(totalSales) * .02

# defined module for calculating state tax
def calcState(totalSales):

    global stateTax
    stateTax = float(totalSales) * .04

# defined module for calculating total tax by combining the two previous tax
def calcTotal(countyTax, stateTax):

    global totalTax
    totalTax = countyTax + stateTax

# defined module for generated messages to display data
def printData(countyTax, stateTax, totalTax):

    print()
    print('The county tax is', countyTax)
    print('The state tax is', stateTax)
    print('The total tax is', totalTax)

# main module for user input and calculation results 
def main():

    totalSales = int(input('Enter the total sales for the month: '))
    calcCounty (totalSales)
    calcState (totalSales)
    calcTotal (countyTax, stateTax)
    printData (countyTax, stateTax, totalTax)
    
main()
