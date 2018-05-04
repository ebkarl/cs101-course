![](../images/cs101.png)
***

# 06 - Project : Number Guessing Game

# 0 - Setup

The following project will require you write and run your own Python code.  There are a number of ways to do this.

- Thonny on your computer.
- Online sites such as https://www.pythonanywhere.com/ or https://www.trinket.io/.  You are able to create free accounts on these websites.
- You are free to write your project in either version 2 or 3 of Python. However, I would prefer you write your project using Python 3.  Just remember what the differences are between version 2 and 3.


# 1 - Objectives

- Using loops and if statements.
- Using the random() function.

# 2 - Overview

This project will implement a number guessing game.  
- Your project will generate a random number that the user of your program will need to guess.  
- The program will tell the user if the guess is too high or too low.  
- The program will continue until the number is guessed.
- When the number if guessed, the program will display the number of guesses that it took to find the number.
- You will be required to use the Python random() function to generate random numbers. 

## How to generate a random number

Below is a example of using the random() function in Python 3.

```python
import random
n = random.randint(1, 3)
guess = int(input('Enter an integer from 1 to 3: '))
if guess == n:
    print('You Guessed It')
else:
    print('You Missed It')
```

# 3 - Instructions

## 3.1 - Sample Output

Here is sample output of your project.

```
Enter an integer from 1 to 100: 34
Guess too low
Enter an integer from 1 to 100: 60
Guess too low
Enter an integer from 1 to 100: 9
Guess too low
Enter an integer from 1 to 100: 99
Guess too high
Enter an integer from 1 to 100: 80
Guess too low
Enter an integer from 1 to 100: 85
Guess too high
Enter an integer from 1 to 100: 83
Guess too high
Enter an integer from 1 to 100: 82
You took 8 guesses
```

## 3.2 - Your Project

For your project, please keep the following in mind:
- Use the random() function to generate a random value between 1 and 100.
- Use a variable to keep track of the number of guesses that are taken.
- You will need to use a loop.


# 4 - Submitting

After you have finished writting and testing your program:

1. Take a screen shot of your code and the results of running your code.  You should be able to do this in one screen shot.  If not, take screen shots of each.
2. Upload your screen shot image(s) to the Assignment Section in I-Learn for the course.  You will find an item for this project.
