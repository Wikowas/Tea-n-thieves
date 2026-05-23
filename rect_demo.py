import pgzrun
import pygame
import math
from typing import TYPE_CHECKING

# --- Window Settings ---
WIDTH = 800
HEIGHT = 600
TITLE = "Tea-n-Thieves"

if TYPE_CHECKING:
    from pygame import keyboard, screen, Actor


class Player:
    def __init__(self, name: str, x: int, y: int):
        self.actor = Actor(name)
        # Store position as floats for smooth sub-pixel movement
        self.x = float(x)
        self.y = float(y)
        self.actor.pos = (self.x, self.y)

        # Movement Settings
        self.speed = 0.0
        self.max_speed = 4.0
        self.acceleration = 0.1
        self.friction = 0.05

        # Scaling state
        self.scale = 0.3
        self.base_size = (self.actor.width, self.actor.height)

        # Keep original surface safe
        self.actor_surface_base = self.actor._surf

        # Cached states
        self.rotation = 0.0
        self.final_surface = self.actor_surface_base
        self.update_visuals()

    # --- Modular Transformation Pipeline ---
    def get_scaled_surface(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )
        return pygame.transform.smoothscale(self.actor_surface_base, new_size)

    def get_rotated_surface(self, surface_to_rotate):
        return pygame.transform.rotate(surface_to_rotate, self.rotation)

    def update_visuals(self):
        scaled_snapshot = self.get_scaled_surface()
        self.final_surface = self.get_rotated_surface(scaled_snapshot)

    def update(self):
        visual_changed = False

        # 1. Handle Rotation Controls (Turning)
        if keyboard.a:
            self.rotation += 3  # Degrees to turn left
            visual_changed = True
        if keyboard.d:
            self.rotation -= 3  # Degrees to turn right
            visual_changed = True

        # 2. Handle Scale Controls
        if keyboard.p:  # Changed to P/L so W/S can be used for driving!
            self.scale += 0.01
            visual_changed = True
        if keyboard.l:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            visual_changed = True

        if visual_changed:
            self.update_visuals()

        # 3. Handle Speed Controls (Forward / Backward)
        if keyboard.w:
            self.speed += self.acceleration
            if self.speed > self.max_speed:
                self.speed = self.max_speed
        elif keyboard.s:
            self.speed -= self.acceleration
            if self.speed < -self.max_speed / 2:  # Slower in reverse
                self.speed = -self.max_speed / 2
        else:
            # Apply passive friction if no keys are pressed so the boat glides to a stop
            if self.speed > 0:
                self.speed = max(0.0, self.speed - self.friction)
            elif self.speed < 0:
                self.speed = min(0.0, self.speed + self.friction)

        # 4. Math: Translate speed + angle into X and Y movement
        # Pygame's 0 degrees is usually facing Right, but many assets face Up.
        # If your boat graphic points Up naturally, add 90 degrees to the math adjustment.
        angle_radians = math.radians(self.rotation + 90)

        self.x += self.speed * math.cos(angle_radians)
        self.y -= self.speed * math.sin(angle_radians)  # Subtracted because Y goes down in Pygame

        # Keep coordinates bound to screen edges (optional)
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))
        
        # Update underlying actor position
        self.actor.pos = (self.x, self.y)

    def draw(self):
        # Measure the actual final drawn rectangle footprint
        rect = self.final_surface.get_rect(center=self.actor.pos)
        screen.blit(self.final_surface, rect)


player = Player("boat", WIDTH / 2, HEIGHT / 2)


def update():
    player.update()


def draw():
    screen.clear()
    player.draw()
    screen.draw.text("Boat Controls: W/S (Drive), A/D (Steer), P/L (Scale)", (10, 10), color="white", fontsize=24)
    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 45), color="yellow", fontsize=24)
    screen.draw.text(f"Rotation: {player.rotation:.1f}°", (10, 85), color="yellow", fontsize=24)
    screen.draw.text(f"Speed: {player.speed:.2f}", (10, 125), color="cyan", fontsize=24)


def on_mouse_down(pos):
    pass


def on_key_down(key):
    pass


pgzrun.go()