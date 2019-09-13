#This originally won't work with out code embedded in the challenge so I added two lines and removed two to make it work

# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day
# and we add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
#   The year can be evenly divided by 4, is a leap year, unless:
#   The year can be evenly divided by 100, it is NOT a leap year, unless:
#   The year is also evenly divisible by 400. Then it is a leap year.
#
# Task
#   You are given the year, and you have to write a function to check if the year is leap or not.
#
# Input Format
#   Read y, the year that needs to be checked.
#
# Output Format
#   Your function must return a boolean value (True/False)

#removed
#def is_leap(year):
leap = False

#added line
year = int(input("Enter the Year to check if it is a leap year: "))

 # Write your logic here
if (year % 4 == 0):
    # Checks if the century is a leap year
    if (year % 100 == 0):
        if (year % 400 == 0):
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

#added line
print(leap)

#removed
#return leap