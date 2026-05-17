import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Rect Demo"


class Player:
    def __init__(self, name: str, x: int, y: int):
        self.actor = Actor(name)
        self.actor.pos = (x, y)

        # scaling state
        self.scale = 0.3
        self.base_size = (self.actor.width, self.actor.height)

        # base surface (scale from this every time)
        self.scaled_actor_surface_base = self.actor._surf
        self.scaled_actor_surface = self.scaled_actor_surface_base

        # rotation state (degrees)
        # Start at 90 degrees
        self.rotation = 90


        self.rect = self.scaled_actor_surface.get_rect(center=self.actor.pos)
        self.rescale()


        # used to detect rect changes so we can flash
        self._last_w = self.rect.width
        self._last_h = self.rect.height

        self._last_cx = self.rect.centerx
        self._last_cy = self.rect.centery

    def rescale(self):
        w, h = self.base_size
        new_size = (
            max(1, int(w * self.scale)),
            max(1, int(h * self.scale)),
        )

        # Smoother rotation while held keys are down:
        # - update rotation in larger steps, but draw from a single fresh transform
        # - use smoothscale (scaling) and let rotate handle rotation
        rotated_base = pygame.transform.rotate(self.scaled_actor_surface_base, self.rotation)
        self.scaled_actor_surface = pygame.transform.scale(rotated_base, new_size)



        self.rect = self.scaled_actor_surface.get_rect(center=self.actor.pos)


    def update(self):
        # Scale controls
        if keyboard.w:
            self.scale += 0.01
            self.rescale()
        if keyboard.s:
            self.scale -= 0.01
            self.scale = max(0.2, self.scale)
            self.rescale()

        # Rotation controls
        # Rotation speed (degrees per frame-ish)
        rot_speed = 1

        if keyboard.a:
            self.rotation = (self.rotation - rot_speed) % 360
            self.rescale()
        if keyboard.d:
            self.rotation = (self.rotation + rot_speed) % 360
            self.rescale()



    def rect_changed(self) -> bool:
        changed = (
            self.rect.width != self._last_w
            or self.rect.height != self._last_h
            or self.rect.centerx != self._last_cx
            or self.rect.centery != self._last_cy
        )
        if changed:
            self._last_w = self.rect.width
            self._last_h = self.rect.height
            self._last_cx = self.rect.centerx
            self._last_cy = self.rect.centery
        return changed


player = Player("boat", WIDTH / 2, HEIGHT / 2)

_rect_flash_time = 0.0


def update():
    global _rect_flash_time
    player.update()

    # flash outline briefly when the rect changes (i.e., size changes)
    if player.rect_changed():
        _rect_flash_time = 0.12

    # clock.dt isn't available in all pgzero versions; dt is 1/60 here.
    _rect_flash_time = max(0.0, _rect_flash_time - (1/60))



def draw():
    screen.clear()

    if _rect_flash_time > 0:
        screen.draw.text("RECT OUTLINE", (10, 10), color="yellow", fontsize=22)
        screen.draw.rect(player.rect, (255, 0, 0))

    else:
        screen.draw.text("BOAT", (10, 10), color="yellow", fontsize=22)
        screen.blit(player.scaled_actor_surface, player.rect)

    screen.draw.text(
        f"Scale: {player.scale:.2f}",
        (10, 40),
        color="white",
        fontsize=20,
    )
    screen.draw.text(
        f"rect: {player.rect}",
        (10, 65),
        color="white",
        fontsize=16,
    )


pgzrun.go()

