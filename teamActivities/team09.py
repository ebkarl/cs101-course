# *******************************************************************
# 09: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
# *******************************************************************

# *****************************************************************
# Part One
# Write a program to display the factors of a number
# 
# Example output:
# 
# factors of 97 are: [1, 97]
# factors of 405761 are: [1, 199, 2039, 405761]
# factors of 360 are: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360]
# factors of 40960 are: [1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 64, 80, 128, 160, 256, 320, 512, 640, 1024, 1280, 2048, 2560, 4096, 5120, 8192, 10240, 20480, 40960]
# Common factors of 360 and 40960 are: [1, 2, 4, 5, 8, 10, 20, 40]
# 
# *****************************************************************

def getFactors(number):
	factors = []

	# Write your code here to return a list of the factors of the given number

	return factors

def commonNumbers(list1, list2):
	newList = []

	# Write code to return a list of common values between
	# list1 and list2

	return newList

factors97 = getFactors(97)
print('factors of 97 are:', factors97)

factorsBig = getFactors(405761)
print('factors of 405761 are:', factorsBig)

factors360 = getFactors(360)
print('factors of 360 are:', factors360)

factors40k = getFactors(40960)
print('factors of 40960 are:', factors40k)

common = commonNumbers(factors360, factors40k)
print('Common factors of 360 and 40960 are:', common)

# ================================================================
# Part Two
# Write a program to display different shapes using the given functions
# 
# Example output:
# 
# Square of size = 3
# ***
# * *
# ***
# 
# Square of size = 5
# *****
# *   *
# *   *
# *   *
# *****
# 
# Rectangle of size = 3 x 5
# *****
# *   *
# *****
# 
# Rectangle of size = 4 x 6
# ******
# *    *
# *    *
# ******
# 
# Right Angle of size = 3
# *
# **
# ***
# 
# Right Angle of size = 5
# *
# **
# ***
# ****
# *****
# 
# ================================================================

def star():
	print('*', end='')

def space():
	print(' ', end='')

def newline():
	print('')

def displaySquare(size):
	print('\nSquare of size =', size)

	# Enter your code here to display a square of stars of the given size


def displayRect(width, height):
	print('\nRectangle of size =', width, 'x', height)

	# Enter your code here to display a rectangle of stars of the
	# given width and height


def displayRightAngle(size):
	print('\nRight Angle of size =', size)

	# Enter your code here to display a right triangle of stars of the given size


# ========================================================================
# This code will call your functions above to display those shapes
displaySquare(3)
displaySquare(5)

displayRect(3, 5)
displayRect(4, 6)

displayRightAngle(3)
displayRightAngle(5)
