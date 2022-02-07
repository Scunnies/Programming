#this program floors, or rounds down, a number
#Author: Eleanor Sammon


import math

#ask user to input a variable and use math/floor function to round it down
numberToFloor = float(input("Type a number: "))
flooredNumber = math.floor(numberToFloor)

print ("{} floored is {}" .format(numberToFloor, flooredNumber))