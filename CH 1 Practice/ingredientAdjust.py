# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 15 ingredient adjuster

#beginning of prompt
#A cookie recipe calls for the following ingredients:
#1.5 cups of sugar
#1 cup of butter
#2.75 cups of flour
#The recipe produces 48 cookies with these amounts of the ingredients.
#Design a program that asks the user how many cookies they want to make,
#and then displays the number of cups of each ingredient needed
#for the specified number of cookies.
#end of prompt

SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

cookies = int(input('Enter how many cookies you want to make: '))

sucrose = (1.5/48) * cookies
butyricAcid = (1/48) * cookies
starch = (2.75/48) * cookies

print()
print('The amount of cups of sugar needed is:', sucrose)
print('The amount of cups of butter needed is:', butyricAcid)
print('The amount of cups of flour needed is:', starch)

