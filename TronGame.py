from Game import Game
from Renderable import Renderable
from Player import Player
from pygame import *
import random

class LightBike(Player):
    def __init__(self, *args, **kwargs):
        Player.__init__(self, *args, **kwargs)
        self.cells = []
        self.dir = 1
        self.x = 40
        self.y = 30
        self.dead = False

    def update(self, delta, otherCells = []):
        if not self.dead:
            if self.dir == 0:
                self.y -= 1
            elif self.dir == 1:
                self.x += 1
            elif self.dir == 2:
                self.y += 1
            elif self.dir == 3:
                self.x -= 1
            if self.x < 0 or self.y < 0 or self.x >= 80 or self.y >= 60:
                self.dead = True
            if [self.x,self.y] in self.cells or [self.x,self.y] in otherCells:
                self.dead = True
            self.cells.append([self.x,self.y])
            self.addUniqueRenderable(self.x*10,self.y*10,"blue.png")

    def handleInput(self, type, input):
        if type == KEYDOWN:
            if input == K_UP:
                self.dir = 0
            if input == K_DOWN:
                self.dir = 2
            if input == K_RIGHT:
                self.dir = 1
            if input == K_LEFT:
                self.dir = 3

class TronGame(Game):
    channelClass = LightBike
    def __init__(self, *args, **kwargs):
        Game.__init__(self, *args, **kwargs)
        self.updatet = 0
        self.speed = 40

    def update(self, delta):
        self.updatet += delta

        if self.updatet>self.speed:
            self.updatet = 0
            for p in self.players:
                if p.ready:
                    p.update(delta)