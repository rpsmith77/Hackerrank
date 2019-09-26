# Users don't always provide input as expected. You have asked the user to input an even number.
# Read in the number the user entered. As long as the number is not even, ignore the input and
# read in another number. When the input is even, output that number.
#
# Input Format
# # A variable number of odd numbers and then an even number
#
# Constraints
# # Input will be whole numbers
#
# Output Format
# # Output the even number that was entered

i = 0
while i == 0:
    num = int(input())
    if num % 2 == 0:
        print(num)
        i += 1
