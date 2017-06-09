# Mini-Project-2

# Implementation of Game - Guess the number

# input will come from buttons and an input field
# all output for the game will be printed in the console

# Imports
import simplegui
import random
import math

# initialize global variables

# Default range of number
num_range = 100

# Secret Number - Computer/Player-1 guesses
secret_number = 0

# Remaining guess count for Player-2
remaining_guesses = 0

# Helper Functions

# Helper Function - It intializes Game
def init():
    '''() -> None

    Starts a new game. It is used to start or restart the game.

    '''
    
    global secret_number, remaining_guesses
    
    # Generate Random number in the selected range
    secret_number = random.randrange(0, num_range)
    
    # Set remaining_guesses to allowed_guesses
    remaining_guesses = allowed_guesses(num_range)
    
    print ''
    print 'New game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', remaining_guesses
    
# Helper Function - For calculating allowed guesses 
def allowed_guesses(num_range):
    '''(number) -> int

    Returns allowed guesses count for the given num_range

    >>> allowed_guesses(100)
    7
    >>> allowed_guesses(1000)
    10
    '''
    
    # In Binary Search we reduce the search space by half
    # In this game we have our search space either 100 or 1000
    # For 100,  math.log(100,2)  = 6.64385618977472,  so math.ceil give us 7
    # For 1000, math.log(1000,2) = 9.965784284662087, so math.ceil give us 10
    
    return math.ceil(math.log(num_range, 2))
    
# Event Handlers - For Control Panel

# Event Hander - Range100
def range100():
    '''() -> None

    Handler for the button that changes range to range [0,100), it also restarts game

    '''
    
    global num_range
    
    # Change range to 100
    num_range = 100
    
    # Restart Game
    init()
    
# Event Hander - Range1000
def range1000():
    '''() -> None

    Handler for the button that changes range to range [0,1000), it also restarts game

    '''
    
    global num_range
    
    # Change range to 1000
    num_range = 1000
    
    # Restart Game
    init()
    
# Event Handler - get_input
def get_input(guess):
    '''(str) -> None

    Handler for input. It contains the core game logic

    '''
    
    global remaining_guesses
    
    guess_number = int(guess)
    
    # NewLine before each guess
    print ''
    
    print 'Guess was', guess_number
    
    # main game logic goes here
    
    # One guess consumed
    remaining_guesses-=1
    
    print 'Number of remaining guesses is', remaining_guesses
    
    if guess_number==secret_number:
        print 'Correct!'
        # Game End - Correctly Guessed
        init() 
    elif remaining_guesses==0:
       print 'You ran out of guesses, The number was', secret_number
       # Game End - Ran out of Guesses
       init()
    elif guess_number < secret_number:
        print 'Higher!'
    elif guess_number > secret_number:
        print 'Lower!'
        
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# Add control elements and register event handlers for control elements
frame.add_button('Range is [0,100)', range100, 200)
frame.add_button('Range is [0,1000)', range1000, 200)
frame.add_input('Enter a guess', get_input, 200)

# initialize game
init()

# start frame
frame.start()