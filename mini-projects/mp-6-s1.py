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

LEFT_MARGIN = 30
SPACING = {'Title': [210, 100], 'Score': [LEFT_MARGIN, 50], 'Dealer msg': [LEFT_MARGIN, 160], 'Dealer hand': [LEFT_MARGIN*2, 180], 'Player msg': [LEFT_MARGIN, 350], 'Player hand': [LEFT_MARGIN*2, 370], 'Instructions': [LEFT_MARGIN, 530], 'Outcome': [LEFT_MARGIN, 570]}
TEXT_SIZE = {'Title': 40, 'Score': 25, 'Dealer msg': 30, 'Instructions': 20, 'Player msg': 30, 'Outcome': 20}
COLORS = {'Active': 'Black', 'Inactive': 'Gray', 'Good': 'Blue', 'Neutral': 'White', 'Bad': 'Red'}

CARD_GAP = 10

text_color = {'Title': 'Black', 'Score': 'White', 'Dealer msg': 'Black', 'Instructions': 'Black', 'Player msg': 'Black', 'Outcome': 'Black'}


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

    def draw(self, canvas, pos, flipped=True):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if flipped:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        

    def __str__(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)
    

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        value = 0
        ace = False
        
        for i in self.cards:
            r = i.get_rank()
            value += VALUES[r]
            if r == 'A':
                ace = True
        
        if ace and value < 12:
            value += 10
            
        return value

    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, p, flipped = True):
        i = 0
        for card in self.cards:
            pos = [p[0]+i*(CARD_SIZE[0]+CARD_GAP), p[1]]
            
            if i == 0:
                card.draw(canvas, pos, flipped)
            else:
                card.draw(canvas, pos)
                
            i += 1
 
        
# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in SUITS:
            self.cards.extend([Card(suit, rank) for rank in RANKS])
        
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        return self.cards



#define event handlers for buttons


def deal():
    global outcome, in_play, message, score
    global deck, dealer_hand, player_hand
    
    message = ""

    text_color['Player msg'] = COLORS['Active']
    text_color['Dealer msg'] = COLORS['Inactive']
    
    deck = Deck()
    
    deck.shuffle()
    
    if in_play:
        score -= 1
    else:
        in_play = True
        
    dealer_hand = Hand()
    player_hand = Hand()
    
    for i in range(2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        
    
    

def hit():
    global message, in_play, score
    
    if in_play:
        player_hand.add_card(deck.deal_card())
        
        if player_hand.busted():
            message = "You are busted, dealer wins!"
            text_color['Outcome'] = COLORS['Bad']
            in_play = False
            score -= 1
       
def stand():
    global in_play, message, score
    if in_play:
        in_play = False
        text_color['Player msg'] = COLORS['Inactive']
        text_color['Dealer msg'] = COLORS['Active']
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            
        if dealer_hand.busted():
            message = "Dealer is busted, you win!"
            text_color['Outcome'] = COLORS['Good']
            score += 1
        else:
            d = dealer_hand.get_value()
            p = player_hand.get_value()
            
            message = "Dealer has " + str(d)+ " points, you have " + str(p) + ". "
            
            if d < p:
                message += "You win!"
                text_color['Outcome'] = COLORS['Good']
                score += 1
            else:
                message += "Dealer wins!"
                text_color['Outcome'] = COLORS['Bad']
                score -= 1
                        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
  
    if in_play:
        instructions = "Hit or stand?"
    else:
        instructions = "New deal?"
                
    if score == 0:
        text_color['Score'] = COLORS['Neutral']
    elif score > 0:
        text_color['Score'] = COLORS['Good']
    else:
        text_color['Score'] = COLORS['Bad']
    
    canvas.draw_text("Blackjack", SPACING['Title'], TEXT_SIZE['Title'], text_color['Title'])
    canvas.draw_text("Score: " + str(score), SPACING['Score'], TEXT_SIZE['Score'], text_color['Score'])
    canvas.draw_text("Dealer:", SPACING['Dealer msg'], TEXT_SIZE['Dealer msg'], text_color['Dealer msg'])
    dealer_hand.draw(canvas, SPACING['Dealer hand'], not in_play)
    canvas.draw_text(instructions, SPACING['Instructions'], TEXT_SIZE['Instructions'], text_color['Instructions'])
    canvas.draw_text("Player:", SPACING['Player msg'], TEXT_SIZE['Player msg'], text_color['Player msg'])
    player_hand.draw(canvas, SPACING['Player hand'])
    canvas.draw_text(message, SPACING['Outcome'], TEXT_SIZE['Outcome'], text_color['Outcome'])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
score = 0
in_play = False
deal()
# get things rolling
frame.start()
