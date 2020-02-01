import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Health():
    
    def __init__(self,bg,health=100):
        self.health = 100
        self.background = bg
        self.updates()
        
    def updates(self,bg=None,damage=0):
        if bg is not None:
            self.background = bg
        self.health += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))
        textpos = self.text.get_rect(centerx=self.background.get_width()*.1,centery=self.background.get_height()*.9)
        self.background.blit(self.text, textpos)
    

       