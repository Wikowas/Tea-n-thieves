import pgzrun
import pygame

# --- Window Settings ---
WIDTH = 800
HEIGHT = 600
TITLE = "Tea-n-Thieves"
center_of_screen = (WIDTH/2, HEIGHT/2)


class Player:
    def __init__(self, name: str, x: int, y: int):
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
        #rotation
        self.rotation = 0
    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )
        self.scaled_actor_surface = pygame.transform.smoothscale(self.actor_surface_base,new_size,)
    def rotate(self):
        self.rotated_scaled_actor_surface = pygame.transform.rotate(self.scaled_actor_surface, self.rotation)

    def update(self):
        # Scale controls
        if keyboard.w:
            self.scale += 0.01
        if keyboard.s:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
        if keyboard.a:
            self.rotation += 1
        if keyboard.d:
            self.rotation -= 1
        self.rotate()
        self.rescale()
    def draw(self):
        rect = self.rotated_scaled_actor_surface.get_rect(center=self.actor.pos)

        # draw boat
        screen.blit(self.rotated_scaled_actor_surface, rect)

player = Player("boat", WIDTH / 2, HEIGHT / 2)


def update():
    player.update()


def draw():
    screen.clear()
    player.draw()
    screen.draw.text("Boat display (scale only)", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    screen.draw.text(f"rotation: {player.rotation:.2f}", (10, 85), color="yellow", fontsize=24)


def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


pgzrun.go()

