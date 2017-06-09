# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# import necessary modules
import simplegui
import random
import math

# initialize global variables used in your code
# variable num_range needs to be initialized to set the start condition range
num_range = 100

# helper function to initialize game
# runs when the program starts and again whenever a new game starts
# calculates a new secret number
# and the starting number of guesses left based on the range
# prints the starting message

def init():
    global secret_number
    global guesses_left
    secret_number = random.randrange(0,(num_range))
    guesses_left = math.ceil(math.log((num_range + 1), 2)) 
    print "New game. Range is from [0 to", str(num_range) + ")"
    print "Number of remaining guesses is", guesses_left

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts the game
    global num_range
    num_range=100
    print""
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts the game
    global num_range
    num_range=1000
    print""
    init()
    
def get_input(guess):
    # main game logic goes here
    global guesses_left
    
    # convert guess from a str to a float
    guess = float(guess)
    
    #decrement guesses_left
    guesses_left = guesses_left - 1
        
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is", guesses_left
    
    # restart if guess is correct
    if guess == secret_number:
        print "Correct!"
        print""
        init()
        
    # restart if no guesses remain
    elif guesses_left == 0:
        print "The secret number was", secret_number
        print "Sorry, you are out of guesses." 
        print ""
        init()
        
    # Give a hint and prompt user for another guess  
    else:
        
        if secret_number > guess:
            hint = 'Higher'
        else:
            hint = 'Lower'
                
        print hint

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
init()

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# start frame
f.start()

# always remember to check your completed program against the grading rubric
