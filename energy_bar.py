import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Energy():
    
    def __init__(self,screen):
        self.energy = 100
<<<<<<< HEAD
       #self.background = bg
        self.updates(0, screen)
        
    def updates(self,damage, screen):
=======
        self.background = bg
        self.updates()
    def updates(self,bg=None,damage=0):
        if bg is not None: 
            self.background = bg
>>>>>>> 31fe1ec2a5b9f10c5f96259050c90b66d25febe1
        self.energy += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("EN:"+str(self.energy), 1, (0, 0, 255))
        textpos = self.text.get_rect(centerx=screen.get_width()*.9,centery=screen.get_height()*.9)
        screen.blit(self.text, textpos)
    

       