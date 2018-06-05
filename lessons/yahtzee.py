import random

# ------------------------------------------------------------
# This function will count the number of tries it takes to get
# a yahtzee (ie., 5 of a kind)
# https://en.wikipedia.org/wiki/Yahtzee
# ------------------------------------------------------------
def getYahtzee():
    tries = 0
    yahtzee = False

    # While we don't have a Yahtzee, keep trying
    while (not yahtzee):

    	# Do 5 rolls of a die
        rolls = []
        for i in range(5):
        	rolls.append(random.randint(1, 6))
        
        # Create a list to count the number of each roll
        count = [0, 0, 0, 0, 0, 0]
        for r in rolls:
            count[r - 1] += 1

        # Keep track on the number of tries we do
        tries += 1

        # Do we have 5 of a kind in the count list (True or False)?
        yahtzee = (5 in count)

    print('   Yahtzee tries:', tries)
    return tries


# ------------------------------------------------------------
# Number of rolls to get a large straight
# 12345 or 23456
# ------------------------------------------------------------
def largeStraight():
    tries = 0
    straight = False

    # While we don't have a straight, keep trying
    while (not straight):

    	# Do 5 rolls of a die
        rolls = []
        for i in range(5):
        	rolls.append(random.randint(1, 6))
        
        # Keep track on the number of tries we do
        tries += 1

        # Do we have 5 in a row
        oneToFive = ((rolls[0] == 1) and (rolls[1] == 2) and (rolls[2] == 3) and
					(rolls[3] == 4) and (rolls[4] == 5))
        twoTosix = ((rolls[0] == 2) and (rolls[1] == 3) and (rolls[2] == 4) and
					(rolls[3] == 5) and (rolls[4] == 6))

        straight =  oneToFive or twoTosix

    print('   large straight tries:', tries)
    return tries


# ------------------------------------------------------------
# Main code
# ------------------------------------------------------------

Yahtzees = []
lStraight = []
for i in range(1000):
    print('Run:', i)
    Yahtzees.append(getYahtzee())
    lStraight.append(largeStraight())

print('\nResults')
print('Yahtzees')
print('min = ', min(Yahtzees))
print('max = ', max(Yahtzees))
print('avg = ', sum(Yahtzees) / len(Yahtzees))

print('')
print('Large Straights')
print('min = ', min(lStraight))
print('max = ', max(lStraight))
print('avg = ', sum(lStraight) / len(lStraight))
