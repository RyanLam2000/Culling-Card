import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Button(pygame.sprite.Sprite):
    
    def __init__(self,screen,txt,x,y):
        self.screen = screen
        self.txt = "  "+txt+"  "
        self.x=x 
        self.y=y
        
        font = pygame.font.Font("data/dpcomic.ttf", 36)
        self.text = font.render(str(self.txt), 1, (188, 62, 31),(0,0,0))
        self.update()
   
        
        
    def clicked(self):
        print("clicked")
    
    def update(self):
        textpos = self.text.get_rect(centerx=self.screen.get_width()*self.x,centery=
        36+(self.y*self.screen.get_height()))
        self.screen.blit(self.text, textpos)
        self.rect = textpos
        
       