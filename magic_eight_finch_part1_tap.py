# Turn a Finch robot into a "Magic 8"-Finch.
#
# Ask a question, tap on the Finch, and get an answer.
#
# NOTE: THIS CODE DOES NOT WORK YET! IT IS INCOMPLETE!
#
# Everywhere you see ========================, you need to add some code
# to make this program work.

# Imports from standard Python libraries.
from random import choice
from time import sleep

# Import from the special Finch robot library.
from finch import Finch


# Always the first step: Create a Finch object we can use.
tweety = Finch()


# ======================================================================
# Define a function called "not_blocked" that can tell us if the Finch
# is not blocked by an obstacle. It will return True if no obstacles are
# detected and False if one or more obstacles are detected.
# (Hint: On the line that currently says "return True", instead you need
# to return the value of a statement. Think of the kind of check you
# would do in an if statement or while statement to see if we've found
# an obstacle. Everything that comes after the word "if" or "while" in
# those instances, except for the ":", is what you should return here.)
# ======================================================================
def not_blocked():
    return True


# Next, we have to create a list of possible ways to answer user
# questions. The answers below are from a standard Magic 8 Ball.
# ======================================================================
# Try adding some new answers to the list!
# ======================================================================
answers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",    
]


# ======================================================================
# Print a message to tell the user how to use our program.
# ======================================================================


while not_blocked():
    x, y, z, tap, shake = tweety.acceleration()
    if tap:
        # ==============================================================
        # Turn the LED green to hint to the user that we detected the
        # tap and we're ready to print an answer.
        # ==============================================================

        # Choose an answer randomly.
        answer = choice(answers)

        # Print the answer.
        print(answer)
    else:
        # ==============================================================
        # Turn the LED red to hint to the user that we're right-side up
        # and not ready to print an answer. (Hint: Delete the line that
        # says "pass". The pass statement does nothing; it's there
        # because we have an "else" on the previous line, and Python
        # requires us to have at least one indented line after every if,
        # else, while, for, or def statement.)
        # ==============================================================
        pass
    sleep(0.1)


# ======================================================================
# Print a message to let the user know the program has ended.
# ======================================================================


# Always the last step: Close the connection to our Finch to keep
# it happy.
tweety.close()
