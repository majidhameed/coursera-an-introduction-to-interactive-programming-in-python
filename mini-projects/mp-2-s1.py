# "Guess the number" (PA2)
# 10-24-2012

import simplegui
import random
import math

# initialize global variables used in your code
secret_num = 0 # the number to guess
count = 0      # the number of attempts
low = 0	       # the range of the secret num
high = 100
limits = 0     # the total number of guesses allowed

# define helper functions
def init():
    """ start a new game """
    global count, secret_num, limits
    secret_num = random.randrange(low,high)
    count = 0
    limits = math.ceil(math.log(high-low,2))
    print "New Game! Range is from " + str(low) + " to " + str(high)
    print "Number of remaining guesses is " + str(limits-count) + "\n"
    
    
# define event handlers for control panel    
def range100():
    """ button that changes range to range [0,100) and restarts """
    global high
    high = 100
    init()

def range1000():
    """ button that changes range to range [0,1000) and restarts """
    global high
    high = 1000
    init()
    
def get_input(guess):
    """ fetch the guess and proceed the game """
    global count
    count += 1
    guess_num = int(guess)
    print "Guess was " + guess
    if count == limits:
        if guess_num == secret_num:
            print "Correct! Congrats! \n"
        else:
            print "Sorry! Reached the limits of guesses."
            print "The correct answer is " + str(secret_num) + "\n"
        init()
    else:
        print "Number of remaining guesses is " + str(limits-count)
        if guess_num == secret_num:
            print "Correct! Congrats! \n"
            init()
        elif guess_num < secret_num:
            print "Higher!"
            if guess_num < low:
                print "! Range is from " + str(low) + " to " + str(high) + "\n"
            else:
                print " "
        else:
            print "Lower!"
            if guess_num > high:
                print "! Range is from " + str(low) + " to " + str(high) + "\n"
            else:
                print " "

# create frame
frame = simplegui.create_frame("Guess the number!", 500, 500)

# register event handlers for control elements
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range {0,1000)", range1000, 200)
frame.add_input("Type in your guess", get_input, 200)

# start frame
frame.start()
init()

