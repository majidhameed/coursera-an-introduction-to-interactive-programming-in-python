# Mini-Project-5
# Implementation of Card Game - Memory

import simplegui
import random

CARD_HORIZONTAL_SPACE = 50
BORDER_COLOR = "Red"; BORDER_LINE_WIDTH = 0.5
HIDE_BG_COLOR = "Green"; VISIBLE_BG_COLOR = "Black"


# helper function to initialize globals
def init():
    global cards, exposed, state, moves, card1, card2
    
    state = 0; moves = 0
    card1 = None; card2 = None
    
    l.set_text('Moves = ' + str(moves))
    
    cards = [i for i in range(8)] + [i for i in range(8)]
    random.shuffle(cards)
    
    # initially no cards exposed
    exposed = [False for x in range(16)]
    
     
# define event handlers
def mouseclick(pos):
    global state, card1, card2, moves
    
    print '\nprevious state:', state
    exposed_index = pos[0]//50
    if exposed[exposed_index] == True:
        print "Card already exposed ignoring"
        return
    exposed[exposed_index] = True
    #State 0 - Start of the Game
    if state==0:
        card1 = exposed_index
        state = 1
    #State 1 - Single exposed Unpaired Card  
    elif state==1:
        card2 = exposed_index
        state = 2
    #State 2 - End of Turn
    else:
        print "Cards:", cards[card1], cards[card2]
        if cards[card1]==cards[card2]:
            print "Paired"
        else:
            print "UnPaired, Flip them back over" 
            exposed[card1] = False
            exposed[card2] = False
        #update moves/turn_counter
        moves += 1
        l.set_text('Moves = ' + str(moves))
        card1 = exposed_index
        state = 1
    print 'current state:', state

    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    # draw cards
    x = 0
    for i in range(16):
        # card not visible
        canvas.draw_polygon([(x, 0), (x + CARD_HORIZONTAL_SPACE-BORDER_LINE_WIDTH, 0), (x + CARD_HORIZONTAL_SPACE-BORDER_LINE_WIDTH, 100), (x, 100), (x, 0)], BORDER_LINE_WIDTH, BORDER_COLOR, HIDE_BG_COLOR)
        # card visible
        if exposed[i]:
            canvas.draw_polygon([(x, 0), (x + CARD_HORIZONTAL_SPACE-BORDER_LINE_WIDTH, 0), (x + CARD_HORIZONTAL_SPACE-BORDER_LINE_WIDTH, 100), (x, 100), (x, 0)], BORDER_LINE_WIDTH, BORDER_COLOR, VISIBLE_BG_COLOR)
            canvas.draw_text(str(cards[i]), (x+5, 70), 50, "White")
        x+=CARD_HORIZONTAL_SPACE
        
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric