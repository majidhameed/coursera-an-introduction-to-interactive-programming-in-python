# Mini-Project-1 

# Implementation of Game - Rock-paper-scissors-lizard-Spock

# For Game Details - Please visit http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def number_to_name(number):
    '''(number) -> str
    
    Returns the game element name on the basis of following rules:
    
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    
    Precondition: 0 <= number <= 4
    
    >>> number_to_name(0)
    rock
    >>> number_to_name(1)
    Spock
    >>> number_to_name(2)
    paper
    >>> number_to_name(3)
    lizard
    >>> number_to_name(4)
    scissors
    '''
    if number == 0 :
        name = 'rock'
    elif number == 1 :
        name = 'Spock'
    elif number == 2 :
        name = 'paper'
    elif number == 3 :
        name = 'lizard'
    else :
        name = 'scissors'
   
    return name

def name_to_number(name):
    '''(str) -> number
    
    Returns the game element number on the basis of following rules:
    
    rock - 0
    Spock - 1
    paper - 2
    lizard - 3
    scissors - 4
    
    Precondition: str = ['rock','Spock','paper','lizard','scissors']
    
    >>> name_to_number('rock')
    0
    >>> name_to_number('Spock')
    1
    >>> name_to_number('paper')
    2
    >>> name_to_number('lizard')
    3
    >>> name_to_number('scissors')
    4
    '''
    if name == 'rock' :
        number = 0
    elif name == 'Spock' :
        number = 1
    elif name == 'paper' :
        number = 2
    elif name == 'lizard' :
        number = 3
    else :
        number = 4    

    return number


def rpsls(name):
    '''(str)->None
    
    Computer randomly guesses a number between 0-4 inclusive. 
    
    Output:
    prints What player chooses
    prints What computer chooses 
    prints who wins!
    ''' 

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    difference = ( player_number - comp_number ) % 5

    # use if/elif/else to determine winner
    if (difference == 1 or difference == 2 ): # 1st Item that is player wins
      result = 'Player wins!'
    elif (difference == 0): # tie
      result = 'Player and computer tie!'
    else: # 2nd Item that is computer wins
      result = 'Computer wins!'      
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
  
    # print results
    print ''
    print 'Player chooses' ,  name
    print 'Computer chooses' ,  comp_name
    print result
    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")