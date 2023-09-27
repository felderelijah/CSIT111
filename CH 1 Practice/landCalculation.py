# Elijah Felder
# 09/14/23
# Programming Practice 1

# exercise 3 land calculation

#beginning of prompt
#One acre of land is equivalent to 43,560 square feet.
#Design a program that asks the user to enter the total square feet in a tract of land
#and calculates the number of acres in the tract.
#HINT: Divide the amount entered by 43,560 to get the number of acres.
#end of prompt

# one acre has a set value 
oneAcre = 43560

# performs divsion to find results for acres based off input
tractLand = float(input('Enter the total square feet in a tract of land: '))
acres = tractLand / oneAcre
print()

print('The number of acres in the tract are', acres, '.')
print()
