# *******************************************************************
# 06: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
# *******************************************************************

# *****************************************************************
# Write a program to ask a student for 5 grades (0.0 to 100.0).
# You will be using functions to create and use the list of grades
# that the function getGrades() creates.
# 
# Example output:
# 
# Enter Grade: 10
# Enter Grade: 20
# Enter Grade: 30
# Enter Grade: 40
# Enter Grade: 50
# Grades : [10.0, 20.0, 30.0, 40.0, 50.0]
# Total  : 150.0
# Average: 30.0
# Lowest : 10.0
# Highest: 50.0
# *****************************************************************

# ===================================================================
def getGrades():
    pass        # replace with your code for this function

# ===================================================================
def getTotal():
    pass        # replace with your code for this function

# ===================================================================
def getAverage():
    pass        # replace with your code for this function

# ===================================================================
def getLowest():
    pass        # replace with your code for this function

# ===================================================================
def getHighest():
    pass        # replace with your code for this function

# ===================================================================
# Main code

grades = getGrades()
total = getTotal(grades)
avg = getAverage(grades)
lowest = getLowest(grades)
highest = getHighest(grades)

print('Grades : {}'.format(grades))
print('Total  : {}'.format(total))
print('Average: {}'.format(avg))
print('Lowest : {}'.format(lowest))
print('Highest: {}'.format(highest))