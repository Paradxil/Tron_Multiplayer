from pygame import *
import pygame
from engine import Engine

DISPLAY = [800,600]
def main():
    engine = Engine()
    engine.run()

if(__name__ == "__main__"):
    main()
    pygame.quit()