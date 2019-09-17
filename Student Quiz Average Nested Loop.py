# Write a program that takes in information for three students. For each student get the student ID and three quiz
# grades. Use a nested loop, where the inner loop gets the three quiz grades. Print the student’s name and average –
# formatted to two decimal places.
#
# Input Format
#   A name and then three quiz scores.
#
# Constraints
#   Input will be whole numbers.

# Output Format
#   Name: Average:

for student in range (3):
    studentName = input()
    total = 0
    for testScores in range (3):
        scores = float(input())
        total = total + scores
    average = total / 3
    print("Name:", studentName)
    print("Average: {:,.2f}".format(average))