# Turn a Finch robot into a "Magic 8"-Finch.
#
# Ask a question, flip the Finch upside down, and get an answer.
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


# ======================================================================
# Define a function called "is_upside_down" that can tell us if the
# Finch is updside-down. It will return True if it is updside-down and
# False if it is not.
# (Hint: Delete the line that says "pass". The pass statement does
# nothing; it's there because we have an "def" function declaration on
# the previous line, and Python requires us to have at least one
# indented line after every if, else, while, for, or def statement.)
# (Second hint: You'll need to use the acceleration function. The Finch
# is upside-down when the value of x is between -0.7 and 0.7, the value
# of y is between -0.7 and 0.7, and the value of z is less than -0.7.)
# ======================================================================
def is_upside_down():
    # Get our current acceleration status.
    x, y, z, tap, shake = tweety.acceleration()

    # Calculation is based on x, y and z.
    return x > -0.7 and x < 0.7 and y > -0.7 and y < 0.7 and z < -0.7


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
    if is_upside_down():
        # ==============================================================
        # Turn the LED green to hint to the user that we're upside-down
        # and ready to print an answer.
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

# ======================================================================
# This is the really hard part:
# You may have noticed that the code above, once you get it working,
# prints a whole bunch of answers when you turn the robot upside-down.
# Ideally, you want it to print just one answer the first moment we
# detect that the user flipped us upside-down. Then, we don't want to
# print another answer until we can tell that the user has flipped us
# right-side up and then upside-down again.
#
# What you need to do is remember if we were upside down the last time
# the loop ran or not.
#
# Here's another way to think about it:
# This program has a loop that runs over and over again. Each time the
# loop runs, we need to know two things to tell us what to do:
# (1) Are we upside-down right now?
# (2) Were we upside-down the last time the loop ran?

# You need to create a variable to track our state across multiple
# executions of the loop. It will remember if we were upside down the
# last time the loop ran or not. We want to print our answer the first
# moment we detect that the user flipped us upside-down. Then, we don't
# want to print another answer until we can tell that the user has
# flipped us right-side up and then upside-down again.
# ======================================================================
