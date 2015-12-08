import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

import random

from pygame import *
import pygame

from Player import Player
from Renderable import Renderable

class Game(Server):
    channelClass = Player
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        pygame.init()
        self.players = WeakKeyDictionary()
        self.renderables = []
        self.timer = time.Clock()
        print 'Server launched'

    def update(self, delta):
        for p in self.players:
            if p.ready and p.connected:
                p.update(delta)

    def createUniqueRenderable(self, x, y, src):
        return Renderable(x,y,src,str(len(self.renderables)))

    def addUniqueRenderable(self, x, y, src):
        r = Renderable(x,y,src,str(len(self.renderables)))
        self.renderables.append(r)
        return r

    def render(self):
        for r in self.renderables:
            if r.updated:
                self.SendRenderable(r)
                r.updated = False

        for p in self.players:
            for r in p.renderables:
                if r.updated:
                    self.SendRenderable(r)
                    r.updated = False

    def run(self):
        while True:
            delta = self.timer.tick(60)
            self.Loop()
            self.update(delta)
            self.render()

    def Connected(self, channel, addr):
        channel.id = len(self.players)
        self.AddPlayer(channel)

    def AddPlayer(self, player):
        print "New Player" + str(player.addr)
        self.players[player] = True
        self.SendPlayers()
        print "players", [p for p in self.players]

    def DelPlayer(self, player):
        print "Deleting Player" + str(player.addr)
        del self.players[player]
        self.SendPlayers()

    def SendPlayers(self):
        for p in self.players:
            for r in p.renderables:
                self.SendRenderable(r)
        for r in self.renderables:
            self.SendRenderable(r)
        self.SendToAll({"action": "initDone", "object": "Sent all data."})

    def SendToAll(self, data):
        [p.Send(data) for p in self.players]

    def SendRenderable(self, renderable):
        self.SendToAll({"action": "render", "object": renderable.getData()})

    def Loop(self):
        self.Pump()

