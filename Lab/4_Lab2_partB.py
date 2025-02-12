'''
Name: Jake Ouyang
Date: 1/29/2025
OOP lab 2 part 2 
'''
#Initializing variables
card_num = 0
card_name = ""
#Read user input
card_num = int(input("Enter card number [1..13] >> "))
if (card_num == 1):
    card_name = "Ace"
elif (card_num == 2):
    card_name = "Two"
elif (card_num == 3):
    card_name = "Three"
elif (card_num == 4):
    card_name = "Four"
elif ( card_num == 5):
     card_name= "Five"
elif (card_num == 6):
     card_name= "Six"
elif (card_num == 7):
    card_name = "Seven"
elif (card_num == 8):
    card_name = "Eight"
elif (card_num == 9):
    card_name = "Nine"
elif (card_num == 10):
    card_name = "Ten"
elif (card_num == 11):
    card_name = "Jack"
elif (card_num == 12):
    card_name = "Queen"
elif (card_num == 13):
    card_name = "King"
else:
    print("Not in the deck of card")
    exit()
#Finish the code
print(card_name)


card_suit = ""
#Read user input
card_input = int(input("Enter card suit [1 - spades, 2 - hearts, 3 - clubs, 4 - diamonds] >> "))
match card_input:
    case 1:
        card_suit = "spades"
        print(card_name ,'of' ,card_suit)
    case 2:
        card_suit = "hearts"
        print(card_name ,'of', card_suit)
    case 3:
        card_suit = 'clubs'
        print(card_name ,'of', card_suit)
    case 4:
        card_suit = 'diamonds'
        print(card_name ,'of', card_suit)
    case 5:
        print('Error! This is not a valid suit')
        exit()
        
