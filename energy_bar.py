import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Energy():
    
    def __init__(self,screen):
        self.energy = 100
        self.screen=screen
        self.updates(0)
        


     
    def updates(self,damage=0):

        self.energy += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("EN:"+str(self.energy), 1, (0, 0, 255))
        textpos = self.text.get_rect(centerx=self.screen.get_width()*.9,centery=self.screen.get_height()*.9)
        self.screen.blit(self.text, textpos)
    

       