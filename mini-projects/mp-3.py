# Mini-Project-3

# Implementation of "Stopwatch: The Game"

import simplegui

# Global Variables

# holds tenth of second integer value
tenth_second=0

# as we know 1s = 1000ms; 1/10 s = 1000/10 ms => 0.1s = 100ms
interval = 100

# holds the formatted (time) string that is displayed in stop watch
time = ""

# frame dimensions
frame_width=300
frame_height=220

# flag for tracking timer is stop or not
is_timer_active = True

# count for tracking successful stops
success_stop_count=0

# count for tracking total stops
total_stop_count=0

# Helper Functions

# Helper Function - Returns formatted string A:BC.D for the given integer 10th of second
def format(t):
    ''' (int)->str	
    
    Returns the formatted (time) string for the given 10th of second
    
    >>> format(0)
    0:00.0
    >>> format(11)
    0:01.1
    >>> format(321)
    0:32.1
    >>> format(613)
    1:01.3
    '''
    # tenth_second in 0-9 range
    tenth_sec  = t % 10
    
    # second in 0-59 range
    second = int(t / 10) % 60
    
    # minute in 0-59 range
    minute = int(t / 10 / 60) % 60
    
    # second with leading zero
    second = "0" + str(second)
    # pick last 2 characters for 09 => 9 and for 011 => 11
    second = second[-2:]
    
    # return formatted string as per required format
    return str(minute) + ":" + second + "." + str(tenth_sec)

# Event Handlers 

# Event Handlers for buttons; "Start", "Stop", "Reset"

# Event Handler - for start button     
def start_button_handler():
    global is_timer_active
    
    # set the timer active flag to True
    is_timer_active = True
    
    # start the watch
    timer.start()
    
# Event Handler - for stop button     
def stop_button_handler():
    global total_stop_count, success_stop_count, is_timer_active
    
    # If watch is in start state then
    if is_timer_active:
        
        # increment total stop count by 1
        total_stop_count+=1
        
        # If watch is stopped at Whole Second then
        if tenth_second%10 == 0:
        
            # increment successful stop count by 1
            success_stop_count+=1
            
    # set the watch start state to false        
    is_timer_active = False
    
    # stop the watch
    timer.stop()
    
    
# Event Handler - for reset button    
def reset_button_handler():
    global tenth_second, time, total_stop_count, success_stop_count
    
    # stop the watch
    stop_button_handler()
    
    # Reset all counts, strings
    
    # reset tenth of second
    tenth_second=0
    
    # reset formatted (time) string
    time = format(tenth_second)
    
    # reset successful stop counts
    success_stop_count=0
    
    # reset total stop counts
    total_stop_count=0
    
    
# Event Handler - for timer with 0.1 sec interval
def timer_handler():
    global tenth_second, time
    
    # increment tenth of second by 1
    tenth_second+=1
    
    # set the formatted time for new value of tenth of second
    time = format(tenth_second)
    
    
# Event Handler - for drawing text    
def draw_handler(canvas):
    
    # draw the formatted time in middle of the screen in White
    canvas.draw_text(time, [frame_width/2-60, frame_height/2], 40, 'White')
    
    # draw the x/y counts on top left of the screen with Yellow
    canvas.draw_text(str(success_stop_count) +"/" + str(total_stop_count), [0,20], 20, "Yellow")
    
    
# create frame
frame = simplegui.create_frame('StopWatch',frame_width,frame_height)
timer = simplegui.create_timer(100,timer_handler)

# add buttons with event their respective event handlers
frame.add_button('Start',start_button_handler,100)
frame.add_button('Stop',stop_button_handler,100)
frame.add_button('Reset',reset_button_handler,100)

# register draw event handler
frame.set_draw_handler(draw_handler)

# start timer
timer.start()
# start frame
frame.start()

# remember to review the grading rubric