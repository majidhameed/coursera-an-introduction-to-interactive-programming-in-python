# template for "Stopwatch: The Game"
import simplegui

# define global variables
sc_str = ""
t_str = ""
tick = 0
tries = 0
succ = 0
running = False

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    A = str(t // 600)
    BC = ("00" + str(int(t / 10) % 60))[-2:]
    D = str(t % 10)
    r = A + ":" + BC + "." + D
    return r

# define event handlers for buttons; "Start", "Stop", "Reset"
def h_start():
    global running
    running = True
    timer.start()
    return

def h_stop():
    global tries
    global succ
    global sc_str
    global running
    timer.stop()
    if running:
        tries = tries + 1
        if D == "0":
             succ = succ + 1
        sc_str = str(succ) + "/" + str(tries)
    
    running = False
    return

def h_reset():
    global tick
    global running
    running = False
    timer.stop()
    tick = 0
    init()
    return

def init():
    global sc_str
    global t_str
    global tries
    global succ
    tries = 0
    succ = 0
    sc_str = "0/0"
    t_str = "0:00.0"
    return

def draw(canvas):
    canvas.draw_text(sc_str, (150, 24), 16, "Green")
    canvas.draw_text(t_str, (60, 80), 24, "White")
    
# define event handler for timer with 0.1 sec interval
def t_handler():
    global t_str
    global tick
    tick = tick + 1
    t_str = format(tick)
    # print tick, format(tick)
    return
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 140)
b_start = frame.add_button("Start", h_start, 100)
b_stop = frame.add_button("Stop", h_stop, 100)
b_reset = frame.add_button("Reset", h_reset, 100)
timer = simplegui.create_timer(100, t_handler)

# register event handlers
frame.set_draw_handler(draw)

# start timer and frame
frame.start()
init()
# remember to review the grading rubric