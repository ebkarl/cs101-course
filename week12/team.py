"""
Course: CS101
File: team.py
Author: Brother Comeau

Description:
  This is the code for the weekly team activity.  
  Please work together in groups of 2 to 3.  
  You will not be sumbitting your code for this activity.
  You are free to continue working on this activity after class if you need more time.


Sample Output:

Display Change
=================================================================
100 cents is Pennies = 0, Nickels = 0, Dimes = 0, Quarters = 4
 91 cents is Pennies = 1, Nickels = 1, Dimes = 1, Quarters = 3
 49 cents is Pennies = 4, Nickels = 0, Dimes = 2, Quarters = 1
 41 cents is Pennies = 1, Nickels = 1, Dimes = 1, Quarters = 1

Display Change in a list
=================================================================
Wallet with 100 cents: [25, 25, 25, 25]
Wallet with 91 cents: [1, 5, 10, 25, 25, 25]
Wallet with 49 cents: [1, 1, 1, 1, 10, 10, 25]
Wallet with 41 cents: [1, 5, 10, 25]

"""


def displayChange(money):
    """ Display change of the given money variable """

    # Add your code here

    print('{:>3} cents is Pennies = {}, Nickels = {}, Dimes = {}, Quarters = {}'.format(originalMoney, pennies, nickels, dimes, quarters))



def fillWallet(money):
    """ Creates and fills in a Python list with change based on the money variable """
    wallet = []

    # Add your code here

    return wallet


# ===========================================================================
# Main Code - Don't change

print('Display Change')
print('=' * 65)
displayChange(100)
displayChange(91)
displayChange(49)
displayChange(41)

print('\nDisplay Change in a list')
print('=' * 65)
print('Wallet with 100 cents:', fillWallet(100))
print('Wallet with 91 cents:', fillWallet(91))
print('Wallet with 49 cents:', fillWallet(49))
print('Wallet with 41 cents:', fillWallet(41))
