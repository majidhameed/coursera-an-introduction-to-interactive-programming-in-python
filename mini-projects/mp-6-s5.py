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
outcome = ""
score = 0
win = 0
loss = 0
show_dealer = False

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

    def draw(self, canvas, pos, hide):
        if hide == False:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:            
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                              [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self, name):        
        self.cards = []
        self.name = name
        #self.value = 0

    def __str__(self):        
        return name + ": " + str(value)

    def add_card(self, card):        
        self.cards.append(card)        

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        val = 0
        one = 0
        for c in self.cards:
            tmp = VALUES[c.get_rank()]
            val += tmp
            if tmp == 1:
                one += 1
        
        while one > 0:
            if val <= 11:
                val += 10
                one -= 1
            else:
                break
        
        return val

    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False
    
    def draw(self, canvas, p, hide):
        pos = p
        if hide:
            self.cards[0].draw(canvas, pos, True)
            pos[0] += CARD_SIZE[0]
            self.cards[1].draw(canvas, pos, False)
        else:
            for c in self.cards:
                c.draw(canvas, pos, False)
                pos[0] += CARD_SIZE[0]
    
    def clear(self):
        self.cards = []
        #self.value = 0
        
# define deck class
class Deck:
    def __init__(self):
        self.cards = []

    # add cards back to deck and shuffle
    def shuffle(self):    
        for s in SUITS:
            for r in RANKS:
                c = Card(s,r)
                self.cards.append(c)
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            self.shuffle()
        return self.cards.pop(0)
    
    def __str__(self):
        pass	# replace with your code

deck = Deck()    
player = Hand("player")
dealer = Hand("dealer")

#define event handlers for buttons
def deal():
    global outcome, in_play, score, message, loss, show_dealer
    
    player.clear()
    dealer.clear()

    c = deck.deal_card()
    player.add_card(c)
    c = deck.deal_card()
    player.add_card(c)
    c = deck.deal_card()
    dealer.add_card(c)
    c = deck.deal_card()
    dealer.add_card(c)
    
    if in_play:
        outcome = "You lose since the hand is not over!"
        score -= 1
        loss += 1
    else:
        outcome = ""
    in_play = True
    
    message = "Hit or stand?"
    show_dealer = False
    #print deck.cards

def hit():
    global outcome, in_play, score, message, loss
    
    if in_play:
        c = deck.deal_card()
        player.add_card(c)
        if player.busted():            
            outcome = "You have busted... You lose..."
            in_play = False            
            score -= 1
            loss += 1
            message = "New deal?"
        else:
            outcome = ""
    else:        
        outcome = "This hand is already over! Press the Deal button!"
    
    # if the hand is in play, hit the player
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score, message, win, loss, show_dealer
    
    if in_play:
        while dealer.get_value() < 17:
            c = deck.deal_card()
            dealer.add_card(c)
        if dealer.busted():            
            outcome = "Dealer has busted! You win!"
            score += 1
            win += 1
        else:
            if player.get_value() > dealer.get_value():                
                outcome = "You win!"
                score += 1
                win += 1
            else:                
                outcome = "You lose..."
                score -= 1
                loss += 1
        in_play = False
        show_dealer = True
    else:
        outcome = "This hand is already over! Press the Deal button!"
    
    message = "New deal?"
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    canvas.draw_text("Blackjack", [10, 30], 20, "Black")
    canvas.draw_text("Score: " + str(score) + " (win: " + str(win) + ", loss: " + str(loss) + ")", [10, 60], 20, "Blue")
    canvas.draw_text(message, [10, 90], 20, "Yellow")
    canvas.draw_text(outcome, [10, 120], 20, "Red")
    canvas.draw_text("Player: " + str(player.get_value()), [50, 190], 15, "Black")
    player.draw(canvas, [50, 200], False)
    #if show_dealer:
    if in_play == False:
        canvas.draw_text("Dealer: " + str(dealer.get_value()), [50, 340], 15, "Black")
        dealer.draw(canvas, [50, 350], False)
    else:
        canvas.draw_text("Dealer: ??", [50, 340], 15, "Black")
        dealer.draw(canvas, [50, 350], True)    

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