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

You will be writing a program to roll 100,000 virtual dice.  The prorgam
will keep track of the following and then display it to the screen;

1) The number of times each dice side/number is rolled.

2) The number of "three-in-a-row" sequences
   Example 1: 
        if the program rolls 4, 5, 2, 2, 2, 4, then
        one sequence of three in a row.

   Example 2: 
        if the program rolls 4, 5, 2, 2, 2, 2, 4, then
        two sequences of three in a row.

3) The number of "sequence of three".
   Example 1: 
        if the program rolls 3, 5, 2, 3, 4, 8, then
        one sequence (2, 3, 4).

   Example 2: 
        if the program rolls 3, 5, 2, 3, 4, 5, 8, then
        two sequences (2, 3, 4) and (3, 4, 5)


Misc Informaiton:

    # To "roll a dice"
    roll = random.randint(1, 6)


Sample Output (Your program needs to match these results):

Total rolls: 100000
1 was rolled   16901 times
2 was rolled   16694 times
3 was rolled   16812 times
4 was rolled   16565 times
5 was rolled   16426 times
6 was rolled   16602 times
Number of three-in-a-row 2801
Number of sequence-of-three 1846

"""

import random

# Do not change or delete this line
random.seed(123)

# Add your code here

