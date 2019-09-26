# You have asked the user to enter a letter from ‘a-z’. Knowing the user won't always do as asked, you should ignore
# any character that is not between ‘a-z’ and continue getting input until a letter between ‘a-z’ is entered. Once it
# has been entered, output that letter.
#
# Input Format
# # A series of individual characters
#
# Constraints
# # One character
#
# Output Format
# # Output the first proper input

i = 0
while i == 0:
    let = input()
    if "a" <= let <= "z":
        print(let)
        i += 1