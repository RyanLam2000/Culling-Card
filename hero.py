import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import *

class Hero(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        
        #Load image and scale down
        self.full_img = load_image("hero.png", -1)[0]
        self.image = pygame.transform.scale(self.full_img,(150,150))
        #Card hitbox
        self.rect = self.image.get_rect()
        
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
 
        #set position = width * slot
        self.card_width = self.image.get_size()[0];
        self.rect.topleft = (screen.get_width()*.1), screen.get_size()[1]*.5
    
    
