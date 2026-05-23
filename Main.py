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
    def __init__(self, name: str, x: float, y: float):
        self.actor = Actor(name)

        #movement positioning
        self.x = float(x)
        self.y = float(y)
        self.actor.pos = (x, y)
        self.max_speed = 10
        self.rotate_speed = 2
        self.velocity = 0
        self.aceleration = 0.05
        self.friction = 0.03

        # Scaling state
        self.scale = 0.3
        self.base_size = (self.actor.width, self.actor.height)

        # Keep original surface so scaling always starts from the same image
        self.actor_surface_base = self.actor._surf

        # Cached scaled surface
        self.scaled_actor_surface = self.actor_surface_base
        self.rescale()

        #rotation
        self.rotation = -0.535 #make the boat straight
        self.offset = -0.535
    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )
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
        if keyboard.w:
            self.velocity += self.aceleration
        
        if self.velocity > self.max_speed:
            self.velocity = self.max_speed
        if self.velocity > 0:
            self.velocity -= self.friction
        print(round(self.x), round(self.y), "aceleration:", self.aceleration, "Velocity: ", self.velocity)


player = Player("boat", WIDTH / 2, HEIGHT / 2)


def update():
    player.update()


def draw():
    screen.clear()
    player.draw()
    screen.draw.text("Boat displsay (scale only)", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    screen.draw.text(f"rotation: {player.rotation:.2f}", (10, 85), color="yellow", fontsize=24)


def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


pgzrun.go()

