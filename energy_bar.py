import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Energy():
    
    def __init__(self,screen):
        self.energy = 3
        self.screen=screen
        self.update()
        
    def update(self, damage = 0):

        self.energy += damage
        font = pygame.font.Font("data/dpcomic.ttf", 36)
        self.text = font.render("EN:"+str(self.energy), 1, (0, 0, 255))
        textpos = self.text.get_rect(centerx=self.screen.get_width()*.1,centery=self.screen.get_height()*.9)
        self.screen.blit(self.text, textpos)


       