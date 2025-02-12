'''

OOP Homework 2 
Name: Jake Ouyang
Date: 2/7/2025

'''
# importig library for use
import random
import time

# constants to store different values
Rock = 1 
Paper = 2 
Scissors = 3

# Creating a random number generator
random.seed(time.time())
random_pick = random.randint(1,3) # Generates 1, 2, or 3
computer_picks = random_pick # Initial computer move


# Prompting player for difficulty level
print('Welcome to rock, paper, scissors! Choose the computer\'s difficulty \nlevel:\n\t1. Easy \n\t2. Medium \n\t3. Hard')

player_input = int(input("Choose the computer\'s difficulty level >> "))

# Validate difficulty level selection
match player_input:
    case 1:
        print('The Computer is set to Easy mode.')
    case 2:
        print('The Computer is set to Medium mode.')
    case 3:
        print('The Computer is set to Hard mode. \nComputer let out a laugh')
    case _:
        print('Invalid input')
        exit()
        

# Prompting player for their move
player_picks = int(input('Your Turn!!\n\t1. Rock\n\t2. Paper\n\t3. Scissors\nInput a move >> '))

# Convert computer's numerical choice to string representation
if player_picks == 1:
    player_picks = 'Rock'
elif player_picks == 2:
    player_picks = 'Paper'
elif player_picks == 3:
    player_picks = 'Scissors'
else:
    print('Your pick was not part of the options')
    exit()



# Difficulty Level: Easy (Random move)
if player_input == 1:
    computer_picks = random_pick

# Difficulty Level: Medium (50% chance of changing it to hard mode)
if player_input == 2:
    random_gen = random.randint(1,10)
    if random_gen % 2 == 0:
        computer_picks = random_pick
    elif random_gen % 2 != 0:
        if player_picks == 'Rock':
            computer_picks = 'Paper'
        elif player_picks == 'Paper':
            computer_picks = 'Scissors'
        elif player_picks == 'Scissors':
            computer_picks = 'Rock'

# Difficulty Level: Hard (Always counters player)

if player_input == 3:
    if player_picks == 'Rock':
        computer_picks = 'Paper'
    
    elif player_picks == 'Paper':
        computer_picks = 'Scissors'
        
    elif player_picks == 'Scissors':
        computer_picks = 'Rock'

# Convert computer's numerical choice to string representation
if computer_picks == 1:
    computer_picks = 'Rock'
elif computer_picks == 2:
    computer_picks = 'Paper'
elif computer_picks == 3:
    computer_picks = 'Scissors'

# Player and Computer picks echo
print(f'Computer chose {computer_picks}')
print(f'Player chose {player_picks}')

# The result of the player pick compare to computer pick
if computer_picks == 'Rock' and player_picks == 'Paper':
    print('player Win. Paper wrap rock')
elif computer_picks == 'Scissors' and player_picks == 'Rock':
    print('Player Win. Rock smash Scissors')
elif computer_picks == 'Paper' and player_picks == 'Scissors':
    print('Player Win. Scissors cut Paper')
elif computer_picks == 'Rock' and player_picks == 'Scissors':
    print('Computer Win. Rock smash Scissors')
elif computer_picks == 'Scissors' and player_picks == 'Paper':
    print('Computer Win. Scissors cut Paper')
elif computer_picks == 'Paper' and player_picks == 'Rock':
    print('Computer Win. Paper wrap Rock')
elif computer_picks == player_picks:
    print('Player Tie with Computer')
