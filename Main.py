import pgzrun
import pygame


# --- Window Settings ---
WIDTH = 800
HEIGHT = 600
TITLE = "Tea-n-Thieves"


class Boat:
    def __init__(self, x: int, y: int, image_name: str = "boat"):
        # Pygame Zero loads images from images/ automatically
        self.actor = Actor(image_name)
        self.actor.pos = (x, y)

        # Scaling state
        self.scale = 1.0
        self.base_size = (self.actor.width, self.actor.height)

        # We keep a base Surface so scaling always starts from the original.
        # Note: Actor.image cannot be set to a Surface, so we draw our scaled Surface ourselves.
        self.scaled_surf_base = self.actor._surf
        self.scaled_surf = self.scaled_surf_base

    def rescale(self):
        w, h = self.base_size
        new_size = (max(1, int(w * self.scale)), max(1, int(h * self.scale)))
        self.scaled_surf = pygame.transform.smoothscale(self.scaled_surf_base, new_size)

    def update(self):
        # Scale controls
        if keyboard.w:
            self.scale += 0.01
            self.rescale()

        if keyboard.s:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            self.rescale()

    def draw(self):
        # Draw the resized surface centered on the Actor position
        rect = self.scaled_surf.get_rect(center=self.actor.pos)
        screen.blit(self.scaled_surf, rect)


# --- Game Setup ---
boat = Boat(WIDTH // 2, HEIGHT // 2, image_name="boat")


# --- Game Functions ---
def update():
    boat.update()


def draw():
    screen.clear()
    boat.draw()
    screen.draw.text("Boat display test", (10, 10), color="white", fontsize=24)


# --- Event Handlers ---

def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


# --- Start Engine ---
pgzrun.go()

