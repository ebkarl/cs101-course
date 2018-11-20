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

Your project will simulate rolling 5 dice and count how many times
the program needs to roll to get a Yahtzee (ie., all 5 dice the same)

1) You are given the function getRoll() that will return 5 dice values
   that you will use in the program.  Call this function as many times
   as you need.

2) You must implement the function isYathzee().  This function will return
   True if the 5 dice make a Yahtzee, otherwise return False.

3) Write code to use getRoll() and isYathzee() to solve this project.

4) Calculate the average number of rolls required to get Yathzze.  To calculate
   this average, simulate 1,000 "runs".

   For example:
      Run 1 takes 2013 rolls to get Yahtzee
      Run 2 takes 981 rolls to get Yahtzee
      Run 3 takes 1655 rolls to get Yahtzee
                      :
      Run 1000 takes 3601 rolls to get Yahtzee

      Add up the rolls in each run and average the results

5) You are free to create other functions in your project as you need them.  Instead
   of doing 1,000 runs, try a smallest number first such as 10 to make sure you
   code is working.

Sample Output:

Number of rolls to get a Yahtzee = 941
Average rolls to get a Yahtzee (1000 runs) = 1277.204

"""

import random

def getRoll():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice3 = random.randint(1, 6)
  dice4 = random.randint(1, 6)
  dice5 = random.randint(1, 6)
  return (dice1, dice2, dice3, dice4, dice5)

# Add your code below

def isYahtzee(d1, d2, d3, d4, d5):
  pass

