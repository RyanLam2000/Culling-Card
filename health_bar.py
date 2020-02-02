import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Health():
    

    def __init__(self,screen):
        self.health = 100
        self.screen=screen
        self.updates(0)
        
    def updates(self,damage=0):
        self.health += damage
        font = pygame.font.Font(None, 36)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))
        textpos = self.text.get_rect(centerx=self.screen.get_width()*.1,centery=self.screen.get_height()*.9)
        self.screen.blit(self.text, textpos)

    def isDead(self):
        return self.health == 0