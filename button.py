import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Button(pygame.sprite.Sprite):
    
    def __init__(self,bg,txt,x,y):
        self.background = bg
        self.text = "  "+txt+"  "
        font = pygame.font.Font(None, 36)
        self.text = font.render(self.text, 1, (188, 62, 31),(0,0,0))
        textpos = self.text.get_rect(centerx=self.background.get_width()*x,centery=
        36+(y*self.background.get_height()))
        self.background.blit(self.text, textpos)
        self.rect = textpos
  
        
    def clicked(self):
        print("clicked")
        pass

       