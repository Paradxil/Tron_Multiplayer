from pygame import *
import pygame

class RenderObject():
    def __init__(self,x,y,texture):
        self.rect = Rect(int(x),int(y),texture.get_width(), texture.get_height())
        self.texture = texture

    def render(self, screen, camera=(0,0)):
        screen.blit(self.texture, Rect(self.rect.x - camera[0], self.rect.y - camera[1], self.rect.w, self.rect.h))
