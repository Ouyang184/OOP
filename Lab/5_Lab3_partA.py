'''

OOP lab 3 part A 
Name: Jake Ouyang
Date: 2/5/2025
'''
# Get user input
userNumber = int(input("Enter a number >> "))
#Print numbers from [1…input]
num = 1
my_list = []
while num <= userNumber:
    num += 1
    my_list.append(num)
    
print(f'My list >> {my_list}')
# Add append even numbers from l to even_num and all odd to odd_num
even_num = []
odd_num = []
for num in my_list:
    if num % 2 ==0:
        even_num.append(num)
    elif num % 2 != 0:
        odd_num.append(num)


#Print even_num
print("Even Numbers")
print(even_num)
#print odd_num
print("Odd Numbers")
print(odd_num)