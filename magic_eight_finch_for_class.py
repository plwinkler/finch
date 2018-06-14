# Turn a Finch robot into a "Magic 8"-Finch.
#
# Ask a question, flip the Finch upside down, and get an answer.
#
# The Finch is a robot for computer science education. Its design is the
# result of a four year study at Carnegie Mellon's CREATE lab.
#
# http://www.finchrobot.com

# Imports from standard Python libraries.
from random import randrange
from time import sleep

# Import from the special Finch robot library.
from finch import Finch


# Always the first step: Create a Finch object we can use.
tweety = Finch()


# Next, we have to create a list of possible ways to answer user
# questions. The answers below are from a standard Magic 8 Ball. Try
# adding some new answers to the list!
answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.'
    'Concentrate and ask again.',
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.',    
]


# Define a function that can tell us if the Finch is updside-down. It
# will return True if it is updside-down and False if it is not.
def is_upside_down():
    return x > -0.5 and x < 0.5 and y > -0.5 and y < 0.5 and z < -0.7


# Tell the user how to use our program. The text below has two special
# characters in it that make it leave one blank line between two lines
# of text. Edit this text so it will leave four blank lines between the
# lines of text.
print('I\'m a "Magic 8"-Finch!'
      '\n\nAsk me a question, and turn me upside down to get your answer.')

# Create the variables we will use to track our state across multiple
# executions of the loop:

# Remember if we were upside down the last time the loop ran or not. We
# want to print our answer the first moment we detect that the user
# flipped us upside down. Then, we don't want to print another answer
# until we can tell that the user has flipped us right-side up and then
# upside down again.
was_upside_down_last_time = False

# Track if we've encountered an obstacle (like if the user waves a hand
# in front of the beak). Note we are also initializing them with real
# data with a call to the obstacle function.
left_obstacle, right_obstacle = tweety.obstacle()

while not left_obstacle and not right_obstacle:
    # Get our current acceleration status.
    x, y, z, tap, shake = tweety.acceleration()

    if is_upside_down():
        # Based on x, y and z, we're now upside down.

        # Green LED (hints to the user that we're upside down and ready
        # to print an answer).
        tweety.led(0, 255, 0)

        if not was_upside_down_last_time:
            # If we weren't upside down already, that means the user
            # *just* flipped us upside down, so take action!

            # Choose an answer randomly.
            answer_index = randrange(0, len(answers))

            # Print the answer.
            print(answers[answer_index])
            
            # Remember that we're already upside down for the next time
            # we check.
            was_upside_down_last_time = True
    else:
        # Based on x, y and z, we're *not* upside down.

        # Red LED (hints to the user that we're right-side up and not
        # ready to print an answer).
        tweety.led(255, 0, 0)

        # Remember that we turned right-side up again.
        was_upside_down_before = False

    # If we sense obstacles, then it's time to close.
    left_obstacle, right_obstacle = tweety.obstacle()

# Let the user know the program has ended.
print('Thanks for playing. Goodbye!')

# Always the last step: Close the connection to our Finch to keep
# it happy.
tweety.close()
