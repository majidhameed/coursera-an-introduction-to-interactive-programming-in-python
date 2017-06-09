# Mini-Project-6
# Implementation of Game - Blackjack

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
player_question = ""

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
    
    def get_str(self):
        return self.suit + self.rank
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.ace = False
        self.value = 0
    
    def __str__(self):
        str = "Hand ["
        for card in self.cards:
            str += " " + card.get_str()
        str += " ]"
        return str

    def add_card(self, card):
        self.cards.append(card)
        if (card.get_rank=='A'):
            self.ace = True
        self.value += VALUES[card.get_rank()]    

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        if self.ace==False:
            return self.value
        else:
            if self.value+10 <= 21:
                return self.value + 10
            else:
                return self.value
            
    def busted(self):
        return self.value>21
    
    def draw(self, canvas, p):
        for card in self.cards:
            card.draw(canvas, p)
            p[0] += CARD_SIZE[0]+20
 
        
# define deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]

    # add cards back to deck and shuffle
    def shuffle(self):
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        str = "Deck ["
        for card in self.cards:
            str += " " + card.get_str()
        str += " ]"
        return str


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, player_question, deck, score
    
    print "deal"

    #creates player and dealer hands
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    if in_play:
        score -= 1
    
    outcome = ""
    in_play = True

def hit():
    global outcome,score,player_question, in_play
    
    # if the hand is in play, hit the player
    if in_play==False:
        return
    
    print "hit"
    
    if player_hand.busted()==False:
        player_hand.add_card(deck.deal_card())
        
    if player_hand.busted():
        outcome = "Player busted. You(Player) Lose"
        if in_play:
            score += -1
            in_play=False
        
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global outcome, score, player_question, in_play
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    
    if in_play==False:
        return
    
    print "stand"
    
    if player_hand.busted():
        outcome = "You(Player) busted"
        score += -1
        in_play=False
        return
    else:
        while dealer_hand.get_value()<17:
            print "Hitting dealer"
            dealer_hand.add_card(deck.deal_card())
            outcome = ""
        
    if dealer_hand.busted():
        outcome = "Dealer Busted, You(Player) Wins"
        score += 1
        in_play=False
    elif player_hand.get_value()<=dealer_hand.get_value():
        outcome = "You(Player) Lose"
        score += -1
        in_play=False
    else:
        outcome = "You(Player) Wins"
        score += 1
        in_play=False
        
    # assign a message to outcome, update in_play and score

def display_holecard(canvas):
    card_loc = (CARD_BACK_CENTER[0] + CARD_SIZE[0] * 0, 
                CARD_BACK_CENTER[1] + CARD_SIZE[1] * 0)
    pos=[80,150]
    canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
    
# draw handler    
def draw(canvas):
    
    dealer_hand.draw(canvas,[80,150])
    player_hand.draw(canvas,[80,350])
    
    canvas.draw_text("Blackjack", (100, 100), 40, "Aqua")
    canvas.draw_text("Score " + str(score), (400, 100), 20, "Black")
    
    #Hide dealer hole card
    if in_play:
        display_holecard(canvas)
        player_question = "Hit or stand?"
    else:
        player_question = "New Deal?"
        
    canvas.draw_text("Dealer", (80, 140), 20, "Black")
    canvas.draw_text(outcome,  (200, 140), 20, "Black")
    
    canvas.draw_text("Player", (80, 340), 20, "Black")
    canvas.draw_text(player_question,  (200, 340), 20, "Black")

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


# remember to review the gradic rubric