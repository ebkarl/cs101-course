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

Create a simple monthly budget.

1) Create a simple 5 item budget

2) Each item MUST have three variables:
  a) Item's name as a string (ie., 'movies', 'food', etc...)
  b) Yearly amount as an integer (ie., 100)
  c) Monthly amount as a floating point.
     (You MUST calculate this value based on yearly amount)

  In Summary
    - create a variable for the item's name
    - create a variable for yearly amount for the item
    - create a variable and calculate (use math) the monthly amount 
      based on the year amount

3) There is code provided that creates a random value for
   the 6th item.  You don't need to understand this code,
   just know that it will create a different random value
   each time you run the program.

   You need to include the variables randomYearAmount and randomMonthAmount
   in your budget output as the last item.

4) Create two variables to total the monthly and yearly amounts
   and display them in the budget.  You need to use math.

5) Notice that the columns of values are right aligned.

6) You will end up with a total of 19 variables.  All variable names
   must be meaningful (no single letters or abbreviations)
          5 item names
          6 monthly values
          6 yearly values
          2 totals
          ----------------
          19 variables

7) There is a variable for a random value in the given code.  You can
   leave the text "Random Value" in the output.

Example Output:


Monthly Budget
=================================================
Item                     Month               Year
=================================================
item 1             $     8.33           $     100
item 2             $    16.67           $     200
item 3             $    25.00           $     300
item 4             $    33.33           $     400
item 5             $    41.67           $     500
Random Value       $    10.33           $     124
=================================================
Totals             $   135.33           $    1624

"""

import random

# TODO -> create your variables here



# Do not change this line of code
randomYearAmount = random.randint(10, 100000)

# TODO -> uncomment this code to calculate randomMonth valueAmount
#         Change "?Amount" to convert the above variable to a monthly
#         value.
# randomMonthAmount = ?Amount


# TODO -> add your budget print() statements here

