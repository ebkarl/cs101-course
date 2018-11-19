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

This program will use Python's dictionary data structure to keep track of
three individuals.  An individual and his parents.

1) Add code in the main section of the project to convert the data records
   into dictionaries.
   
2) Implement the functions given in this file to produce the sample output
   using the dictionaries. 


Sample Output:

============================================================
Name : John Brown
Birth: 1950
Death: ---
Age  : ---
City : Rexburg
State: Idaho
============================================================
Name : Fred Brown
Birth: 1914
Death: 1965
Age  : 51 years
City : Logan
State: Utah
============================================================
Name : Mary Smith
Birth: 1918
Death: 1988
Age  : 70 years
City : Boston
State: Idaho
============================================================
Parent Fred Brown was 36 years old when John Brown was born
Parent Mary Smith was 32 years old when John Brown was born
============================================================
Parent Fred born in Utah and child John born in Idaho
Parent Mary and child John were born in same state Idaho


"""

def createData():
    """ Create the list of records """
    data = []

    data.append('Father name fred')
    data.append('Mother city boston')
    data.append('Father birth 1914')
    data.append('Ind city rexburg')
    data.append('Father city logan')
    data.append('Mother name mary')
    data.append('Ind death 0')
    data.append('Father surname brown')
    data.append('Mother state idaho')
    data.append('Ind name john')
    data.append('Mother surname smith')
    data.append('Ind birth 1950')
    data.append('Father state utah')
    data.append('Ind state idaho')
    data.append('Mother death 1988')
    data.append('Ind surname brown')
    data.append('Mother birth 1918')
    data.append('Father death 1965')

    return data


def displayPerson(person):
    """ Display the details of a person """
    print('=' * 60)
    # TODO -> fill out this function to display a person's details (match the sample output)
    pass


def displayParentAgeAtChild(parent, child):
    # TODO -> fill out this function to display age details of a
    # parent and child
    pass


def doesParentChildSameState(parent, child):
    # TODO -> fill out this function to display age details the
    # state parent and child where born
    pass


# =====================================================================
# Main Code - add your below

# Create the list of records strings
data = createData()

# Create the three dictionaries
ind = {}
father = {}
mother = {}

# TODO -> Add code here to convert the records found in the list "data"
# into the three dictionaries above (ie., ind, father and mother)

"""
Logic for the following code that you need to write:

process each line in the dictionary data
    split the line into words
    if line is for individual then add record to individual
    if line is for father then add record to father
    if line is for mother then add record to mother
"""

# Display individual details
displayPerson(ind)
displayPerson(father)
displayPerson(mother)

# Display family stats
print('=' * 60)
displayParentAgeAtChild(father, ind)
displayParentAgeAtChild(mother, ind)
print('=' * 60)
doesParentChildSameState(father, ind)
doesParentChildSameState(mother, ind)

# Add your code here

