# Sometimes a programmer does not know how many times data is to be entered.
#   Create a program that adds an unknown amount of positive numbers that will be entered by the user.
#   The program stops adding numbers when the user enters a zero or a negative number.
#   Then the program prints the total.
#
# Input Format
#   an unknown amount of positive numbers followed by one zero or negative number
#
# Constraints
#   all input will be whole numbers
#
# Output Format
#   one whole number that is the sum of all positive inputs

total = 0
n = int(input())

while(0 < n):
    total = total + n
    n = int(input())

print(total)