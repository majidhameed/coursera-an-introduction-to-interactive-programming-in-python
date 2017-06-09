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
message = ""
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
        return " ".join([str(card) for card in self.cards])
        
    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        hand_value, num_aces = 0, 0
        # add up card values and count the number of aces
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                num_aces += 1
                        
        if num_aces > 0 and hand_value + 10 <= 21:
            return hand_value + 10
        
        return hand_value
        
    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, pos, start = 0):
        for card in self.cards[start:]:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 10
 
        
# define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self, hand):
        if not self.cards:
            print "Deck is empty"
        
        hand.add_card(self.cards.pop())
    
    def __str__(self):
        return " ".join([str(card) for card in self.cards])


#define event handlers for buttons
def deal():
    global message, in_play, player, dealer, deck, score
    
    if in_play:
        score -= 1
        
    deck = Deck()
    deck.shuffle()
    
    player, dealer = Hand(), Hand()
    deck.deal_card(player)
    deck.deal_card(player)
    deck.deal_card(dealer)
    deck.deal_card(dealer)
    
    message = "Hit or stand?"
    in_play = True

    
def hit():
    global in_play, message    
    if not in_play:
        message = "Click deal for new hands"
        return
    
    # if the hand is in play, hit the player
    global deck, player, score
    deck.deal_card(player)        
    
    # if busted, assign an message to outcome, update in_play and score
    if player.busted():
        message = "You went busted and lost."
        score -= 1
        in_play = False 
    
    
def stand():
    global in_play, message
    if not in_play:
        message = "Click deal for new hands"
        return
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global deck, dealer, score
    while dealer.get_value() < 17:
        deck.deal_card(dealer)
    
    # assign a message, update in_play and score
    if dealer.busted():
        message = "Dealer went busted. You won!"
        score += 1
    elif player.get_value() > dealer.get_value():
        message = "You won!"
        score += 1
    else:
        message = "You lost."
        score -= 1
    
    in_play = False
    
    
# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [100, 100], 36, "White")
    canvas.draw_text("Dealer", [50, 160], 24, "Black")
    canvas.draw_text("Player", [50, 380], 24, "Black")                 
    canvas.draw_text("Score " + str(score), [350, 570], 24, "Red")
    
    canvas.draw_text(message, [175, 330], 24, "Black")
    
    player.draw(canvas, [50, 400])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_CENTER[0], 180 + CARD_CENTER[1]], CARD_SIZE)
        dealer.draw(canvas, [50 + CARD_SIZE[0] + 10, 180], 1)
    else:
        dealer.draw(canvas, [50, 180])
        canvas.draw_text("New deal?", [175, 360], 24, "Black")


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
