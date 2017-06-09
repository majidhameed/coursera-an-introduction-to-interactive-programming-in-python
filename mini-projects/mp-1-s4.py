# Rock-paper-scissors-lizard-Spock template


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
import random

def number_to_name(number):
    # fill in your code below
    # a switch statement would be better, but I'll do it they way they instruct
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"	          
    elif number == 2:
        return "paper"                 
    elif number == 3:
        return "lizard"
    else:
        return "scissors"
    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1	          
    elif name == "paper":
        return 2                 
    elif name == "lizard":
        return 3
    else: 
        return 4

def rpsls(name): 

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)	
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number)%5
    
    comp_name = number_to_name(comp_number)
    # print results
    print "Player selects " + name
    print "Computer selects " + comp_name
    if difference == 1 or difference == 2:
        print "Player wins!"
    elif difference == 3 or difference == 4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    print
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


