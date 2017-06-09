# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize global variables
in_play = False
message = ""
score = 0

# globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if in_play == True:	
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [37.5 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.inventory = []
        
    def __str__(self):
        s = str(self.inventory)
        return s
    
    def add_card(self, card):
        self.inventory.append(str(card))
        
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        Ace = False # sets check on Aces to false
        i = 0 # used to increment thro the list
        v = 0 # sets vaule to 0

        while i < len(self.inventory): #repeats for each card in the list
            # print self.inventory # use to print inventory for manual check
            # print self.inventory[i] # use to print item in list dependant on i (e.g 0 to 3)
            x = self.inventory[i] # assigns temp variable to next item in the list
            if x[1] == 'A': # this is looking at the 2nd letter of the list item and if A sets variable to true
                Ace = True
            # print Ace # use to test the Ace sense if statement
            temp = x[1] # sets the 2nd chr of the list item and assigns temp variable
            # print temp # use to test temp value is correct
            v = v + VALUES.get(temp) # gets and sums the values of the cards 
            # print v # use to test the sum of the vaules
            i = i + 1

        if Ace == False: # if there are no Aces
            v = v #  returns the sum of the cards vaules
        else: # if there are Aces
            if v + 10 <=21: # checks if an Ace is 11 if it will be over 21
                v = v + 10 # if it isn't adds 10 to the vaule (i.e. Ace == 11)
            else:
                v = v # otherwise returns the sum of card value with Ace counted as 1
        return v
            
    def draw(self, canvas, p):
        # card = Card("S", "5") # use to test with line below
        # card.draw(canvas, [37, 150])
        s = self.inventory
        # print s # use to test s
        position = [37, p]
        # print position # use to test position
        i = 0
        while i < len(self.inventory):
            # print i # use to test iteration
            ci = str(s[i])
            # print ci[0] # use to test the suit of the card is read
            # print ci[1] # use to test the value of the card is read
            card = Card(ci[0], ci[1]) # assigns the local vaiable card with the Card instance where ci[0] is the suit and ci[1] is the vaule
            card.draw(canvas, position)
            position[0] = position[0] + 100 # update the position so next card is moved to the right
            i = i + 1 
     
# the deck class, shuffle and deal cards in deck
class Deck:
    def __init__(self,):
        self.inventory = []
       
    # adds cards back to the deck and shuffles
    def shuffle(self, SUITS, RANKS):
        self.inventory = [suit+rank for suit in SUITS for rank in RANKS]
        random.shuffle(self.inventory)
        
    def deal_card(self, p):
        p.add_card(self.inventory.pop(0))
    
    def __str__(self):
        print self.inventory

# the deal button, deals the plahyers and dealers initial hands
def deal():
    global outcome, in_play, player, dealer, pack, message, score
    if in_play == True:
        score = score -1
    message = " " # resets the message for new deal
    in_play = True # The game is now being played
    pack = Deck()
    pack.shuffle(SUITS, RANKS)
    player = Hand()
    dealer = Hand()
    
    i = 2 # used to deal 2 cards
    while i > 0:
        pack.deal_card(dealer)
        pack.deal_card(player)
        i = i - 1
        # if i == 0: # use the if/print statement to check the hands have been created correctly
            # print "Dealers hand is " + str(dealer)
            # print "Players hand is " + str(player)
    message = "Hit or stand?"
    #return
    
# the hit button, adds to the players hand until stand() or bust
def hit():
    global in_play, score, message
    # if the hand is in play, hit the player
    if in_play == True:
        if player.get_value() <= 21:
            # print "hand is " + str(player.get_value()) # use to test player.get_value
            pack.deal_card(player)
            # print player.get_value()
        if player.get_value() >= 22:
            message = "You are busted. The dealer has won. New deal?"
            score = score -1
            in_play = False
    # in_play = False

# the stand button, once player stands adds to the dealers hand until value > 17,
# then checks who won.
def stand():
    global in_play, score, message
    if player.get_value() >= 22:
        message = "You are BUSTED!!! The dealer won.  New deal?"
        in_play = False
    # if in play and the dealer's hand is below 17 give the hand another card
    if in_play == True:
        while dealer.get_value() < 17:
            #print "hand is " + str(dealer.get_value()) # use to test dealer.get_value
            pack.deal_card(dealer)
            # print "The dealer's hand is " + str(dealer.get_value())
        if dealer.get_value() > 21:
            message = "The dealer is bust!!! You win. New deal?"
            score = score +1
            in_play = False 
        elif dealer.get_value() > player.get_value():
            message = "The dealer wins. New deal?"
            score = score -1
            in_play = False
        elif dealer.get_value() == player.get_value():
            message = "Tie! The dealer wins ties. New deal?"
            score = score -1
            in_play = False
        else:
            message = "You win."
            score = score +1
            in_play = False 

# draw handler    
def draw(canvas):
    canvas.draw_text("BlackJack", (200, 50), 40, "White")
    canvas.draw_text("Score:", (37.5, 90), 20, "White")
    canvas.draw_text(str(score), (130, 90), 20, "White")
    canvas.draw_text("Dealer's hand", (37.5, 130), 20, "White")
    dealer.draw(canvas, 150)
    canvas.draw_text("Player's hand", (37.5, 330), 20, "White")
    player.draw(canvas, 350)
    canvas.draw_text(message, (37.5, 500), 20, "White")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()

# get things rolling
frame.start()

# The End - Boy! This was tough...