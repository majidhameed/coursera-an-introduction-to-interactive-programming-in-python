# Mini-Project-7
# Implementation of Game - Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0
angle_vel_degrees = 5
fwd_vector = [0.3, 0.3]
friction = fwd_vector[0]/23
fire_acc = 10

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

def init_art():
    global debris_info, debris_image, nebula_info, nebula_image, splash_info, splash_image
    global ship_info, ship_image, missile_info, missile_image, asteroid_info, asteroid_image
    global explosion_info, explosion_image, explosion_sound
    
    global soundtrack, missile_sound, ship_thrust_sound 
    
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
    # To show shif with thurst on add 90 to the ImageInfo.x
    ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
    
    # missile image - shot1.png, shot2.png, shot3.png
    missile_info = ImageInfo([5,5], [10, 10], 3, 50)
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
    
    ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
    explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

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
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0],self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:    
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
 
    def update(self):
        
        if self.thrust:
            angle_vector = angle_to_vector(self.angle)
            self.vel[0] += angle_vector[0] * fwd_vector[0]
            self.vel[1] += angle_vector[1] * fwd_vector[1]
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height
        self.angle += self.angle_vel
        self.vel[0] *= 1-friction
        self.vel[1] *= 1-friction
        
    def set_angle_vel(self, angle_vel):
        self.angle_vel = angle_vel
        
    def thurst(self, on):
        if on:
            self.thrust = True
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            self.thrust = False
            ship_thrust_sound.pause()
        
     
    def shoot(self):
        global a_missile
        angle_vector = angle_to_vector(self.angle)
        vel=[0,0]
        vel[0] = self.vel[0]+ angle_vector[0] * fwd_vector[0] * fire_acc
        vel[1] = self.vel[1]+ angle_vector[1] * fwd_vector[1] * fire_acc
        a_missile = Sprite([self.pos[0]+angle_vector[0]*self.radius, self.pos[1]+angle_vector[1]*self.radius], vel, self.angle, 0, missile_image, missile_info, missile_sound) 
    
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
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

def init():
    global my_ship, a_rock, a_missile
    # initialize ship and two sprites
    my_ship = Ship([width/2, height/2], [0, 0], 0, ship_image, ship_info)
    a_missile=None
    rock_spawner()
    
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    if wtime == 0: 
        wtime += 0.1
    
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])
    
    canvas.draw_text('Lives',    [width/15,height/12], 20, 'White')
    canvas.draw_text(str(lives), [width/15,height/8], 20, 'White')
        
    canvas.draw_text('Score',    [width-width/8,height/12], 20, 'White')
    canvas.draw_text(str(score), [width-width/8,height/8], 20, 'White')
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    
    if a_missile!=None:
        a_missile.draw(canvas)
        a_missile.update()
        
    # update ship and sprites
    my_ship.update()
    a_rock.update()

def get_rand_num():
    return (-1,1)[(random.randint(0,1))]*random.random()
    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    a_rock = Sprite([random.randrange(0,width), random.randrange(0,height)], (get_rand_num(),get_rand_num()), 0, math.radians(get_rand_num()*angle_vel_degrees), asteroid_image, asteroid_info)

def turn(direction):
    my_ship.set_angle_vel(math.radians(direction*angle_vel_degrees))

def thurst(on):
    my_ship.thurst(on)

def shoot_missile(shoot_count):
    my_ship.shoot()
    
def do_nothing(nothing):
    pass

key_down_map = {
    'left':  [turn,-1], 
    'right': [turn,1], 
    'up' : [thurst, True], 
    'space': [shoot_missile, 0]
}

key_up_map = {
    'left':  [turn,0], 
    'right': [turn,0], 
    'up' : [thurst, False], 
    'space': [do_nothing, 0]
}       


# ship control keyhanders
def keydown(key):
    for k in key_down_map:
        if key == simplegui.KEY_MAP[k]:
            key_down_map[k][0](key_down_map[k][1])
            break

def keyup(key):
    for k in key_up_map:
        if key == simplegui.KEY_MAP[k]:
            key_up_map[k][0](key_up_map[k][1])
            break
            
init_art()
init()

# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# register handlers
frame.set_draw_handler(draw)

# register key handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

    
