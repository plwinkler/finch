# Turn a Finch robot into a "Magic 8"-Finch.
#
# Ask a question, flip the Finch upside down, and get an answer.
#
# The Finch is a robot for computer science education. Its design is the
# result of a four year study at Carnegie Mellon's CREATE lab.
#
# http://www.finchrobot.com

# Imports from standard Python libraries.
from random import choice
from time import sleep

# Import from the special Finch robot library.
from finch import Finch


# Always the first step: Create a Finch object we can use.
tweety = Finch()


# Next, we have to create a list of possible ways to answer user
# questions. The answers below are from a standard Magic 8 Ball.
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
    "Don\'t count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",    
]


# Create the variables we will use to track our state across multiple
# executions of the loop:

# Remember if we were upside down the last time the loop ran or not. We
# want to print our answer the first moment we detect that the user
# flipped us upside-down. Then, we don't want to print another answer
# until we can tell that the user has flipped us right-side up and then
# upside-down again.
upside_down_counter = 0
right_side_up_counter = 0


# This program has a loop that runs over and over again. Each time the
# loop runs, we need to know two things to tell us what to do:
# (1) Are we upside-down right now?
# (2) Were we upside-down the last few times the loop ran?
# Define a function that can tell us if the Finch is updside-down. It
# will return True if it has officially just turned updside-down and
# False if it is right-side up or if it was already upside-down.
def just_turned_upside_down():
    # Get our current acceleration status.
    x, y, z, tap, shake = tweety.acceleration()

    global upside_down_counter, right_side_up_counter
    # Calculation is based on x, y and z.
    if x > -0.7 and x < 0.7 and y > -0.7 and y < 0.7 and z < -0.7:
        upside_down_counter = upside_down_counter + 1
        if upside_down_counter >= 5:
            right_side_up_counter = 0
            # Turn the LED green to hint to the user that we're upside-down
            # and ready to print an answer.
            tweety.led(0, 255, 0)
    else:
        right_side_up_counter = right_side_up_counter + 1
        if right_side_up_counter >= 5:
            upside_down_counter = 0
            # Turn the LED red to hint to the user that we're right-side up
            # and not ready to print an answer.
            tweety.led(255, 0, 0)
    return upside_down_counter == 5


# Define a function called "not_blocked" that can tell us if the Finch
# is not blocked by an obstacle. It will return True if no obstacles are
# detected and False if one or more obstacles are detected.
def not_blocked():
    left_obstacle, right_obstacle = tweety.obstacle()
    return not left_obstacle and not right_obstacle


# Print a message to tell the user how to use our program.
print("I'm a Magic 8 Finch!")
print("Ask me a question and turn me upside down to get your answer.")


while not_blocked():
    if just_turned_upside_down():
        # Choose an answer randomly.
        answer = choice(answers)

        # Print the answer.
        print(answer)

    # Sleep for one tenth of a second before restarting the loop. This
    # means we will run through this loop ten times each second.
    sleep(0.1)


# Print a message to let the user know the program has ended.
print("Thanks for playing. Goodbye!")


# Always the last step: Close the connection to our Finch to keep
# it happy.
tweety.close()
