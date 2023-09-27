# Elijah Felder
# 09/14/23
# Programming Practice CH 1

#exercise 1 personal information

#beginning of prompt
#Design a program that displays the following information:
#Your name
#Your address, with city, state, and ZIP
#Your telephone number
#Your college major
#end of prompt

#user input
Name = input('What is your name?: ')
print()

numAddress = int(input('What is your house numbering?: '))
streetName = input('What is your street address name, city, and state? (Seperate with commas): ')
zipCode = int(input('What is your ZIP?: '))
print()

Phone = int(input('What is your telephone number?: '))
Major = input('What is your college major?: ')
print()

#ouput from the information entered
print('Hello,', Name, '.')
print('Your address is', numAddress, streetName, zipCode, '.')
print('Your phone number is', Phone, '.')
print('Your college major is', Major, '.')
print()
