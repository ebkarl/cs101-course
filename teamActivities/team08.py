# *******************************************************************
# 08: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# Use the print() function to get the output that is in the double quotes.
# *******************************************************************

# *****************************************************************
# This solution from Week 07 team activity and replace lists
# with dictionaries
# 
# Example output:
#
# Enter name: Fred
# Enter age: 23
# Enter grade: 10
# Enter grade: 20
# Enter name: Mary
# Enter age: 33
# Enter grade: 30
# Enter grade: 40
# Enter name: John
# Enter age: 43
# Enter grade: 50
# Enter grade: 60
#
# Student: Fred
#     age: 23
#  grades: [10, 20]
# Student: Mary
#     age: 33
#  grades: [30, 40]
# Student: John
#     age: 43
#  grades: [50, 60]
# 
# *****************************************************************

# -----------------------------------------------------------------
# Get the student's age
# -----------------------------------------------------------------
def getAge():
    age = int(input('Enter age: '))
    return age


# -----------------------------------------------------------------
# Get the student's name
# -----------------------------------------------------------------
def getName():
    name = input('Enter name: ')
    return name


# -----------------------------------------------------------------
# Get the student's grades - 3 of them
# -----------------------------------------------------------------
def getGrades():
    grades = []
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
    print('Student: {}'.format(student[0]))
    print('    age: {}'.format(student[1]))
    print(' grades: {}'.format(student[2]))



# Main code
fred = getStudent()
displayStudent(fred)

# TODO
#    1) Copy this code into Thonny
#    2) add code to require three students from the user
#    3) convert code to use a dictionary to hold the students
#       a) Note: You will still have the grades as a list.
