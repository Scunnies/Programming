#lab 3.2
#this program reads in two numbers and subtracts the second from the first
#author: Eleanor Sammon

#establish my variables and convert to ints
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

#perform the calc
answer = x-y

#present the result
print ("{} minus {} is {}" .format (x, y, answer))