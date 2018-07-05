# *******************************************************************
# 11: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
# *******************************************************************

# *****************************************************************
# Write a program to read the Book of Mormon text and process it.
# 
# Example output:
# 
# Number of non-blank lines      : 32776
# Count of "Mormon" words        : 48
# Count of "God" words           : 1686
# Count of "And it came to pass" : 1092
# Average line length            : 43.59168293873566
# Number letter "e"              : 144848
# *****************************************************************

def doesContain(text, line):
	return (text.upper() in line.upper())


def removeSymbols(text):
    text = text.replace('\n', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(';', '')
    text = text.replace(')', '')
    text = text.replace('(', '')
    text = text.replace("'", '')
    return text


def countNonBlankLines(filename):
	pass


def countWord(filename, word):
	# Hint: you will need to use the function removeSymbols()
	# hint: use the function doesContain()
	pass


def countText(filename, text):
	# hint: use the function doesContain()
	pass


def calcAverageLineLength(filename):
	pass


def countLetter(filename, letter):
	pass

# ===========================================================================
# Main code


print('Number of non-blank lines      :', countNonBlankLines('bom.txt'))

print('Count of "Mormon" words        :', countWord('bom.txt', 'Mormon'))
print('Count of "God" words           :', countWord('bom.txt', 'God'))

print('Count of "And it came to pass" :', countText('bom.txt', 'And it came to pass'))

print('Average line length            :', calcAverageLineLength('bom.txt'))

print('Number letter "e"              :', countLetter('bom.txt', 'e'))



