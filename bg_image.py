import pygame,os
from helpers import *

class BackgroundImage(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        img = pygame.image.load(image_file)
        screen = pygame.display.get_surface()
        self.image = pygame.transform.scale(img,(screen.get_width(),screen.get_height()))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    