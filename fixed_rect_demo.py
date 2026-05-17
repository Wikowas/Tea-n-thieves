import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Fixed Rect Demo"


# This demo shows the same rotation+scaling transforms, but avoids using the
# transformed image's bounding-box rect to anchor the position.
#
# Instead:
# - keep a fixed center point (actor.pos)
# - compute a rect for drawing by centering the transformed surface on it
# - for the debug outline, also center on the fixed point


class Player:
    def __init__(self, name: str, x: int, y: int):
        self.actor = Actor(name)
        self.actor.pos = (x, y)

        # scale state
        self.scale = 0.3
        self.base_size = (self.actor.width, self.actor.height)

        # keep original surface for transforms
        self.surface_base = self.actor._surf

        # rotation state
        self.rotation = 90

        # current transformed surface
        self.transformed = self.surface_base

        # anchor point stays fixed
        self.center = self.actor.pos

        # rect used only for drawing/debug, always centered on fixed anchor
        self.rect = self.transformed.get_rect(center=self.center)

        self.rescale()

    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )

        # rotate from the ORIGINAL base each time
        rotated = pygame.transform.rotate(self.surface_base, self.rotation)

        # then scale the rotated image
        self.transformed = pygame.transform.scale(rotated, new_size)

        # rect is derived ONLY from centering on fixed anchor
        self.rect = self.transformed.get_rect(center=self.center)

    def update(self):
        if keyboard.w:
            self.scale += 0.01
            self.rescale()

        if keyboard.s:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            self.rescale()

        rot_speed = 1
        if keyboard.a:
            self.rotation = (self.rotation - rot_speed) % 360
            self.rescale()

        if keyboard.d:
            self.rotation = (self.rotation + rot_speed) % 360
            self.rescale()


player = Player("boat", WIDTH // 2, HEIGHT // 2)

# Flash when rect size changes (still expected)
_rect_flash_time = 0.0
_last = (player.rect.width, player.rect.height)


def update():
    global _rect_flash_time, _last

    player.update()

    current = (player.rect.width, player.rect.height)
    if current != _last:
        _rect_flash_time = 0.12
        _last = current

    _rect_flash_time = max(0.0, _rect_flash_time - (1 / 60))


def draw():
    screen.clear()

    screen.draw.text("FIXED-ANCHOR", (10, 10), color="yellow", fontsize=22)

    # draw outline when flashing
    if _rect_flash_time > 0:
        screen.draw.rect(player.rect, (0, 255, 0))
    else:
        screen.draw.rect(player.rect, (255, 0, 0))

    # draw image centered on fixed anchor rect
    screen.blit(player.transformed, player.rect)

    screen.draw.text(f"Scale: {player.scale:.2f}", (10, 40), color="white", fontsize=20)
    screen.draw.text(f"Rotation: {player.rotation:.0f}", (10, 65), color="white", fontsize=20)
    screen.draw.text(f"rect: {player.rect}", (10, 90), color="white", fontsize=16)


pgzrun.go()

