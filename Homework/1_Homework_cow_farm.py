'''
Homework #1
DASC 12004 Intro to OOP
Name: Jake Ouyang

'''
print("Congratulations on deciding to buy a farm! Let's check your budget,\nfarm size, and cows to figure out your profit!")

print('')

# Input for the length of the short side of the farm
Length_short_side = int(input('What is the length of the long side of your farm? >> '))

print('The short side of your farm is', Length_short_side, 'ft.')

print('') # Blank line for spacing

# Input for the length of the long side of the farm
Lenght_long_side = int(input('What is the length of the long side of your farm? >> '))

print('The long side of your farm is', Lenght_long_side, 'ft.')

print('')

# Input for the height of the farm
height_of_farm = int(input('What is the height of your farm? >> '))

print('The height of your farm is',height_of_farm,'ft.')

print('')

# Input for the cost of land per square foot
cost_of_land_per_sq = float(input('What is the cost of land per square foot? >> '))

print('The land costs $',cost_of_land_per_sq,'per square foot.')

print('')

# Input for the budget for buying cows
Budget_for_cows = int(input('What is your budget for buying cows? >> '))

print(f'You have ${Budget_for_cows:,.2f} available for buying cows.')

print('')

# Calculate the area of land using the formula for the area of a trapezoid
Area_of_land = ((Lenght_long_side + Length_short_side)/2)* height_of_farm

# Calculate the total price of the land
Total_Price_of_land = Area_of_land * cost_of_land_per_sq

print(f'You are buying {Area_of_land:,.2f} sq ft of land for total price of ${Total_Price_of_land:,.2f}.')

print('')

# Cost of one cow
one_cow_cost = 2500

# Calculate the number of cows you can buy with your budget
num_cows = Budget_for_cows // one_cow_cost # // is just divison but you only get whole number instead of float 

# Calculate the leftover budget after buying cows
left_over_budget = Budget_for_cows - (num_cows * one_cow_cost)

# Calculate the total cost of cows
Total_cost_of_cows = num_cows * one_cow_cost

print(f'You are buying {num_cows} cows and have ${left_over_budget:,.2f} left over from your cow\nbudget.')

print('')

# Calculate the initial investment cost
initial_investment_cost = Total_Price_of_land + Total_cost_of_cows

print(f'Your initial investment into the land and cows was ${initial_investment_cost:,.2f}.')

print('')

# Calculate the annual income from cows
Income_from_cow_year = (1250 * num_cows) * 12 


# Calculate the annual maintenance cost for cows
maintenance_for_cow_year = (172 * num_cows) * 12

# Calculate the annual profit from cows
annual_profit = Income_from_cow_year - maintenance_for_cow_year

print(f'You will make ${annual_profit:,.2f} per year from your cows. Moo!')



