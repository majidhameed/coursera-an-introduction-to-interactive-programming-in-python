# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# helper function that spawns a ball, returns a position vector and a velocity vector
def spawns():
    global score1, score2
    
    position = (ball_pos)
    velocity = (ball_vel)
    
    # Check for top/bottom, left, right, sets velocity or init the ball if necesary
    if position[1] <= BALL_RADIUS or position[1] >= HEIGHT - BALL_RADIUS:
        velocity[1] = - velocity[1] 
        
    # left gutter
    if (position[0] <= PAD_WIDTH + BALL_RADIUS and not is_ball_hitting_left_paddle(position)):
        score2 += 1
        ball_init(False)
    elif is_ball_hitting_left_paddle(position):
        velocity[0] = - velocity[0] * 1.10
    # right gutter    
    if ((position[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and not is_ball_hitting_right_paddle(position)):        
        score1 += 1
        ball_init(True)
    elif is_ball_hitting_right_paddle(position):
        velocity[0] = - velocity[0] * 1.10    
    
    return [position,velocity]

def is_ball_hitting_right_paddle(ball_position):
    """ Checks ball position and returns true if it is hitting the right paddle """
    
    is_hitting = False
    if ((WIDTH - PAD_WIDTH - BALL_RADIUS) <= ball_position[0]
        and (paddle2_pos[0][1] <= ball_position[1] 
        and paddle2_pos[1][1] >= ball_position[1])):
        is_hitting = True
        
    return is_hitting

def is_ball_hitting_left_paddle(ball_position):
    """ Checks ball position and returns true if it is hitting the left paddle """
    
    is_hitting = False
    if ((PAD_WIDTH + BALL_RADIUS) >= ball_position[0]
        and (paddle1_pos[0][1] <= ball_position[1] 
        and paddle1_pos[1][1] >= ball_position[1])):
        is_hitting = True
        
    return is_hitting

def move_paddle(paddle_pos, paddle_vel):
    """ Moves paddle position """
    
    paddle_pos[0][1] += paddle_vel
    paddle_pos[1][1] += paddle_vel
                
def paddle_in_range(paddle_position, paddle_vel):
    """ Returns true if paddle pos + vel is inside canvas """"
    
    return check_paddle_pos_top(paddle_position[0][1] + paddle_vel) and check_paddle_pos_bottom(paddle_position[1][1]  + paddle_vel)
    
def check_paddle_pos_top(vertical_pos):
    return vertical_pos >= 0

def check_paddle_pos_bottom(vertical_pos):   
    return vertical_pos <= HEIGHT

def ball_init(right):
    """" Init ball position and velocity. """
    global ball_pos, ball_vel 					# these are vectors stored as lists
    
    # Always init centered upwards
    ball_pos = list([WIDTH / 2, HEIGHT / 2])
    ball_vel = list([random.randrange(120, 240)/60, - random.randrange(120, 240)/60])
    
    if (right):									# Always init to the opposite
        ball_vel[0] = - abs(ball_vel[0])
    else:
        ball_vel[0] = abs(ball_vel[0])
    
    pass

# define event handlers
def init():
    """ Init most global variables """
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    
    h_center = (HEIGHT / 2) - HALF_PAD_HEIGHT
    paddle1_pos = [[HALF_PAD_WIDTH, h_center], [HALF_PAD_WIDTH, h_center + PAD_HEIGHT]]
    paddle2_pos = [[WIDTH - HALF_PAD_WIDTH, h_center], [WIDTH - HALF_PAD_WIDTH, h_center + PAD_HEIGHT]]
    paddle1_vel,paddle2_vel  = 0, 0
    ball_init(random.randrange(0,2))	# Randomly init the ball either to the right or to the left    
    score1, score2  = 0, 0				# Set scores to 0, since ball_init modifies those values
    
    pass

def draw(c):
    """ Draws paddles, gutters, ball and score """
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle_in_range(paddle1_pos, paddle1_vel)):
        move_paddle(paddle1_pos, paddle1_vel)    
    if (paddle_in_range(paddle2_pos, paddle2_vel)):
        move_paddle(paddle2_pos, paddle2_vel) 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles          
    c.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "White")
    c.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "White")
    
    # update ball
    spawns()
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]    
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (WIDTH / 4, 50), 30, "White")
    c.draw_text(str(score2), (WIDTH - WIDTH / 4, 50), 30, "White")    
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5        
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    if key == 38:
        paddle2_vel -= 5
    if key == 40:
        paddle2_vel += 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']):
        paddle1_vel = 0        
    if (key == 38 or key == 40):
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

