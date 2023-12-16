# Elijah Felder
# 11/28/23
# Programming Project 10
# Calculates the total of a blood drive over several days \
# Inputting the results into a file and displaying them upon requeest

# getPints function
def getPints(pints):
    counter = 0
    # loop for user input
    while counter < 7:
        pints[counter] = int(input('Enter pints collected: '))
        counter = counter + 1
    return pints

#getTotal function
def getTotal(pints, totalPints):
    counter = 0
    while counter < 7:
        #formula for total
        totalPints = totalPints + pints[counter]
        counter = counter + 1
    return totalPints

#getAverage function
def getAverage(totalPints, averagePints):
    #formula for average
    averagePints = float(totalPints) / 7
    return averagePints

# output function to a file
def writeToFile(averagePints, pints):
    outFile = open('blood.txt', 'a')
    outFile.write('Print Each Hour\n')
    counter = 0
    while counter < 7:
        outFile.write(str(pints[counter]) + '\n')
        counter = counter + 1
    outFile.write('Average Pints: ')
    outFile.write(str(averagePints) + '\n\n')
    outFile.close()

# input function from a file
def readFromFile(averagePints, pints):
    inFile = open('blood.txt', 'r')
    str1 = inFile.read()
    print(str1)
    pints = inFile.read()
    print(pints)
    print()
    str2 = inFile.read()
    print(str2)
    averagePints = inFile.read()
    print(averagePints)
    print()
    inFile.close()

# main function
def main():
    
    endProgram = 'no'
    print()
    while endProgram == 'no':
        option = 0
        print()
        # user input if you would to insert fields
        # or display records
        print('Enter 1 to enter in new data and store to file')
        print('Enter 2 to display data from the file')
        option = int(input('Enter now ->'))
        print()

        # declare variables
        pints = [0] * 7
        totalPints = 0
        averagePints = 0

        # option 1
        if option == 1:
            # function calls
            pints = getPints(pints)
            totalPints = getTotal(pints, totalPints)
            averagePints = getAverage(totalPints, averagePints)
            writeToFile(averagePints, pints)
        # option 2
        else:
            # loop to end program upon request
            endProgram = input('Do you want to end program? (Enter yes or no): ')
            while not (endProgram == 'yes' or endProgram == 'no'):
                # if any value entered outside of the two possible values
                # it will repeat your only options
                print('Please enter a yes or no')
                endProgram = input('Do you want to end program? (Enter yes or no): ')
            readFromFile(averagePints, pints)
main()

