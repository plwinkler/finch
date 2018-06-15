# File: acc.py
#
# This program will print the x, y, and z from the robot's accelerometer. The
# program will run for 30 seconds.

from finch import Finch
from time import time, sleep

tweety = Finch()

# Define a function that can tell us if the Finch is updside-down. It
# will return True if it is updside-down and False if it is not.
def is_upside_down():
    # Get our current acceleration status.
    x, y, z, tap, shake = tweety.acceleration()

    print("%+.02f %+.02f %+.02f %-5s %-5s" % (x, y, z, tap, shake))

    # Calculation is based on x, y and z.
    return x > -0.7 and x < 0.7 and y > -0.7 and y < 0.7 and z < -0.7

# get the current time, in seconds
start_time = time()

# This loop condition takes the current time and subtracts the start time,
# giving the elapsed time in seconds. So this loop will keep looping until it
# has been 30 seconds since the start time.
while time() - start_time < 30:
    if is_upside_down():
        tweety.led(0, 255, 0)
    else:
        tweety.led(0, 0, 0)

    sleep(0.1)

tweety.close()
