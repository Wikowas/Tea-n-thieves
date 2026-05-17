import pgzrun
import pygame
import time


# --- Debug ---
_last_print = 0.0


# --- Window Settings ---
WIDTH = 800

HEIGHT = 600
TITLE = "Tea-n-Thieves"

class Player:
    def __init__(self, name: str, x: int, y: int):
        self.actor = Actor(name)
        self.actor.pos = (x, y)

        # transform state
        self.scale = 0.3
        self.rotation = 0
        self.base_size = (self.actor.width, self.actor.height)

        # Keep a base Surface to scale from (we draw it ourselves)
        self.actor_surface_base = self.actor._surf
        self.actor_surface = self.actor_surface_base
        self.rotate()
        self.rescale()
        
    def rotate(self):
        self.rotated_actor_surface = pygame.transform.rotate(self.actor_surface_base, self.rotation)
        self.rescale()
        
    def rescale(self):
        self.w, self.h = self.base_size
        self.new_size = (max(1, int(self.w * self.scale)), max(1, int(self.h * self.scale)))
        self.actor_surface = pygame.transform.smoothscale(self.rotated_actor_surface, self.new_size)
        
    # This function runs 60 times per second.
    def update(self):
        # Scale controls
        if keyboard.p:
            self.scale += 0.01
            self.rescale()

        if keyboard.l:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            self.rescale()
        if keyboard.a:
            self.rotation += 1
            self.rotate()
        if keyboard.d:
            self.rotation -= 1
            self.rotate()

    # Called 60 times a second, use to draw actors and text
    def playerdraw(self):
        # Draw the resized surface ourselves.
        self.rect = self.actor_surface.get_rect(center=self.actor.pos)
        screen.blit(self.actor_surface, self.rect)

        
        
        
player = Player("boat", WIDTH/2, HEIGHT/2)


def update():
    player.update()

def draw():
    screen.clear()
    player.playerdraw()
    screen.draw.text("Boat display test", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    #screen.draw.text(f"rotation: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)


# --- Event Handlers ---
def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


# --- Start Engine ---
pgzrun.go()

