# Mini-Project-8
# Implementation of Game - RiceRocks(Asteriods)
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0

SHIP_ANGLE_VEL_DEGREES = 3
MAX_ROCKS = 12
MAX_ROCK_ANGLE_DEGREES = 9
MAX_ROCK_VEL = 1.11
MIN_SHIP_ROCK_DIST = 9

FWD_VECT = [0.3, 0.3]
FRICTION = 1-FWD_VECT[0]/11
FIRE_ACC = 21

started = False

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
    #                 debris1_blue.png, debris1_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
    debris_info = ImageInfo([320, 240], [640, 480])
    debris_image = (simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_brown.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris1_blue.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_brown.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris3_blue.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_brown.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris4_blue.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png"))
    
    # nebula images - nebula_brown.png, nebula_blue.png
    nebula_info = ImageInfo([400, 300], [800, 600])
    nebula_image = (simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png"),
                    simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png"))
    
    # splash image
    splash_info = ImageInfo([200, 150], [400, 300])
    splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")
    
    # ship image
    ship_info = ImageInfo([45, 45], [90, 90], 35)
    ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
    
    # missile image - shot1.png, shot2.png, shot3.png
    missile_info = ImageInfo([5,5], [10, 10], 3, 50)
    missile_image = (simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png"),
                     simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png"),
                     simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png"))
    
    # asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
    asteroid_info = ImageInfo([45, 45], [90, 90], 40)
    asteroid_image = (simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png"),
                      simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png"),
                      simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png"))
    
    # animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
    explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
    explosion_image = (simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png"),
                       simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png"),
                       simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png"),
                       simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png"))
    
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
            self.vel[0] += angle_vector[0] * FWD_VECT[0]
            self.vel[1] += angle_vector[1] * FWD_VECT[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height
        self.angle += self.angle_vel
        self.vel[0] *= FRICTION
        self.vel[1] *= FRICTION
        
    def set_angle_vel(self, angle_vel):
        self.angle_vel = angle_vel
        
    def set_thurst(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
     
    def shoot(self):
        angle_vector = angle_to_vector(self.angle)
        vel=[0,0]
        vel[0] = self.vel[0]+ angle_vector[0] * FWD_VECT[0] * FIRE_ACC
        vel[1] = self.vel[1]+ angle_vector[1] * FWD_VECT[1] * FIRE_ACC
        a_missile = Sprite([self.pos[0]+angle_vector[0]*self.radius, self.pos[1]+angle_vector[1]*self.radius], vel, self.angle, 0, missile_image[(lives+score)%len(missile_image)], missile_info, missile_sound) 
        missile_group.add(a_missile)
       
    def get_position(self):
        return self.pos
        
    def get_radius(self):
        return self.radius        
    
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
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0]*self.age,self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:    
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = self.pos[0] % width
        self.pos[1] = self.pos[1] % height
        self.age+=1
        return self.age<self.lifespan
    
    def get_position(self):
        return self.pos
        
    def get_radius(self):
        return self.radius
        
    def collide(self,other):
        return dist(self.pos,other.get_position())<=self.radius+other.get_radius()
        
def init():
    global my_ship, rock_group, missile_group, lives, score, explosion_group
    rock_group = set([])
    missile_group = set([])
    explosion_group = set([])
    
    my_ship = Ship([width/2, height/2], [0, 0], 0, ship_image, ship_info)
    
    if started:
        lives = 3
        score = 0
        soundtrack.rewind()
        soundtrack.play()
    else:
        soundtrack.pause()
    

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, score
    
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        init()

def process_sprite_group(canvas,sprite_set):
    for sprite in list(sprite_set):
        sprite.draw(canvas)
        if not sprite.update():
            sprite_set.remove(sprite)
        
def group_collide(sprite_set,other_sprite):
    collision_count = 0
    for sprite in list(sprite_set):
        if sprite.collide(other_sprite):
            a_explosion = Sprite(sprite.get_position(), [0,0], 0,0, explosion_image[time%4], explosion_info)
            explosion_group.add(a_explosion)
            sprite_set.remove(sprite)
            collision_count+=1
            explosion_sound.rewind()
            explosion_sound.play()
    return collision_count

def group_group_collide(first_group, second_group):
    hit_count = 0
    for sprite in list(first_group):
        if group_collide(second_group,sprite)>0:
            first_group.remove(sprite)
            hit_count+=1
    return hit_count
        
def draw(canvas):
    global time, started, lives, score
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image[(time//(60*10))%len(nebula_image)], nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    
    canvas.draw_image(debris_image[score//10%len(debris_image)], [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image[score//10%len(debris_image)], [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])
    
    canvas.draw_text('Lives',    [width/15,height/12], 20, 'White')
    canvas.draw_text(str(lives), [width/15,height/8], 20, 'White')
        
    canvas.draw_text('Score',    [width-width/8,height/12], 20, 'White')
    canvas.draw_text(str(score), [width-width/8,height/8], 20, 'White')
    
    # draw ship
    my_ship.draw(canvas)
    my_ship.update()
    
    # draw/update rocks, missiles
    process_sprite_group(canvas,rock_group)
    process_sprite_group(canvas,missile_group)
    process_sprite_group(canvas,explosion_group)
    
    # game over
    if lives==0:
        started=False
        init()
    
    # update lives
    if group_collide(rock_group,my_ship)>0:
        lives-=1
    
    # update score
    score+=group_group_collide(missile_group, rock_group)
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [width/2, height/2], 
                          splash_info.get_size())

def get_rand_vel():
    return (time//120+score+random.random()) % MAX_ROCK_VEL * random.choice((-1,1))

def get_rock_cord():
    return (my_ship.get_position()[0] + my_ship.get_radius()*2 + random.randrange(0,width)*random.choice((-1,1)),
            my_ship.get_position()[1] + my_ship.get_radius()*2 + random.randrange(0,height)*random.choice((-1,1)))

def get_new_rock():
    rock_cord = get_rock_cord()
    distance = (rock_cord, my_ship.get_position()) 
    while distance <= my_ship.get_radius()*2:
        print "TOO NEAR"
        rock_cord = get_rock_cord()
        distance = (rock_cord, my_ship.get_position()) 
    
    angle = (time//60+score+random.random()) % MAX_ROCK_ANGLE_DEGREES * random.choice((-1,1))
    vel = [ get_rand_vel(),get_rand_vel() ]
    return Sprite(rock_cord, vel, 0, math.radians(angle), asteroid_image[time%len(asteroid_image)], asteroid_info)
    
    
# timer handler that spawns a rock    
def rock_spawner():
    if started and len(rock_group)<=MAX_ROCKS:
        rock_group.add(get_new_rock())

def turn(direction):
    my_ship.set_angle_vel(math.radians(direction*SHIP_ANGLE_VEL_DEGREES))

def thurst(on):
    my_ship.set_thurst(on)

def shoot_missile(shoot_count):
    my_ship.shoot()
    
def do_nothing(nothing):
    pass

key_map = {
    'left':  [turn,-1], 'right': [turn,1], 'leftku':  [turn,0], 'rightku': [turn,0], 
    'up' : [thurst, True], 'upku' : [thurst, False], 
    'space': [shoot_missile, 0], 'spaceku': [do_nothing, 0]
}    

# ship control keyhanders
def keydown(key):
    for k in key_map:
        if key == simplegui.KEY_MAP[k]:
            key_map[k][0](key_map[k][1])
            break

def keyup(key):
    for k in key_map:
        if key == simplegui.KEY_MAP[k]:
            key_map[k+'ku'][0](key_map[k+'ku'][1])
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
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
