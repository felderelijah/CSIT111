# Elijah Felder
# 09/29/23
# Programming Practice 2

# exercise 9 shipping charges

#beginning of prompt
#Design a program that asks the user to enter the weight of a package
#and then displays the shipping charges.
#end of prompt

p1 = 1.10
p2 = 2.20
p3 = 3.70
p4 = 3.80

weight = int(input('Enter the weight of the package: '))
print()

perP1 = weight * p1
perP2 = weight * p2
perP3 = weight * p3
perP4 = weight * p4

if weight <= 2:
    print('Shipping Rate:', p1)
    print('The shipping charge will be: $', perP1)
elif weight > 2 and weight <= 6:
    print('Shipping Rate:', p2)
    print('The shipping charge will be: $', perP2)
elif weight > 6 and weight <= 10:
    print('Shipping Rate:', p3)
    print('The shipping charge will be: $', perP3)
else:
    print('Shipping Rate:', p4)
    print('The shipping charge will be: $', perP4)

    
