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

- This project contains a small program that will calculate areas
  and perimeters of different shapes.  
- There is code in the main section of the project that you can
  NOT edit.  
- Your task is to create and implement the missing functions 
  that the code in main calls.
- you must use math to calculate these values.  
- Your goal is to match the sample output below.

Note, don't forget to replace the TODO comments with function 
descriptions.


Output:

Welcome to project 06 - Calculate Areas and Perimeters
======================================================
Circle   : area = 39.82, perimeter = 22.37
Square   : area = 85.19, perimeter = 36.92
Rectangle: area = 41.24, perimeter = 34.24
Triangle : area = 21.16

"""

import math

# Add your code here

# TODO -> Add welcome function here


# TODO -> Add circle area function here


# TODO -> Add circle perimeter function here


# TODO -> Add square area function here


# TODO -> Add Square perimeter function here


# TODO -> Add rectangle area function here


# TODO -> Add rectangle perimeter function here


# TODO -> Add triangle area function here



# =====================================================================
# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()

radius = 3.56
area = calcAreaCircle(radius)
perimeter = calcPerimeterCircle(radius)
print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))

side = 9.23
area = calcAreaSquare(side)
perimeter = calcPerimeterSquare(side)
print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))

width = 2.9
height = 14.22
area = calcAreaRect(width, height)
perimeter = calcPerimeterRect(width, height)
print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))

base = 7.97
height = 5.31
area = calcAreaTriangle(base, height)
print('Triangle : area = {0:.2f}'.format(area))

