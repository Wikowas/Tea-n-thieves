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
        self.x = float(x)
        self.y = float(y)
        self.actor = Actor(name)
        self.actor.pos = (x, y)

        # Scaling state
        self.scale = 0.3
        self.base_size = (self.actor.width, self.actor.height)

        # Keep original surface so scaling always starts from the same image
        self.actor_surface_base = self.actor._surf

        # Cached scaled surface
        self.scaled_actor_surface = self.actor_surface_base
        self.rescale()
        
        # Rotation (tracked completely in degrees now)
        self.rotation = 0.0
        self.rotated_scaled_actor_surface = self.scaled_actor_surface

    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )
        self.scaled_actor_surface = pygame.transform.smoothscale(self.actor_surface_base, new_size)

    def rotate(self):
        # Keep the angle within a clean 0-360 degree boundary
        self.rotation = self.rotation % 360
        
        # Pygame's rotate function expects degrees natively
        self.rotated_scaled_actor_surface = pygame.transform.rotate(self.scaled_actor_surface, self.rotation)

    def update(self):
        # Scale controls
        if keyboard.p:
            self.scale += 0.01
        if keyboard.l:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            
        # Rotation controls (1 degree adjustments)
        if keyboard.a:
            self.rotation += 1.0
        if keyboard.d:
            self.rotation -= 1.0
            
        # ALWAYS rescale the base image before applying the rotation
        self.rescale()
        self.rotate()

    def draw(self):
        rect = self.rotated_scaled_actor_surface.get_rect(center=self.actor.pos)
        # draw boat
        screen.blit(self.rotated_scaled_actor_surface, rect)

    def movement(self):
        return

player = Player("boat", WIDTH / 2, HEIGHT / 2)


def update():
    player.update()


def draw():
    screen.clear()
    player.draw()
    screen.draw.text("Boat display (scale & rotate)", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    screen.draw.text(f"Rotation: {player.rotation:.1f}°", (10, 85), color="yellow", fontsize=24)


def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


pgzrun.go()