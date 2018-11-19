"""
Course: CS101
File: <name of your file>
Project: <project number>
Author: <Your name>

Description:
  <What does your project/program do?>
"""

"""
Instructions:

Replace the "pass" statements with python code to complete each function.

Sample Output:

Month 1 - Jan
Month 5 - May
Month 10 - Oct

day of the week 0 - Sunday
day of the week 1 - Monday
day of the week 2 - Tuesday
day of the week 3 - Wednesday
day of the week 4 - Thursday
day of the week 5 - Friday
day of the week 6 - Saturday

[2, 16, 19, 28, 33, 33, 59, 69, 80, 93]
Average:        43.2
Max value:      93
Min value:      2
Second highest: 80
Three lowest:   37
Grade exist:    10 - False
Grade exist:    33 - True
Grade exist:    20 - False
Closest to 50:   59

"""

import random

def getMonthName(month):
  """ Return the month's name.  Do not use any if statements or print statements
      for example: when month == 5, return the string 'May' """
  pass

def getWeekdayName(day):
  """ Return the week day's name.  Do not use any if statements or print statements
      for example: when day == 1, return the string 'Monday'
      0 = Sunday, 1 = Monday, .... 6 = Saturday """
  pass


def displayGradesSorted(grades):
  """ Display the list grades in sorted order ie., [2, 45, 56, 89] """
  pass


def calcGradeAverage(grades):
  """ Return the average of grades """
  pass


def getMaxGrade(grades):
  """ Return the max value in the grades list """
  pass


def getMinGrade(grades):
  """ Return the min value in the grades list """
  pass


def getSecondHighestGrade(grades):
  """ return the second highest grade in the list """
  pass


def sumThreeLowestGrades(grades):
  """ Return the sum of the three smallest values in the list """
  pass


def doesGradeExist(grades, value):
  """ return True if value is in the list grades """
  pass


def getClosestGradeTo50(grades):
  """ Return the grade that is closest to 50.  If there is a tie, return either grade
      For example: [30, 40, 55, 20] -> return 55 
      For example: [30, 45, 55, 20] -> return 45 or 55 """
  pass

# ===========================================================================
# Main code - Do not edit

# create a list of random grades
grades = []
for i in range(10):
  grades.append(random.randint(1, 100))

# Display month names
print('Month {} - {}'.format(1, getMonthName(1)))
print('Month {} - {}'.format(5, getMonthName(5)))
print('Month {} - {}'.format(10, getMonthName(10)))
print()

# Display week day names
for i in range(7):
  print('day of the week {} - {}'.format(i, getWeekdayName(i)))
print()

displayGradesSorted(grades)

print('Average:        {}'.format(calcGradeAverage(grades)))
print('Max value:      {}'.format(getMaxGrade(grades)))
print('Min value:      {}'.format(getMinGrade(grades)))
print('Second highest: {}'.format(getSecondHighestGrade(grades)))
print('Three lowest:   {}'.format(sumThreeLowestGrades(grades)))
print('Grade exist:    {} - {}'.format(10, doesGradeExist(grades, 10)))
print('Grade exist:    {} - {}'.format(grades[4], doesGradeExist(grades, grades[4])))
print('Grade exist:    {} - {}'.format(20, doesGradeExist(grades, 20)))
print('Closest to 50:  {}'.format(getClosestGradeTo50(grades)))
