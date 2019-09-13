# Write an if/elif statement that assigns a value to the variable bonus depending on the amount of sales, which will be input.
#
# Sales Bonus
#   Greater than or equal to 100,000 10,000
#   Greater than or equal to 75,000 5,000
#   Greater than or equal to 50,000 2,500
#   Greater than or equal to 25,000 1,000
#
# Input Format
#   a whole number
#
# Constraints
#   input will be positive
#
# Output Format
#   One of the bonus amounts listed in the problem statement.

sales = int(input())

if(sales >= 100000):
    print("Your bonus is $10,000.00")
elif(sales >= 75000):
    print("Your bonus is $5,000.00")
elif(sales >= 50000):
    print("Your bonus is $2,500.00")
elif(sales >= 25000):
    print("Your bonus is $1,000.00")
else:
    print("Your bonus is $0.00")