import pgzrun
import pygame

# --- Window Settings ---
WIDTH = 800
HEIGHT = 600
TITLE = "Tea-n-Thieves"

class Player:
    def __init__(self, name, x, y):
        self.player = Actor(name)
        self.player.pos = (x, y)    
        self.scale = 1.0
        self.base_size = (self.player.width, self.player.height)
        self.scaled_surf_base = self.player._surf
        self.scaled_surf = self.scaled_surf_base

    def rescale(self):
        self.w, self.h = self.base_size
        self.new_size = (max(1, int(self.w * self.scale)), max(1, int(self.h * self.scale)))
        self.scaled_surf = pygame.transform.smoothscale(self.scaled_surf_base, self.new_size)
    
    # This function runs 60 times per second.
    def update(self):
        # Scale controls
        if keyboard.w:
            self.scale += 0.01
            self.rescale()

        if keyboard.s:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            self.rescale()
    # Called 60 times a second, use to draw actors and text
    def draw(self):
        screen.clear()

        # Draw the resized surface ourselves.
        # Keep player.draw() off the screen to avoid using Actor's unscaled image.
        self.rect = self.scaled_surf.get_rect(center=self.player.pos)
        screen.blit(self.scaled_surf, self.rect)
        
        
        
player = Player("boat", WIDTH/2, HEIGHT/2)

def update():
    player.update()
    
def draw():
    screen.clear()
    player.draw()
    screen.draw.text("Boat display test", (10, 10), color="white", fontsize=24)
# --- Event Handlers ---
def on_mouse_down(pos):
        pass

def on_key_down(key):
        pass
    
# --- Start Engine ---
pgzrun.go()