#lab 3.3
# this program reads in two numbers
#divides them and gives a remainder
#author: Eleanor Sammon

#establish the two variables and convert to ints
x = int(input("What is your first number: "))
y = int(input("Enter the number you want to divide by: "))

#perform the calculations
answer = x//y
remainder = x%y

#present the results
print ("{} divided by {} is {} with a remainder of {}" .format (x, y, answer, remainder))