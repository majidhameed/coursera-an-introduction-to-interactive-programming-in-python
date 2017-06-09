# "Stopwatch: The Game"
# Based on the provided template

import simplegui

# global variables
timer_count = 0
a = 0
b = 0
c = 0
d = 0
tries = 0
wins = 0
is_started = False

# helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    a = int(t / 600)
    b = int((t % 600)/100)
    c = int((t % 600)/10)%10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# event handlers for buttons; "Start", "Stop", "Reset", and
# to draw the timer and game results to the canvas
def start_handler():
    global is_started
    timer.start()
    is_started = True
    
def stop_handler():
    global tries, wins, d, is_started
    if is_started:
        tries += 1
        if d == 0:
            wins += 1
    timer.stop()
    is_started = False
        
def reset_handler():
    global timer_count, tries, wins, is_started
    timer_count = 0
    tries = 0
    wins = 0
    timer.stop()
    is_started = False
    
def draw(canvas):
    canvas.draw_text(format(timer_count), (60, 110), 25, "Red")
    canvas.draw_text(str(wins) + "/" + str(tries), (25, 25), 12, "Green")
    
# event handler for timer with 0.1 sec interval
def tick():
    global timer_count
    timer_count += 1

# creating the frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# called event handlers
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)


# start the frame
frame.start()

