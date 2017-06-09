# implementation of card game - Memory

import simplegui
import random

moves = 0

# helper function to initialize globals
def init():
    global deck
    global exposed
    global state
    global moves
    
    deck = [i//2 for i in range(16)]
    random.shuffle(deck)
    exposed = [False for c in deck]
    state = 0
    moves = 0
    l.set_text("Moves = " + str(moves))
    

     
# define event handlers
def mouseclick(pos):
    global exposed 
    global moves
    global state
    global previous1
    global previous2
    card_index = pos[0] // 50
   
    
    if state == 1:
        if exposed[card_index] == False:
            exposed[card_index] = True
            previous2 = card_index
            state = 2
    
    elif state == 2:
        if exposed[card_index] == False:
            exposed[card_index] = True
            if deck[previous1] != deck[previous2]:
                exposed[previous1] = False
                exposed[previous2] = False
            previous1 = card_index
            state = 1
            moves += 1
            l.set_text("Moves = " + str(moves))
        
    
    elif state == 0:
        if exposed[card_index] == False:
            exposed[card_index] = True
            previous1 = card_index
            state = 1  
    
    print (state) 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    horiz = 0
    for x in range(len(deck)):
        if exposed[x] == True:
            canvas.draw_text(str(deck[x]),[horiz + 5, 80], 60, "White")
        else:
            canvas.draw_polygon([(horiz + 2, 2), (horiz + 48, 2), (horiz + 48, 98), (horiz + 2, 98)], 4, "White", "Green")
        horiz += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
l=frame.add_label("Moves = 0")

# get things rolling
init()
frame.start()



# Always remember to review the grading rubric