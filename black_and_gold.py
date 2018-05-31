"""
This file plays one song. Just one song. The only song that matters: The
College of Wooster fight song "Black and Gold"!Plays a list of songs.
Input 1 to play the song, 2 to quit. (But really, why wouldn't you want
to just keep playing "Black and Gold", over and over again, forever?)

Uses notes.py, an add-on library that simplifies buzzer song creation.
Thanks to Justas Sadvecius for the library!

The Finch is a robot for computer science education. Its design is the
result of a four year study at Carnegie Mellon's CREATE lab.

http://www.finchrobot.com
"""

from finch import Finch
import notes

# Main function for the music player example program.

# Initialize the finch.
finch = Finch()

black_and_gold = (
    'C6       A5   G   F  GA           '
    'C6       A5   G  FBb           '
    'A  GF#   G   A   E   G --F       '
    'F  F#G   G  AbA   A  BbC6DCDCDCDCC--'  # Behold my awesome trill!
    'C   C       A5   G   F  GA           '
    'C6  CB5 C6 C  CB5 C6 D         --'
    'C5   F   F  GA   A  GF   F  DC  -'
    'C C# D F   D F   E   F C6CC C F '
)

song = 1
while song == 1:
    # Get value telling us if we should play song or quit.
    song = int(input(
        'Enter 1 to play The College of Wooster fight song, "Black and Gold",'
        '\nor any other character to exit: '
    ))

    if song == 1:
        notes.sing(finch, black_and_gold, 0.08)
    else:
        print('Exiting...')

finch.close()
