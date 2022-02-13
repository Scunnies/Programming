# this program asks user to enter a number
# and says whether number is even or odd
#Author: Eleanor Sammon

# request user input
aNumber = int (input ("Enter an integer: "))

# tell the program how to react based on the input
if (aNumber % 2) ==0:
    print ("{} is an even number " .format (aNumber))

else:
    print ("{} is an odd number" .format (aNumber))