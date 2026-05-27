import pgzrun
import pygame
import math
from typing import TYPE_CHECKING
from pgzero.actor import Actor
if TYPE_CHECKING:
    #The IDE reads this, but it will NEVER execute at runtime
    from pygame import keyboard, screen, Actor


class Cannon:
    def __init__ (self, image):
        self.actor = Actor(image)
    def cannon_draw (self, screen, actor, player_pos, rotation,  offset_x = 0, offset_y = 0):
        # draw cannon
        self.r = 30
        #calculating offset from middle of sprite
        self.cannon_x = math.floor(self.r * math.cos(rotation-math.pi + math.pi/2))
        self.cannon_y = math.floor(self.r * math.sin(rotation-math.pi + math.pi/2))
        self.cannon_offset_final = (player_pos[0] - 12 + self.cannon_x, player_pos[1] - self.cannon_y - 6)
        rect = actor.get_rect(center=self.cannon_offset_final)
        #rect = actor.get_rect(center=player_pos)
        screen.blit(self.actor._surf, rect)