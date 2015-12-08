import sys
from time import sleep, localtime
from weakref import WeakKeyDictionary

from PodSixNet.Server import Server
from PodSixNet.Channel import Channel

from pygame import *
import pygame

import random

from Game import Game
from TronGame import TronGame

'''class ClientChannel(Channel):
    """
    This is the server representation of a single connected client.
    """

    def __init__(self, *args, **kwargs):
        self.nickname = "anonymous"
        self.id = 0
        Channel.__init__(self, *args, **kwargs)

    def Close(self):
        self._server.DelPlayer(self)

    def handleInput(self, type, input):
        print type
        print input

    ##################################
    ### Network specific callbacks ###
    ##################################

    def Network_input(self, data):
        self.handleInput(int(data['event'].split(':')[0]),int(data['event'].split(':')[1]))

    def Network_message(self, data):
        self._server.SendToAll({"action": "message", "message": data['message'], "who": self.nickname})

    def Network_nickname(self, data):
        self.nickname = data['nickname']
        self._server.SendPlayers()


class Server(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.players = WeakKeyDictionary()
        print 'Server launched'

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
        self.SendToAll({"action": "players", "players": [p.nickname for p in self.players]})

    def SendToAll(self, data):
        [p.Send(data) for p in self.players]

    def SendRenderable(self, renderable):
        self._server.SendToAll({"action": "render", "object": renderable.getData()})

    def Lool(self):
        self.Pump()'''

# get command line argument of server, port
'''if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "host:port"
    print "e.g.", sys.argv[0], "localhost:31425"
    host, port = "localhost:4242".split(":")
    s = Server(localaddr=(host, int(port)))
    s.Launch()
else:
    host, port = sys.argv[1].split(":")
    s = Server(localaddr=(host, int(port)))
    s.Launch()'''

def main():
    game = TronGame(localaddr=("localhost", 4242))
    game.run()

if(__name__ == "__main__"):
    main()
    pygame.quit()