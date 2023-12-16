# Elijah Felder
# 11/25/23
# Programming Project 9
# Calculate the average pints of blood donated during a blood drive

# the getPints function
def getPints(pints):
    counter = 0
    for counter in range(0,7):
        pints[counter] = int(input('Enter pints collected: '))

# the getTotal function
def getTotal(pints):
    counter = 0
    totalPints = 0
    for counter in range(0,7):
        totalPints = totalPints + pints[counter]
    return totalPints

# the getAverage function
def getAverage(totalPints):
    averagePints = totalPints / 7
    return averagePints

# the getHigh function
def getHigh(pints):
    highPints = pints[0]
    index = 1
    for index in range(1,7):
        if pints[index] > highPints:
            highPints = pints[index]
    return highPints

# the getLow function
def getLow(pints):
    lowPints = pints[0]
    index = 1
    for index in range(1,7):
        if pints[index] < lowPints:
            lowPints = pints[index]
    return lowPints

# the displayInfo function
def displayInfo(averagePints, highPints, lowPints):
    print('The average pints donated', averagePints)
    print('The highest number of pints donated',highPints)
    print('The lowest number of pints donated', lowPints)
# the main method
def main():

    # declare variables

    again = 'yes'
    pints = [0] * 7
    averagePints = 0
    highPints = 0
    lowPints = 0

    # function calls

    while again.lower() == 'yes':
        getPints(pints)
        totalPints = getTotal(pints)
        averagePints = getAverage(totalPints)
        highPints = getHigh(pints)
        lowPints = getLow(pints)
        displayInfo(averagePints, highPints, lowPints)

        again = input('Do you want to run again (yes or no): ')

main()
