import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Shield():
    
    def __init__(self,screen,x=.1,y=.8):
        self.defense = 0
        self.screen=screen
        self.x = x 
        self.y = y
        self.update()

        
    def update(self):
        font = pygame.font.Font("data/dpcomic.ttf", 36)
        self.text = font.render("SH:"+str(self.defense), 1, (0, 0, 255))
        textpos = self.text.get_rect(centerx=self.screen.get_width()*self.x,centery=self.screen.get_height()*self.y)
        self.screen.blit(self.text, textpos)


       