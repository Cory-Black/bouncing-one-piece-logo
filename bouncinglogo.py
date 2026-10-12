"""The Bouncing One Piece Logo, by Cory R. Black (Cory.r.black@icloud.com)
Like the bouncing DVD logo animation, you have to be "of a certain age" to 
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal windon while this program is running."""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can installl by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

#Setting up constants:
width, height = bext.size()

#We can't print to the last column in windows without it adding a
#newline automatically, so we reduce the width by one:
width -= 1

number_of_logos = 5
pause_amount = 0.2

#creating a list of colors for the logo:
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

#creating directions for logo to move in:
up_right = 'ur'
up_left = 'ul'
down_right = 'dr'
down_left = 'dl'
directions = (up_left, up_right, down_left, down_right)

#Key names for logo dictionaries:
color = 'color'
X = 'x'
Y = 'y'
Dir = 'direction'

def main():
    bext.clear()

    #Generate some logos:
    logos = []
    for i in range(number_of_logos):
        logos.append({color: random.choice(colors),
                      X: random.randint(1, width - 4),
                      Y: random.randint(1, height - 4),
                      Dir: random.choice(directions)})

        #Making sure X is even so it can hit the corner:
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    #Counter to keep track of the amount of times a logo hits the corner:
    cornerBounces = 0

    #Main program loop:
    while True:

        #Handling each logo in the logos list:
        for logo in logos:

            #Erasing the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('         ', end= '')

            originalDirection = logo[Dir]

            #Check if logo bounced off corner:
            if logo[X] == 0 and logo[Y] == 0:
                logo[Dir] = down_right
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == height - 1:
                logo[Dir] = up_right
                cornerBounces += 1
            elif logo[X] == width - 9 and logo[Y] == 0:
                logo[Dir] = down_left
                cornerBounces += 1
            elif logo[X] == width - 9 and logo[Y] == height - 1:
                logo[Dir] = up_left
                cornerBounces += 1

            #Checking if logo bounced off the left edge:
            elif logo[X] == 0 and logo[Dir] == up_left:
                logo[Dir] = up_right
            elif logo[X] == 0 and logo[Dir] == down_left:
                logo[Dir] = down_right

            #Checking if logo bounced off the right edge:
            #(width - 9 because 'One Piece' has 9 characters.)
            elif logo[X] == width - 9 and logo[Dir] == up_right:
                logo[Dir] = up_left
            elif logo[X] == width - 9 and logo[Dir] == down_right:
                logo[Dir] = down_left

            #Checking if logo bounced off top edge:
            elif logo[Y] == 0 and logo[Dir] == up_left:
                logo[Dir] = down_left
            elif logo[Y] == 0 and logo[Dir] == up_right:
                logo[Dir] = down_right

            #Checking if logo bounced off bottom edge:
            elif logo[Y] == height - 1 and logo[Dir] == down_right:
                logo[Dir] = up_right
            elif logo[Y] == height - 1 and logo[Dir] == down_left:
                logo[Dir] = up_left

            #Change color when logo bounces:
            if logo[Dir] != originalDirection:
                logo[color] = random.choice(colors)

            #Move the logo. (X moves by 2 because the terminal
            #characters are twice as tall as they are wide.)
            if logo[Dir] == up_right:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[Dir] == up_left:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[Dir] == down_right:
                logo[X] += 2
                logo[Y] += 1
            elif logo[Dir] == down_left:
                logo[X] -= 2
                logo[Y] += 1

        #Display number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        #Drawing logos in their new locations:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[color])
            print('One Piece', end= '')

        bext.goto(0, 0)

        #Required for bext-using programs:
        sys.stdout.flush()
        time.sleep(pause_amount)

#If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing One Piece logo, by Cory R. Black')

        #Pressing Ctrl-C ends the program:
        sys.exit()
