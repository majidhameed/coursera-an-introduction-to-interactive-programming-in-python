# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80

# helper function that spawns a ball, returns a position vector and a velocity vector
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    dir = 1
    ball_pos = [WIDTH/2, HEIGHT/2]
    if(not right):
        dir = -1
    hor = dir * (random.randrange(2,4))
    vir = - (random.randrange(1, 3))
    ball_vel = [hor, vir]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats 
    global score1, score2  # these are ints
    score1, score2, paddle1_vel, paddle2_vel = 0, 0, 0, 0
    paddle1_pos = [0, (HEIGHT/2) - PAD_HEIGHT/2]
    paddle2_pos = [WIDTH-PAD_WIDTH, HEIGHT/2 - PAD_HEIGHT/2]
    ball_init(random.randrange(4) % 2 == 1)
    
def drawBall(c):  
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if(ball_pos[0] <= BALL_RADIUS + PAD_WIDTH or ball_pos[0] > (WIDTH -1)- (BALL_RADIUS + PAD_WIDTH)): 
        ball_vel[0] = - ball_vel[0]
    if(ball_pos[1] <= BALL_RADIUS or ball_pos[1] > (HEIGHT -1) - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")    

def draw_paddle(c, paddle_pos, vel):
    if (paddle_pos[1] >= 0 and paddle_pos[1] <= HEIGHT-PAD_HEIGHT):
        paddle_pos[1] += vel
    if (paddle_pos[1] < 0):
        paddle_pos[1] = 0
    elif (paddle_pos[1] > HEIGHT-PAD_HEIGHT):
        paddle_pos[1] = HEIGHT-PAD_HEIGHT    
    c.draw_line([paddle_pos[0] + PAD_WIDTH/2, paddle_pos[1]], [paddle_pos[0] + PAD_WIDTH/2 , paddle_pos[1]+PAD_HEIGHT], PAD_WIDTH, "White")  

def inc_vel():
    if(ball_vel[0] <= 0):
        ball_vel[0] = - (math.fabs(ball_vel[0]) + float((math.fabs(ball_vel[0])*2)/10))
    else :
        ball_vel[0] = ball_vel[0] + float((ball_vel[0] *2)/10)

    if(ball_vel[1] <= 0):
        ball_vel[1] = - (math.fabs(ball_vel[1]) + float((math.fabs(ball_vel[1])*2)/10))
    else :
        ball_vel[1] = ball_vel[1] + float((ball_vel[1]* 2)/10)
            
def check(): # Check the ball relative to paddles to update the score if needed 
    global score1, score2
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH): 
        if(ball_pos[1] < paddle1_pos[1] or ball_pos[1] > paddle1_pos[1] + PAD_HEIGHT):
            score2 += 1
            ball_init(True)
        else : inc_vel()    
    elif (ball_pos[0] > (WIDTH -1)- (BALL_RADIUS + PAD_WIDTH)):
        if(ball_pos[1] < paddle2_pos[1] or ball_pos[1] > paddle2_pos[1] + PAD_HEIGHT):
            score1 += 1
            ball_init(False)
        else : inc_vel()    
        
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles    
    draw_paddle(c, paddle1_pos, paddle1_vel)
    draw_paddle(c, paddle2_pos, paddle2_vel)
            
    # draw ball and scores
    drawBall(c)
    c.draw_text(str(score1), [150, 80], 26, "White")
    c.draw_text(str(score2), [450, 80], 26, "White")
    check()

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"] :
       paddle2_vel = -4
    elif key == simplegui.KEY_MAP["down"] :
       paddle2_vel = 4
    elif key == simplegui.KEY_MAP["w"] :
       paddle1_vel = -4
    elif key == simplegui.KEY_MAP["s"] :
       paddle1_vel = 4
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]) :
       paddle2_vel = 0
    if (key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]) :
       paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()