import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Card(pygame.sprite.Sprite):
    
    def __init__(self,slot):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        #position in deck
        self.slot = slot 
        
        #Load image and scale down
        self.full_img = load_image("download.png", -1)[0]
        self.image = pygame.transform.scale(self.full_img,(50,75))
        #Card hitbox
        self.rect = self.image.get_rect()
        
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
 
        #set position = width * slot
        self.card_width = self.image.get_size()[0];
        self.rect.topleft = (screen.get_width()*.25)+self.card_width*slot, screen.get_size()[1]-100
        self.selected = False
    
    def clicked(self):
        """Update in response to click
        """
        if not self.selected:
            self.rect.topleft = (self.rect.topleft[0],self.rect.topleft[1]-20) 
            self.selected = True
       