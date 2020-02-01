import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Health():
    
<<<<<<< HEAD
    def __init__(self,screen):
        self.health = 100
        self.updates(0, screen)
        
    def updates(self,damage, screen):
=======
    def __init__(self,bg,health=100):
        self.health = 100
        self.background = bg
        self.updates()
        
    def updates(self,bg=None,damage=0):
        if bg is not None:
            self.background = bg
>>>>>>> 31fe1ec2a5b9f10c5f96259050c90b66d25febe1
        self.health += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))
        textpos = self.text.get_rect(centerx=screen.get_width()*.1,centery=screen.get_height()*.9)
        screen.blit(self.text, textpos)

    def isDead(self):
        return self.health == 0