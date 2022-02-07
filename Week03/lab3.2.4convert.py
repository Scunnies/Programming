#this program takes a float amount and returns absolute amount in cents
#Author: Eleanor Sammon

number = float(input("Input monetary amount: "))
absoluteNumber = abs(int(number*100))

#when I first ran this it was giving me a float output 
#so I added int to my conversion to keep it as a whole number output

print ("The absolute amount of {} in cents is {}" .format (number, absoluteNumber))