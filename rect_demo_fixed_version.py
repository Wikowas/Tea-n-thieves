import pgzrun
import pygame

# Hold onto the Actor class only if you truly need it; this demo uses no class.

WIDTH = 800
HEIGHT = 600

boat_surf = Actor("boat")._surf
boat_center = (WIDTH // 2, HEIGHT // 2)

rot = 0


def update():
    global rot
    if keyboard.left:
        rot -= 2
    if keyboard.right:
        rot += 2


def draw():
    screen.clear()
    img = pygame.transform.rotate(boat_surf, rot)
    screen.blit(img, img.get_rect(center=boat_center))


pgzrun.go()

