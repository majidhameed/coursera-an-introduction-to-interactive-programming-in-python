# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT /2]
ball_vel = [0, 0]
score1 = 0
score2 = 0
paddle1_pos = 0
paddle2_pos = 0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT /2]
    if right == True :
        ball_vel = [((random.randrange(20, 240) / 60)),  (-(random.randrange(60, 180) / 60))]    
    else :
        ball_vel = [(-(random.randrange(20, 240) / 60)),  (-(random.randrange(60, 180) / 60))]    
    
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(True)
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT /2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT /2 - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= 0 and paddle1_vel < 0) or (paddle1_pos + PAD_HEIGHT >= HEIGHT and paddle1_vel > 0):
        paddle1_pos += 0
    else:
        paddle1_pos += paddle1_vel
    if (paddle2_pos <= 0 and paddle2_vel < 0) or (paddle2_pos + PAD_HEIGHT >= HEIGHT and paddle2_vel > 0):
        paddle2_pos += 0
    else:
        paddle2_pos += paddle2_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw paddles
#   canvas.draw_line(point1, point2, line_width, line_color)
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, (paddle1_pos + PAD_HEIGHT)], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # collide and reflect off of left side of canvas
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)) and ((ball_pos[1] >= paddle1_pos) or (ball_pos[1] <= paddle1_pos + PAD_HEIGHT)) :
        ball_vel[0] = - ball_vel[0] * 1.1
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) and ((ball_pos[1] <= paddle1_pos) or (ball_pos[1] >= paddle1_pos + PAD_HEIGHT)) :
        ball_init(True)
        score2 += 1
    # collide and reflect off of right side of canvas
    if (ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)) and ((ball_pos[1] >= paddle2_pos) or (ball_pos[1] <= paddle2_pos + PAD_HEIGHT)) :
        ball_vel[0] = - ball_vel[0] * 1.1
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)  and ((ball_pos[1] <= paddle2_pos) or (ball_pos[1] >= paddle2_pos + PAD_HEIGHT)) :
        ball_init(False)
        score1 += 1
    # collide and reflect off of top and bottom of canvas
    if ball_pos[1] >= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] <= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
           
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 4, "White", "White")    
    c.draw_text(str(score1),[2.5*(WIDTH / 8), HEIGHT / 4], 48, "White")
    c.draw_text(str(score2),[5*(WIDTH / 8), HEIGHT / 4], 48, "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    acc = 6
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos, paddle2_pos
    acc = 6
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)

# start frame
init()
frame.start()

