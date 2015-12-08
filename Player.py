import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

from pygame import *
import pygame

import random

from Renderable import Renderable

class Player(Channel):
    """
    This is the server representation of a single connected client.
    """
    def __init__(self, *args, **kwargs):
        self.id = 0
        self.renderables = []
        self.disconnected = False
        self.ready = False
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
       self.disconnected = True

    def handleInput(self, type, input):
        print type
        print input

    def update(self, delta):
        pass

    def createUniqueRenderable(self, x, y, src):
        return Renderable(x,y,src,str(self.id)+":" + str(len(self.renderables)))

    def addUniqueRenderable(self, x, y, src):
        r = Renderable(x,y,src,str(self.id)+":" + str(len(self.renderables)))
        self.renderables.append(r)
        return r

    ##################################
    ### Network specific callbacks ###
    ##################################

    def Network_input(self, data):
        self.handleInput(int(data['event'].split(':')[0]),int(data['event'].split(':')[1]))

    def Network_ready(self, data):
        self.ready = True

    '''def Network_message(self, data):
        self._server.SendToAll({"action": "message", "message": data['message'], "who": self.nickname})

    def Network_nickname(self, data):
        self.nickname = data['nickname']
        self._server.SendPlayers()'''
