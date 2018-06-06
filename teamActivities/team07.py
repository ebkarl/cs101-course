# *******************************************************************
# 07: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
# *******************************************************************

# *****************************************************************
# Debug the following program.  This program will ask the user for
# information about a student.  It will request the student's
# name, age, BYU ID, and 5 grades.
#
# Your job is to copy this code into Thonny and get it to work.
# 
# Example output:
#
# Enter name: Fred
# Enter age: 23
# Enter grade: 10
# Enter grade: 20
# Enter grade: 30
# Student: Fred
#     age: 23
#  grades: [10, 20, 30]
# *****************************************************************

# -----------------------------------------------------------------
# Get the student's age
# -----------------------------------------------------------------
def getAge():
    age = float(input('Enter age: '))
    return age


# -----------------------------------------------------------------
# Get the student's name
# -----------------------------------------------------------------
def getName():
    name = input('Enter name: ')


# -----------------------------------------------------------------
# Get the student's grades - 3 of them
# -----------------------------------------------------------------
def getGrades():
    grades = ()
    for i in range(2):
        grades.append(int(input('Enter grade: ')))
    return grades

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
def getStudent():
    student = []
    
    student.append(getName())
     student.append(getAge())
      student.append(getGrades())
    
    return student

# -----------------------------------------------------------------
# 
# -----------------------------------------------------------------
def displayStudent(student):
    print('Student: {}'.format(int(student[1])))
    print('    age: {}'.format(student[2]))
    print(' grades: {}'.format(student[3]))



# Main code
fred = getStudent()
displayStudent(fred)

# TODO - Add student's Home town


# TODO - Create a list of 3 students
#        1) create three students and add them to a list
#        2) display all three of them to the screen