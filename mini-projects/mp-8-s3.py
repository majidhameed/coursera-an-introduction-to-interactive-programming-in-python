# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 0
time = 0
started = False
rock_group = set([])
missile_group = set([])
explosion_group = set([])

left = False
right = False
cw = 0
up = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 2)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


#helper function "process_sprite_group".

def process_sprite_group (group_set, canvas):
     remove_set = set([])
     for x in group_set:
         x.draw(canvas)          
         if not x.update():          
                remove_set.add(x)                  
     group_set.difference_update(remove_set)

       
            
def group_collide (group_set, sprt): 
    remove_set = set([])  
    for x in group_set:
        if x.collide(sprt):
            explosion_group.add(Sprite( sprt.pos, [0,0], 0 ,0, explosion_image, explosion_info,explosion_sound ))
            remove_set.add(x)          
    group_set.difference_update(remove_set)  
    return len(remove_set)

def group_group_collide ( group_set1, group_set2):
    remove_set = set([])
    for x in group_set1:
        if group_collide (group_set2,x) > 0: 
            remove_set.add(x)
    group_set1.difference_update(remove_set)  
    return len(remove_set)
    
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):         
        canvas.draw_image(self.image , (self.image_center[0] +( self.image_size[0] * int(self.thrust)), self.image_center[1]) ,self.image_size , self.pos, self.image_size, self.angle)
        
    def update(self):
        # Rotation
        global left, right,cw        
        if left or right:
            self.angle += (math.pi /60) * (-1)**cw 
        self.angle = self.angle % (2 * math.pi )   
        angulo =  angle_to_vector(self.angle)      
        # thrust
        if self.thrust:
            self.vel[0] +=  angulo[0] * 0.05
            self.vel[1] +=  angulo[1] * 0.05
            ship_thrust_sound.set_volume(1)
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
        self.vel[0]*=.995
        self.vel[1]*=.995
        self.pos[0]+= self.vel[0] 
        self.pos[1]+= self.vel[1]   
        self.pos[0] = self.pos[0] % width 
        self.pos[1] = self.pos[1] % height
            
    def shot(self):
        angulo =  angle_to_vector(self.angle)
        missile_group.add(Sprite( [(self.pos[0] +angulo[0] * self.radius) , (self.pos[1]+angulo[1] * self.radius)] , [self.vel[0]+angulo[0]*6 ,self.vel[1]+angulo[1]*6], 0, 0, missile_image, missile_info, missile_sound) )              
        
    def get_position(self):
        return self.pos
        
    def get_radius(self): 
        return self.radius    
    
    def collide(self, obj):
        return (dist(self.pos, obj.get_position()) <= (self.radius+obj.get_radius()))
        
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated:
            current_center = [self.image_center[0] +  60* self.age * self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image , current_center ,self.image_size , self.pos, self.image_size, self.angle)
        else:     
             canvas.draw_image(self.image , self.image_center ,self.image_size , self.pos, self.image_size, self.angle)
        
    
    def update(self):
        # Rotation
        self.angle += self.angle_vel
        self.angle = self.angle % (2 * math.pi )                 
        self.pos[0]+= self.vel[0] 
        self.pos[1]+= self.vel[1]   
        self.pos[0] = self.pos[0] % width 
        self.pos[1] = self.pos[1] % height        
        self.age += 1/60
        return  (self.age < self.lifespan) 
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_position(self):
        return self.pos
        
    def get_radius(self): 
        return self.radius
    
    def collide(self, obj):
        return (dist(self.pos, obj.get_position()) <= (self.radius+obj.get_radius()))
            
        


# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score ,rock_group
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        rock_group = set([])
        missile_group = set([])
        timer.start()
        soundtrack.rewind()
        soundtrack.set_volume(.2)
        soundtrack.play()
        
        
           
def draw(canvas):
    global time, started,lives,score,rock_group   
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])
    
    if group_collide(rock_group, my_ship ) and started:
        lives -= 1
        if lives == 0:
            started = False 
            rock_group = set([]) 
            timer.stop()
            soundtrack.pause()
        
    score += group_group_collide (missile_group,rock_group)
    
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group( rock_group , canvas)
    process_sprite_group( missile_group , canvas)
    process_sprite_group(explosion_group, canvas)
    
    
    # update ship and sprites
    my_ship.update()
   
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [width/2, height/2], 
                          splash_info.get_size())

         
# timer handler that spawns a rock    
def rock_spawner():    
    if len ( rock_group )< 12:
        pos = [random.randrange(0, width), random.randrange(0, height) ]
        while dist ( pos, my_ship.pos) <  my_ship.radius * 3 :
            pos = [random.randrange(0, width), random.randrange(0, height) ]
        a_rock = Sprite( pos, [(random.random()-.5) * (1+ score/10), (random.random()-.5) * (1+ score/10)], 0, (random.random()-0.5)/10 , asteroid_image, asteroid_info)
        rock_group.add(a_rock)


# Keyboard handler
def keydown(key):
    global left, right,up, cw   
    if key == simplegui.KEY_MAP["left"]:
        cw = 1
        left = True        
    elif key == simplegui.KEY_MAP["right"]:
        cw = 0
        right = True        
    elif key == simplegui.KEY_MAP["space"]:        
        my_ship.shot()
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True

 
 
def keyup(key):    
   global left, right,up 
   if key == simplegui.KEY_MAP["left"]:
        left = False
   elif key == simplegui.KEY_MAP["right"]: 
        right = False    
   elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust  =  False
        
            
        
# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)


timer = simplegui.create_timer(2000.0, rock_spawner)


# get things rolling
   
    
frame.start()
