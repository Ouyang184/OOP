'''
Name: Jake Ouyang
Date: 1/29/2025
Class: OOP lab 2 part 1
'''

#Read test score
score = float(input("Enter test score >> "))
#check test score
if (score >= 100):
    print("Your grade is an A+")
elif (score > 90):
    print("Your grade is an A")
elif (score >= 80) and (score <= 90):
    print('Your grade is an B')
elif (score >= 70) and (score <= 80):
    print('Your grade is an C')
elif (score >= 60) and (score <= 70):
    print('Your grade is an D')
elif (score >= 50) and (score <= 60):
    print('Your grade is an F')
else:
    print("You are something else")