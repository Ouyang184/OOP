'''
Name: Jake Ouyang
Date: 1/22/25
Assignment: Lab 1 part 2
'''
#Input values
n1 = n2 = n3 = n4 = 0.
print("Enter four numbers.")
n1 = float(input("Number 1 >> "))
n2 = float(input("Number 2 >> "))
n3 = float(input("Number 3 >> "))
n4 = float(input("Number 4 >> "))

print()

#Calculate mean of 4 values
mean = (n1 + n2 + n3 + n4)/4
#Calculate variance of 4 values
variance = ((n1 - mean)*(n1 - mean) + (n2-mean)*(n2-mean) + (n3-mean)*(n3 - mean) + (n4-mean)*(n4-mean))/4

#Print the output
print(f"mean = {int(mean)}")
print(f"variance = {int(variance)}")