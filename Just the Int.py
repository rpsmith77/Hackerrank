# Read in a float number. Output the integer portion of the number.
#
# Input Format
# # A number with a decimal component.
#
# Constraints
# # Number will be positive and less than 1000
#
# Output Format
# # A whole number

num = float(input())
print("{:.0f}".format(num//1))