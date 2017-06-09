# Mini-Project-4

# Implementation of "Classic Arcade Game: Pong"

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2


def paddle_hit():
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_vel[0] += math.ceil(ball_vel[0]*0.1)
    ball_vel[1] += math.ceil(ball_vel[1]*0.1)
    
    ball_vel = [-1*ball_vel[0],-1 * ball_vel[1]]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    global score1, score2
    
    if ball_vel[1] == 0:
        ball_vel[1] = -1 * random.randrange(1,3)
    
    # Ball hits the paddles
    if 	right and (ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT):
        print "left paddle hit"
        paddle_hit()
        
    elif ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT:    
        print "right paddle hit"
        paddle_hit()
        
    # Hits the gutter   
    else:
        cycle = 0
        # spawn ball back in the center
        ball_pos = [WIDTH/2, HEIGHT/2]
        
        ball_vel = [math.ceil(random.randrange(120,240)/60),-1*math.ceil(random.randrange(60,180)/60)]
    
        # head toward oppositve corner
        if right:
            print "left gutter hit"
            
            ball_vel[0] = 1*ball_vel[0]
            
            score2 += 1
        
        else:
            print "right gutter hit"
            
            ball_vel[0] = -1*ball_vel[0]
            score1 += 1
        
    
def ball_collides_vertically():
        
        ball_vel[1]	= -1*ball_vel[1]
        ball_pos[1] += ball_vel[1]
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    # left paddle
    if 	paddle1_vel < 0 and paddle1_pos[1] + paddle1_vel >= 0:
        paddle1_pos[1] +=  paddle1_vel
    elif paddle1_vel > 0 and paddle1_pos[1] + PAD_HEIGHT <= HEIGHT:
        paddle1_pos[1] +=  paddle1_vel
    # right paddle    
    if 	paddle2_vel < 0 and paddle2_pos[1] + paddle2_vel >= 0:
        paddle2_pos[1] +=  paddle2_vel
    elif paddle2_vel > 0 and paddle2_pos[1] + PAD_HEIGHT <= HEIGHT:
        paddle2_pos[1] +=  paddle2_vel    
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    
    # left paddle
    canvas.draw_polyline([paddle1_pos, [PAD_WIDTH, paddle1_pos[1] + 0], [PAD_WIDTH, paddle1_pos[1] + PAD_HEIGHT], [0, paddle1_pos[1] + PAD_HEIGHT], paddle1_pos], PAD_WIDTH, "White")
    
    # right paddle
    canvas.draw_polyline([paddle2_pos, [WIDTH-PAD_WIDTH, paddle2_pos[1] + 0], [WIDTH-PAD_WIDTH, paddle2_pos[1] + PAD_HEIGHT], [WIDTH, paddle2_pos[1] + PAD_HEIGHT], paddle2_pos], PAD_WIDTH, "Blue")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Collision Detection
    
    # horizontal collision
    # right gutter
    if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        ball_init(False)
        
    # left gutter
    elif ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
        ball_init(True)
        
    # vertical collision
    # down	
    if ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_collides_vertically()
    # up
    elif ball_pos[1] - BALL_RADIUS <= 0:
        ball_collides_vertically()
    
    # draw ball and scores
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 1, "Red", "Orange")
    
    canvas.draw_text(str(score1), [WIDTH / 2 - BALL_RADIUS*2, 50], 20, "White")
    canvas.draw_text(str(score2), [WIDTH / 2 + BALL_RADIUS*2, 50], 20, "Blue")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # left paddle movement
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP["s"]:    
        paddle1_vel = 10
    
    # right paddle movement
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10
    elif key == simplegui.KEY_MAP["down"]:    
        paddle2_vel = 10    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
     
    # stop left paddle movement
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    # stop right paddle movement
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
        
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    global ball_pos, ball_vel
    
    # initial Ball Position
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    ball_vel = [math.ceil(random.randrange(120,240)/60),-1*math.ceil(random.randrange(60,180)/60)]
    
    # initial paddle positions
    paddle1_pos = [0,HEIGHT/2-PAD_HEIGHT]
    paddle2_pos = [WIDTH,HEIGHT/2-PAD_HEIGHT]

    paddle1_vel=0
    paddle2_vel=0

    score1 = 0
    score2 = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()

# remember to review the grading rubric