# Elijah Felder
# 09/14/23
# Programming Practice 1

#exercise 14 major and nonmajor percentages 

#beginning of prompt
#The computer science department at a college offers a programming course that is required for all computer science majors.
#The course is also popular with students who are not computer science majors.
#Design a program that asks the user to enter the number of computer science majors that are registered in the class,
#and the number of nonmajor students that are registered in the class.
#The program should display the percentages of computer science majors and nonmajor students that are registered in the class.
#HINT: Suppose there are 12 computer science majors and 8 nonmajor students in the class. There are 20 students in the class.
#end of prompt

majors = int(input('Enter the number of computer science majors that are registered in the class: '))
non = int(input('Enter the number of nonmajor that are registered in the class: '))
print()

total = majors + non
a = majors / total
b = non / total

print('The percentage of computer science majors in the class is:', a)
print('The percentage of nonmajors in the class is:', b)

