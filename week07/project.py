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

This project contains code in the main part of the program.  Do NOT
Change any of this code.  Your job is to implement the missing functions
that the main code calls.  The current code for this project will 
not compile and run until you create the missing functions.  
You must pass all of the tests.

Example Output:

    isAgeOver20(21)                     : Passed
not isAgeOver20(10)                     : Passed
not isAgeOver20(20)                     : Passed

    isAge20andOver(21)                  : Passed
not isAge20andOver(10)                  : Passed
    isAge20andOver(20)                  : Passed

not isAge10(20)                         : Passed
    isAge10(10)                         : Passed
not isAge10(5)                          : Passed

    isAgeNot10(20)                      : Passed
not isAgeNot10(10)                      : Passed
    isAgeNot10(5)                       : Passed

    isTeenager(13)                      : Passed
    isTeenager(19)                      : Passed
not isTeenager(10)                      : Passed
not isTeenager(20)                      : Passed

not isAge10or20(11)                     : Passed
not isAge10or20(19)                     : Passed
    isAge10or20(10)                     : Passed
    isAge10or20(20)                     : Passed

    allSameValues(10, 10, 10)           : Passed
not allSameValues(20, 10, 10)           : Passed
not allSameValues(10, 20, 10)           : Passed
not allSameValues(10, 10, 20)           : Passed

not isTextLength10('123456789')         : Passed
    isTextLength10('1234567890')        : Passed
not isTextLength10('12345678901')       : Passed

not is3rdCharacterLetterX('Happy')      : Passed
not is3rdCharacterLetterX('OXO')        : Passed
    is3rdCharacterLetterX('XOX')        : Passed

not isLetterThere('Happy', 3, 'X')      : Passed
not isLetterThere('OXO', 2, 'X')        : Passed
    isLetterThere('OXO', 1, 'X')        : Passed
    isLetterThere('ABCDE', 4, 'E')      : Passed

"""

import sys

# TODO -> Add your functions here.  Don't forget to have function
#         comments.


# =====================================================================
# =====================================================================
# =====================================================================
# Main Code - DO NOT EDIT.  You can comment code out while you are writting
#             the functions above.  However, you must have everything 
#             un-commented when you submit your project for full points.

def test(text):
    print('{:<40}: {}'.format(text, 'Passed' if eval(text) else '*** FAILED ***'))


print('You need to implement the missing functions and have them')
print('calculate and return the correct value to pass all of the tests.\n')

test('    isAgeOver20(21)')
test('not isAgeOver20(10)')
test('not isAgeOver20(20)')

print()

test('    isAge20andOver(21)')
test('not isAge20andOver(10)')
test('    isAge20andOver(20)')

print()

test('not isAge10(20)')
test('    isAge10(10)')
test('not isAge10(5)')

print()

test('    isAgeNot10(20)')
test('not isAgeNot10(10)')
test('    isAgeNot10(5)')

print()

test('    isTeenager(13)')
test('    isTeenager(19)')
test('not isTeenager(10)')
test('not isTeenager(20)')

print()

test('not isAge10or20(11)')
test('not isAge10or20(19)')
test('    isAge10or20(10)')
test('    isAge10or20(20)')

print()

test("    allSameValues(10, 10, 10)")
test("not allSameValues(20, 10, 10)")
test("not allSameValues(10, 20, 10)")
test("not allSameValues(10, 10, 20)")

print()

test("not isTextLength10('123456789')")
test("    isTextLength10('1234567890')")
test("not isTextLength10('12345678901')")


print()

test("not is3rdCharacterLetterX('Happy')")
test("not is3rdCharacterLetterX('OXO')")
test("    is3rdCharacterLetterX('XOX')")

print()

# Arguments: text, position, letter
test("not isLetterThere('Happy', 3, 'X')")
test("not isLetterThere('OXO', 2, 'X')")
test("    isLetterThere('OXO', 1, 'X')")
test("    isLetterThere('ABCDE', 4, 'E')")

