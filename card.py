import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Card(pygame.sprite.Sprite):
    
    def __init__(self,slot=-1, img = "download.png"):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        #position in deck
        self.slot = slot
        self.img = img
        self.selected = False
        self.update()
       
    def clicked(self):
        """Update in response to click
        """
        if not self.selected:
            self.rect.topleft = (self.rect.topleft[0],self.rect.topleft[1]-20) 
            self.selected = True
        
            
    
    def set_slot(self, slot: int):
        self.slot = slot
        self.update()
    
            
    def update(self): 
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #Load image and scale down
        self.full_img = load_image(self.img, -1)[0]
        self.image = pygame.transform.scale(self.full_img,(int(.1*screen.get_width()),int(.15*screen.get_width())))
        #Card hitbox
        self.rect = self.image.get_rect()
       
 
        #set position = width * slot
        self.card_width = self.image.get_size()[0];
        self.rect.topleft = (screen.get_width()*.2)+(self.card_width+10)*self.slot, screen.get_size()[1]-(self.image.get_height()*1.3)
        self.selected = False
       