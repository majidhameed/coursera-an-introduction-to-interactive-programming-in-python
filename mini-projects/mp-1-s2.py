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
    
    # convert number to a name using if/elif/else
    
    if   number == 0: return "rock"
    elif number == 1: return "Spock"
    elif number == 2: return "paper"
    elif number == 3: return "lizard"
    elif number == 4: return "scissors"   
    
def name_to_number(name):

    # convert name to number using if/elif/else
    
    if   name == "rock"    : return 0
    elif name == "Spock"   : return 1
    elif name == "paper"   : return 2
    elif name == "lizard"  : return 3
    elif name == "scissors": return 4 

def rpsls(name): 
    

    # convert name to player_number using name_to_number
    player = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    computer = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    evaluate = (player - computer) % 5
    
    # print players choices
    print 'Player chooses',number_to_name(player)
    print 'Computer chooses',number_to_name(computer)
    
    # use if/elif/else to determine winner and print results
    if evaluate ==0:
        print "Player and Computer tie!\n" 
    elif evaluate <=2:
        print "Player wins!\n"
    else :
        print "Computer wins!\n"
    
    
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


