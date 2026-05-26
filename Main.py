import pgzrun
import pygame
import math
from typing import TYPE_CHECKING

# --- Window Settings ---
WIDTH = 800
HEIGHT = 600
TITLE = "Tea-n-Thieves"
center_of_screen = (WIDTH/2, HEIGHT/2)

if TYPE_CHECKING:
    # The IDE reads this, but it will NEVER execute at runtime
    from pygame import keyboard, screen, Actor


class Player:
    def __init__(self, image: str, x: float, y: float):
        #animation
        self.actor = Actor(image)
        self.frame = 0
        self.step = 0
        
        #movement positioning
        self.x = float(x)
        self.y = float(y)
        self.actor.pos = (x, y)
        self.max_speed = 4
        self.rotate_speed = 2
        self.velocity = 0
        self.aceleration = 0.03
        self.friction = 0.03

        # Scaling state
        self.scale = 1
        self.base_size = (self.actor.width, self.actor.height)

        # Keep original surface so scaling always starts from the same image
        self.actor_surface_base = self.actor._surf

        # Cached scaled surface
        self.scaled_actor_surface = self.actor_surface_base
        self.rescale()

        #rotation
        self.rotation = math.pi #-0.535 #make the boat straight
        self.offset = self.rotation
    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )
        self.actor_surface_base = self.actor._surf
        self.scaled_actor_surface = pygame.transform.smoothscale(self.actor_surface_base,new_size,)
    def rotate(self):
        self.rotation_degrees = math.degrees(self.rotation)
        self.rotated_scaled_actor_surface = pygame.transform.rotate(self.scaled_actor_surface, self.rotation_degrees)
        if abs(self.rotation) > 2*math.pi:
            self.rotation = 0
    def update(self):
        # Scale controls
        if keyboard.p:
            self.scale += 0.01
        if keyboard.l:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
        if keyboard.a:
            self.rotation += (1*math.pi)/180 * self.rotate_speed
        if keyboard.d:
            self.rotation -= (1*math.pi)/180 * self.rotate_speed
            
        self.animation()
        self.rotate()
        self.rescale()
        self.movement()

    def draw(self):
        rect = self.rotated_scaled_actor_surface.get_rect(center=self.actor.pos)
        # draw boat
        screen.blit(self.rotated_scaled_actor_surface, rect)

    def movement(self):
        #use of velocity for easing 
        self.actor.pos = (self.x, self.y) 
        self.y -= math.cos(self.rotation - self.offset) * min(self.velocity, self.max_speed) #updating positon
        self.x -= math.sin(self.rotation - self.offset) * min(self.velocity, self.max_speed)
        
        #need to set the animation based off velocity
        self.animation_velocity_tracker = math.floor((self.velocity/self.max_speed)*100*0.6)
        if keyboard.w:
            self.velocity += self.aceleration
            self.friction = 0
            if self.frame < 60:
                self.frame = self.animation_velocity_tracker 
        if keyboard.s:
            if self.frame > 0:
                self.frame = self.animation_velocity_tracker
            if self.friction < 0.03:
                self.friction += 0.01/4
        if self.velocity > self.max_speed:
            self.velocity = self.max_speed
        if self.velocity > 0:
            self.velocity -= self.friction
        if self.velocity < 0:
            self.velocity = 0
        print(self.animation_velocity_tracker)
        #print(round(self.x), round(self.y), "friction:", self.friction, "Velocity: ", round(self.velocity, 2), "Frame:", self.frame, "step:", self.step)
    
    def animation(self):
        self.step = str(math.floor(self.frame/8.6) + 1)
        self.actor.image = self.step

player = Player("boat", WIDTH / 2, HEIGHT / 2)


def update():
    player.update()


def draw():
    screen.clear()
    player.draw()
    screen.draw.text("scale:", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    screen.draw.text(f"velocity: {player.velocity:.2f}", (10, 85), color="yellow", fontsize=24)


def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


pgzrun.go()

