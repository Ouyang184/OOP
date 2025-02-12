'''

OOP lab 3 Part B 
Name: Jake Ouyang
Date: 2/5/2025
'''

user_input = int(input('Enter a Number >> '))
for outer in range(1,  user_input + 1):
    for inner in range(1, user_input +1):
        print(f'{inner * outer:5d}', end =' ')
    print('')
        