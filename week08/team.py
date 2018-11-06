"""
Course: CS101
File: team02.py
Author: Brother Comeau

Description:
  This is the code for the weekly team activity.  
  Please work together in groups of 2 to 3.  
  You will not be sumbitting your code for this activity.
  You are free to continue working on this activity after class if you need more time.


Sample Output:

Age 10 can't vote
Age 20 can't vote
Age 21 can vote
Age 30 can vote

Yes you are happy and knowit
You are a sad person
You are a sad person
You are a sad person

The three sorted values are:
339, 175, 11

happy

"""

import random

# ====================================================================
# Complete these functions

def canVote(age):
	# TODO -> add print statements if the person can vote based on age (above 20)
	pass


canVote(10)
canVote(20)
canVote(21)
canVote(30)
print()


def DisplayIfHappyAndKnowit(happy, knowit):
	# TODO -> add your print statements here
	pass


DisplayIfHappyAndKnowit(True, True)
DisplayIfHappyAndKnowit(True, False)
DisplayIfHappyAndKnowit(False, True)
DisplayIfHappyAndKnowit(False, False)
print()



def displayThreeSortedValues(a, b, c):
	print('The three sorted values are:')
	# TODO -> Add your if statements here
	#         hint: use this format -> print('{}, {}, {}'.format(a, b, c))
	pass


displayThreeSortedValues(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))
print()


# ====================================================================
# Using assert() to test functions

def add(a, b):
	pass

assert(add(1, 2) == 3)
assert(add(-10, 20) == 10)


def multiply(a, b):
	pass

assert(multiply(1, 2) == 2)
assert(multiply(-1, 1000) == -1000)
assert(multiply(10, 20) == 200)


def power(a, b):
	pass

assert(power(2, 0) == 1)
assert(power(2, 1) == 2)
assert(power(2, 2) == 4)
assert(power(2, 3) == 8)
assert(power(2, 4) == power(2, 3) * 2)


def subtract(a, b):
	return (a - b)

# TODO -> create at least 3 assert() tests for the function subtract() above.



def isFactor(number, factor):
	pass

assert(isFactor(10, 2) == True)
assert(isFactor(20, 3) == False)
assert(isFactor(21, 3) == True)

# ======================================================================
# Advanced features

happy = True

# TODO -> convert the following If statement to be one line 
#         (There are at least are two solutions)
if (happy):
	print('happy')
else:
	print('sad')


