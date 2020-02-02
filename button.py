import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Button(pygame.sprite.Sprite):
    
    def __init__(self,bg,txt,x,y):
        self.background = bg
        self.txt = "  "+txt+"  "
        self.x=x 
        self.y=y
        
        font = pygame.font.Font(None, 36)
        self.text = font.render(str(self.txt), 1, (188, 62, 31),(0,0,0))
        self.update()
   
        
        
    def clicked(self):
        print("clicked")
    
    def update(self,bg = None):
        if bg is not None:
            self.background=bg
        textpos = self.text.get_rect(centerx=self.background.get_width()*self.x,centery=
        36+(self.y*self.background.get_height()))
        self.background.blit(self.text, textpos)
        self.rect = textpos
        
       