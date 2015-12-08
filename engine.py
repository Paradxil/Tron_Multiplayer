from pygame import *
import pygame
from client import Client
from renderObject import RenderObject

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = display.set_mode([800,600], RESIZABLE)
        self.timer = time.Clock()
        self.renderObjects = {}
        self.camera = [0,0]
        self.followingObject = ""
        self.client = Client("localhost", 4242, self)

    def addRenderObject(self, name, obj):
        self.renderObjects[name] = obj

    def update(self, delta):
        self.client.Loop()
        if self.followingObject != "":
            self.camera = self.renderObjects[self.followingObject].rect.center

    def getInput(self):
        for event in pygame.event.get():
            #send events to the server
            if event.type == KEYDOWN:
                self.client.sendInput(event.type,event.key)

    #used to update camera
    def setFollowingObject(self, name):
        self.followingObject = name

    def render(self):
        self.screen.fill(Color('#000000'))
        for obj in self.renderObjects.values():
            obj.render(self.screen, self.camera)

        pygame.display.flip()

    def run(self):
        while True:
            delta = self.timer.tick(60)
            self.update(delta)
            self.getInput()
            self.render()
