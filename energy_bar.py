import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Energy():
    
    def __init__(self,bg):
        self.energy = 100
        self.background = bg
        self.updates()
    def updates(self,bg=None,damage=0):
        if bg is not None: 
            self.background = bg
        self.energy += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("EN:"+str(self.energy), 1, (0, 0, 255))
        textpos = self.text.get_rect(centerx=self.background.get_width()*.9,centery=self.background.get_height()*.9)
        self.background.blit(self.text, textpos)
    

       