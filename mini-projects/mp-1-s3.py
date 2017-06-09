# Rock-paper-scissors-lizard-Spock game

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# helper functions

def number_to_name(number):
    """Converts number to name following the number-string conversion table above"""
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"
       
    return name

def name_to_number(name):
    """Converts name to number following the number-string conversion table above"""

    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4

    return number



def rpsls(guess): 
    """Generates random computer guess, compares it to player's guess and determines the winner"""
    
    print
    print "Player chooses", guess
    
    player_number = name_to_number( guess )
    
    comp_number = random.randrange( 5 )

    name = number_to_name( comp_number )
    print "Computer chooses", name

    diff = (player_number - comp_number + 5 ) % 5

    # determine the winner
    if diff == 0:
        message = "Player and computer tie!"
    elif diff == 1 or diff == 2:
        message = "Player wins!"
    else:
        message = "Computer wins!"
        
    # print results
    print message

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


