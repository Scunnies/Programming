# This program reads in numbers until
# the user enters 0
# it will them print the numbers input
# and their average
#Author: Eleanor Sammon

numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))
while number != 0:
 numbers.append(number) # read in the next number and check if 0
 number = int(input("enter another (0 to quit): "))
for value in numbers:
 print (value)

# add the values, average them and prints output
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))