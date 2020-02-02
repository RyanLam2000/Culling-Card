import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import load_image

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, hp=50, atk=5, attribute="Rainbow", img='enemy.png', multiplier = 0):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.health = int(hp * (1 + .2 * multiplier))
        self.pow = atk
        self.type = attribute
        self.img = img
        self.update()
  
        #Load image and scale down
   
        
    def attack(self):
        pass
        
    def update(self,dmg=0):
        screen = pygame.display.get_surface()
        
        self.health -= dmg
        full_img = load_image(self.img, -1)[0]
        self.image = pygame.transform.scale(full_img,(int(.1*screen.get_width()),int(.1*screen.get_width())))
        self.rect = self.image.get_rect()
        self.area = screen.get_rect()
 
        #set position = 80vw,50vh
        self.rect.topleft = (screen.get_width()*.8), screen.get_size()[1]*.66 - self.image.get_height()*.9
        
        #Display health 
        font = pygame.font.Font("data/dpcomic.ttf", 36)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))
        text_center = (self.rect.topleft[0]+(self.image.get_width()/2),int(self.rect.topleft[1])*.8)
        textpos = self.text.get_rect(center=text_center)
        screen.blit(self.text, textpos)
        self.text2 = font.render("Atk:"+str(self.pow), 1, (255, 0, 0))
        text_center = (self.rect.topleft[0]+(self.image.get_width()/2),int(self.rect.topleft[1])*.9)
        textpos = self.text2.get_rect(center=text_center)
        screen.blit(self.text2, textpos)
    
        