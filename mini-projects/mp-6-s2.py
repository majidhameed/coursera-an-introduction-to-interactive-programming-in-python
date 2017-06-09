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

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
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
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
         return " ".join([str(x) for x in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        value = 0
        for m in self.cards:
            value += VALUES[m.get_rank()]
        if 'A' in [m.get_rank() for m in self.cards] and value < 12:
            value += 10
        return value

    def busted(self):
        if self.get_value() > 21:
            return True
        return False
    
    #addition variable hole - if 1 first card is hidden, otherwise is visible
    def draw(self, canvas, vertical_position, hole):
        start = CARD_SIZE[1]
        for m in self.cards:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(m.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(m.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [start, vertical_position], CARD_SIZE)
            start += CARD_SIZE[1]
        if hole == 1:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_SIZE[1], vertical_position], CARD_BACK_SIZE)

 
        
# define deck class
class Deck:
    def __init__(self):
        self.deck = [Card(i,j) for i in SUITS for j in RANKS]
        self.shuffle()
        
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)	
        
    def deal_card(self):
        return self.deck.pop()

#define event handlers for buttons
def deal():
    global in_play, dealer_hand, player_hand, deck, message, score
    # your code goes here
    if in_play == True:
        score -= 1
    dealer_hand = Hand()
    player_hand = Hand()
    deck = Deck()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    message = ''
    in_play = True

def hit():
    global score, in_play, dealer_hand, player_hand, deck, message
    if in_play:
        player_hand.add_card(deck.deal_card())

        if player_hand.busted():
            in_play = False
            message = 'You have busted! You lose!'
            score -= 1
        else:
            if player_hand.get_value() == 21:
                stand()
    
    # if busted, assign an message to outcome, update in_play and score        
        
def stand():
    global score, in_play, dealer_hand, player_hand, deck, message
    if in_play:
        in_play = False
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if  dealer_hand.get_value() > 21:
            message = 'I have busted! You win!'
            score += 1
        else:
             if dealer_hand.get_value() >= player_hand.get_value():
                    message = 'You lose!'
                    score -= 1
             else:
                    message = 'You win!'
                    score += 1

# draw handler    
def draw(canvas):
    global message
    
    #BLACKJACK SIGN
    canvas.draw_line((0, 30), (600, 30), 60, "Black")
    canvas.draw_line((0, 60), (600, 60), 1, "White")
    for i in range(9):
        canvas.draw_text("BLACKJACK"[i], (130+40*i,40), 30, "White")
   
    #Drawing for the player
    canvas.draw_text("Player's hand", (250, 560), 17, "White")
    canvas.draw_text("(value: "+ str(player_hand.get_value()) + ")", (268, 580), 14, "White")
    player_hand.draw(canvas,480,0)
    
    #Drawing for the dealer & messages dependent on in_play
    canvas.draw_text("Dealer's hand", (250, 90), 17, "White")    
    if in_play:
        dealer_hand.draw(canvas,180,1)
        canvas.draw_text("Hit or stand?", (180, 360), 17, "White")
    else:
        dealer_hand.draw(canvas,180,0)
        canvas.draw_text("(value: "+ str(dealer_hand.get_value()) + ")", (268, 115), 14, "White")
        canvas.draw_text(message, (180, 320), 17, "White") #result message
        canvas.draw_text("New deal?", (180, 360), 17, "White")
        
    #The rest - score & deck
    for m in range(100,120,2):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [m,330], CARD_BACK_SIZE)
    canvas.draw_text("Score:", (520, 300), 15, "White")
    canvas.draw_text(str(score), (542, 330), 15, "White")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
deal()
frame.start()
