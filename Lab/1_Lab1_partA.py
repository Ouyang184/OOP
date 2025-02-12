'''
Name: Jake Ouyang
Class: OOP Lab 1
Date: 1/22/25
'''
import math
from decimal import Decimal
#Read input parameter
print("Some PI approximations: ")
#Archimedes 225 BC
print(f"22 / 7 = {22 / 7}")
#Zu Chongzhi 480AD
print(f"355 / 113 = {355 / 113}")
#Indiana law
print(f"16 / 5 = {16 / 5}")
#Python math library
print(f"math.pi = {math.pi}")
print()

 # Change the divison sign (/) to interger divsion sign(//) so the out put is round down to an interger
#Read input parameter
print("Some PI approximations: ")
#Archimedes 225 BC
print(f"22 / 7 = {22 // 7}")
#Zu Chongzhi 480AD
print(f"355 / 113 = {355 // 113}")
#Indiana law
print(f"16 / 5 = {16 // 5}")
#Python math library
print(f"math.pi = {math.pi:.0f}")
print()

# Using decimal library to get the greater degree of accuracy 
#Read input parameter
print("Some PI approximations: ")
#Archimedes 225 BC
print("Decimal('22') / Decimal('7') = ", Decimal(22) / Decimal(7))
#Zu Chongzhi 480AD
print(f"Decimal('355') / Decimal('113')", Decimal(355) / Decimal(113))
#Indiana law
print("Decimal('16') / Decimal('5') = ", Decimal(16) / Decimal(5))
#Python math library
print(f"math.pi = {math.pi:.22f}")
