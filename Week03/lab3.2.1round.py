#this program rounds a float number to a whole number
#author: Eleanor Sammon

#ask user for a number with decimal places and then round it to nearest int 
Number = float(input("Enter a number: "))
RoundNumber = round(Number)

#output result
print ("{} rounded is {}" .format (Number, RoundNumber))