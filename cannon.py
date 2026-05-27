import pgzrun
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # The IDE reads this, but it will NEVER execute at runtime
    from pygame import keyboard, screen, Actor


class Cannon:
    def __init__ (self, image):
        self.image = image 
    def cannon_draw (self, draw_location, offset_x, offset_y):
        # draw cannon
        #figure out what (center=self.actor.pos) does
        rect = draw_location.get_rect(center=self.actor.pos)
        screen.blit(self.image, rect)