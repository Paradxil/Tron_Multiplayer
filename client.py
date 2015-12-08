import sys
from sys import stdin, exit

from renderObject import RenderObject
from pygame import *
import pygame

from PodSixNet.Connection import connection, ConnectionListener

class Client(ConnectionListener):
    def __init__(self, host, port, engine):
        self.Connect((host, port))
        self.engine = engine
    def Loop(self):
        connection.Pump()
        self.Pump()

    '''def InputLoop(self):
        # horrid threaded input loop
        # continually reads from stdin and sends whatever is typed to the server
        while 1:
            connection.Send({"action": "message", "message": stdin.readline().rstrip("\n")})'''

    def sendInput(self, type, input):
        connection.Send({"action": "input", "event": str(type)+":"+str(input)})
        
    #######################################
    ### Network event/message callbacks ###
    #######################################

    '''def Network_players(self, data):
        print "*** players: " + ", ".join([p for p in data['players']])

    def Network_message(self, data):
        print data['who'] + ": " + data['message']'''

    def Network_render(self, data):
        self.engine.addRenderObject(data['object'][0],RenderObject(int(data['object'][1]),int(data['object'][2]),pygame.image.load("sprites/"+data['object'][3])))

    def Network_initDone(self, data):
         connection.Send({"action": "ready"})

    # built in stuff

    def Network_connected(self, data):
        print "You are now connected to the server"

    def Network_error(self, data):
        print 'error:', data['error'][1]
        connection.Close()

    def Network_disconnected(self, data):
        print 'Server disconnected'
        exit()


