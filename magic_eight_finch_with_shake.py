"""
Turn a Finch robot into a "Magic 8"-Finch.

Ask a question, shake the Finch, and flip it upside down, and get an
answer.

The Finch is a robot for computer science education. Its design is the
result of a four year study at Carnegie Mellon's CREATE lab.

http://www.finchrobot.com
"""
# Imports from standard Python libraries.
from random import randrange
from time import sleep

# Import from the special Finch robot library.
from finch import Finch

# Many possible ways to answer user questions.
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

# Always the first step: Create a Finch object we can use.
tweety = Finch()

# Tell the user how to use our program.
print('I\'m a "Magic 8"-Finch!'
      '\n\nAsk me a question, shake me, and turn me upside down to get '
      'your answer.')

# Create the variables we will use to track our state across multiple
# executions of the loop:

# Track which answer we should print.
answer_index = 0

# Remember if we were upside down the last time the loop ran or not. We
# want to print our answer the first moment we detect that the user
# flipped us upside down. Then, we don't want to print another answer
# until we can tell that the user has flipped us right-side up and then
# upside down again.
was_upside_down_before = False

# Track if we've encountered an obstacle (like if the user waves a hand
# in front of the beak). Note we are also initializing them with real
# data with a call to the obstacle function.
left_obstacle, right_obstacle = tweety.obstacle()

while not left_obstacle and not right_obstacle:
    # Get our current acceleration status.
    x, y, z, tap, shake = tweety.acceleration()

    if x > -0.5 and x < 0.5 and y > -0.5 and y < 0.5 and z < -0.7:
        # Based on x, y and z, we're now upside down.

        # Green LED (hints to the user that we're upside down and ready
        # to print an answer).
        tweety.led(0, 255, 0)

        if not was_upside_down_before:
            # If we weren't upside down already, that means the user
            # *just* flipped us upside down, so take action!

            # Print the answer.
            print(answers[answer_index])
            
            # Remember that we're already upside down for the next time
            # we check.
            was_upside_down_before = True
    else:
        # Based on x, y and z, we're *not* upside down.

        # Red LED (hints to the user that we're right-side up and not
        # ready to print an answer).
        tweety.led(255, 0, 0)

        # Remember that we turned right-side up again.
        was_upside_down_before = False

        if shake:
            # If we're not upside-down, and the user shook us, then
            # change which answer we're going to print.
            answer_index = randrange(0, len(answers))

            # Beep to let the user know we sensed the "shake".
            tweety.buzzer(0.1, 440)

    # If we sense obstacles, then it's time to close.
    left_obstacle, right_obstacle = tweety.obstacle()

# Let the user know the program has ended.
print('Thanks for playing. Goodbye!')

# Always the last step: Close the connection to our Finch to keep
# it happy.
tweety.close()
