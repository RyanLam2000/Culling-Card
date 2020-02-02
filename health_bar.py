import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Health():


    def __init__(self,screen,x=.1,y=.85):
        self.health = 25
        self.screen=screen
        self.x = x 
        self.y = y
        self.update()
   

    def update(self, damage = 0):

        self.health += damage
        font = pygame.font.Font("data/dpcomic.ttf", 36)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))

        textpos = self.text.get_rect(centerx=self.screen.get_width()*self.x,centery=self.screen.get_height()*self.y)
        self.screen.blit(self.text, textpos)

    def isDead(self):
        return self.health <= 0