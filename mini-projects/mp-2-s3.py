# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


# initialize global variables used in your code
import simplegui
import math
import random
computer_number = random.randrange (0,100)
guess_chances = math.ceil(math.log(101)/math.log(2))
current_range = 100

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global computer_number
    global guess_chances
    global current_range
    computer_number = random.randrange (0,100)
    guess_chances = math.ceil(math.log(101)/math.log(2))
    current_range = 100
    print "Guess the number, from 0 to 100."
    print "You have " + str(guess_chances) + " chances!"
    print ""
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global computer_number
    global guess_chances
    global current_range
    computer_number = random.randrange (0,1000)
    guess_chances = math.ceil(math.log(1001)/math.log(2))
    current_range = 1000
    print "Guess the number, from 0 to 1000."
    print "You have " + str(guess_chances) + " chances!"
    print ""

def select_range():
    if current_range == 1000:
        range1000()
    elif current_range == 100:
        range100()
    
def get_input(guess):
    
    # main game logic goes here
    global guess_chances
    guess_chances = guess_chances - 1
    player_number = int(guess)
    
    if player_number == computer_number:
        print "Correct!"
        print ""
        print ""
        select_range()
    elif player_number != computer_number and guess_chances == 0:
        print "Sorry, the correct number was " + str(computer_number) + "."
        print ""
        print ""
        select_range()
    elif player_number > computer_number and guess_chances > 0:
        print "Lower!"
        print "You have " + str(guess_chances) + " more chances."
    elif player_number < computer_number and guess_chances > 0:
        print "Higher!"
        print "You have " + str(guess_chances) + " more chances."
    print ""
    
# create frame
f = simplegui.create_frame("Test",200,200)

# register event handlers for control elements
f.add_button("Range from 0 to 100", range100, 200)
f.add_button("Range from 0 to 1000", range1000, 200)
f.add_input("Player Guess",get_input,200)

# start frame
f.start()
print "Guess a number, from 0 to 100."
print "You have " + str(guess_chances) + " chances!"
print ""

# always remember to check your completed program against the grading rubric
