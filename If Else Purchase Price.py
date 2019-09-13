# Write a program that accepts the cost of two items to be purchased, then the payment amount. If the amount entered is less than the total cost of the two items, print a message that states how much is still owed. Otherwise, print a thank you message and state how much change will be given.
#
# Input Format
#   Input will be numbers in the format nn.nn
#
# Constraints
#   All input values will be positive
#
# Output Format
#   You still owe nn.nn or Thank you, your change is nn.nn

#Get the price of the first item
price1 = float(input())
#Get the price of the second item
price2 = float(input())
#Get the payment amount
payment = float(input())
difference = payment - price1 - price2
# Determine if customer still owes
if(difference < 0):
    print("You still owe ${:,.2f}".format(-difference))

# or if change is owed
else:
    print("Thank you, your change is ${:,.2f}".format(difference))