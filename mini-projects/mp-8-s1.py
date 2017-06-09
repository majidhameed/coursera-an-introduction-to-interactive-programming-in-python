# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
score = 0
lives = 3
time = 0
started = False
number_of_rocks = 12
difficulty = 1000 #easy: 1000, hard: 100, madness: 10

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
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris_blend.png")

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
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")
asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

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

def process_sprite_group(canvas, sprite_group):
    for sprite in list(sprite_group):
        sprite.draw(canvas)
        if not sprite.update():
            sprite_group.remove(sprite)
        
def group_collide(group, other_object):
    collision = 0
    for sprite in list(group):
        if sprite.collide(other_object):
            group.remove(sprite)
            collision += 1
            explosion_group.add(Sprite(sprite.pos, [0, 0], 0, 0, 
                                       explosion_image, explosion_info, explosion_sound))
    return collision

def group_group_collide(group, other_group):
    collision = 0
    for sprite in list(group):
        if group_collide(other_group, sprite) > 0:
            group.remove(sprite)
            collision += 1
    return collision


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
        #canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)            
        
        #draw the ship, perhaps more than once if it is near the edge.
        for x in (self.pos[0] - width, self.pos[0], self.pos[0] + width):
            for y in (self.pos[1] - height, self.pos[1], self.pos[1] + height ):
                if (-self.image_center[0] < x < (width + self.image_center[0])) and \
                   (-self.image_center[1] < y < (height + self.image_center[1])):
                    canvas.draw_image(self.image, self.image_center, self.image_size, (x,y), self.image_size, self.angle)   
                
    def update(self):
        # turn ship
        self.angle += self.angle_vel
        
        # update position 
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        # update friction 
        self.vel[0] *= (1 - 0.02)
        self.vel[1] *= (1 - 0.02)
        
        # update velocity 
        if self.thrust:
            vector = angle_to_vector(self.angle)
            self.vel[0] = self.vel[0] + vector[0] * 0.2
            self.vel[1] = self.vel[1] + vector[1] * 0.2
      
    def rotate(self, direction):
        if direction == "left":
            self.angle_vel += -0.05
        elif direction == "right":
            self.angle_vel += 0.05
        else:
            self.angle_vel = 0
        
    def accelerate(self, state):
        if state:
            self.thrust = True
            self.image_center = [135, 45]
            ship_thrust_sound.play()
        else:
            self.thrust = False
            self.image_center = [45, 45]
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
    
    def shoot(self):
        global missile_group
      
        vector = angle_to_vector(self.angle)
        missile_group.add(Sprite([self.pos[0] + vector[0] * self.radius, 
                                  self.pos[1] + vector[1] * self.radius], 
                                 [self.vel[0] + vector[0] * 5, 
                                  self.vel[1] + vector[1] * 5], 
                                 self.angle, 0, missile_image, missile_info, missile_sound))
        
        
    
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
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0] * self.age, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        # rotate sprite 
        self.angle += self.angle_vel       
        
        # update position 
        self.pos[0] = (self.pos[0] + self.vel[0]) % width
        self.pos[1] = (self.pos[1] + self.vel[1]) % height
        
        #increment age and test lifespan
        self.age += 1
        if self.age < self.lifespan:
            return True
        else:
            return False
        
    def collide(self, other):
        if dist(self.pos, other.pos) < self.radius + other.radius:
            return True
        else:
            return False
        
           
def draw(canvas):
    global time, ship_info, lives, score, rock_group, missile_group, started
    
    # animate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])

    # draw and update ship
    my_ship.draw(canvas)
    my_ship.update()
    
    # draw and update missiles
    process_sprite_group(canvas, missile_group)
    
    # draw and update explosions
    process_sprite_group(canvas, explosion_group)
    
    if started:
        # draw and update rocks
        process_sprite_group(canvas, rock_group)
          
        # collides 
        score += group_group_collide(missile_group, rock_group) * 10
        lives -= group_collide(rock_group, my_ship)
        if lives <= 0:
            started = False
            lives = 0
    else:
        canvas.draw_image(splash_image, splash_info.center, splash_info.size, [width / 2, height / 2], splash_info.size)
        rock_group = set([])
        soundtrack.pause()

    # lives and score
    canvas.draw_text("Lives", (25, 35), 18, "White")
    canvas.draw_text(str(lives), (25, 65), 18, "White")
    canvas.draw_text("Score", (width - 100, 35), 18, "White")
    canvas.draw_text(str(score), (width - 100, 65), 18, "White")
            
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len(rock_group) < number_of_rocks:
        # to avoid collision with ship when a rock is spawned
        position = [random.randrange(width), random.randrange(height)]
        while ((my_ship.pos[0] - 20 < position[0] < my_ship.pos[0] + my_ship.radius + asteroid_info.get_radius() + 20) or 
              (my_ship.pos[0] - my_ship.radius - asteroid_info.get_radius() - 20 < position[0] < my_ship.pos[0] + 20) or
              (my_ship.pos[1] - 20 < position[1] < my_ship.pos[1] + my_ship.radius + asteroid_info.get_radius() + 20) or 
              (my_ship.pos[1] - my_ship.radius - asteroid_info.get_radius() - 20 < position[1] < my_ship.pos[1] + 20)):
            position = [random.randrange(width), random.randrange(height)]
       
        # increase velocity of rocks based on the score
        velocity = [random.randrange(-10, 11) / 10 + score * random.choice([-1, 1]) / difficulty, 
                    random.randrange(-10, 11) / 10 + score * random.choice([-1, 1]) / difficulty]
        
        asteroid_image = random.choice([asteroid_image1, asteroid_image2, asteroid_image3])
        
        rock_group.add(Sprite(position, velocity, 
                        0, random.randrange(-10, 11) / 100, asteroid_image, asteroid_info))
    

# key handlers
def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.rotate("left")
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.rotate("right")
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.accelerate(True)
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]:
        my_ship.rotate("stop")
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.accelerate(False)
        
   
def mouseclick(pos):
    global started, lives, score
    
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    if (not started) and inwidth and inheight:
        lives = 3
        score = 0
        started = True
        soundtrack.rewind()
        soundtrack.play()

# difficulty buttons
def easy():
    global difficulty
    if not started:
        difficulty = 1000
        diff.set_text("Difficulty: Easy")
    
def hard():
    global difficulty
    if not started:
        difficulty = 100
        diff.set_text("Difficulty: Hard")

def madness():
    global difficulty
    if not started:
        difficulty = 10
        diff.set_text("Difficulty: Madness")
    
# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([]) 
missile_group = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouseclick)

diff = frame.add_label("Difficulty: Easy")
frame.add_button("Easy", easy, 100)
frame.add_button("Hard",  hard, 100)
frame.add_button("Madness", madness, 100)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()


