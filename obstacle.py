# File: obstacle.py
#
# This program will print the left and right values from the robot's
# obstacle sensor. The program will run for 30 seconds.

from finch import Finch
from time import time, sleep

tweety = Finch()

# Define a function that can tell us if the Finch sees an obstacle. It
# will return True if it senses at least one obstacle and False if it
# senses no obstacles.
def is_blocked():
    # Get our current acceleration status.
    left_obstacle, right_obstacle = tweety.obstacle()

    print("%-5s %-5s" % (left_obstacle, right_obstacle))

    return left_obstacle or right_obstacle

# get the current time, in seconds
start_time = time()

# This loop condition takes the current time and subtracts the start time,
# giving the elapsed time in seconds. So this loop will keep looping until it
# has been 30 seconds since the start time.
while time() - start_time < 30:
    if is_blocked():
        tweety.led(255, 0, 0)
    else:
        tweety.led(0, 255, 0)

    sleep(0.1)

tweety.close()
