import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from helpers import load_image

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, hp=50, atk=5, attribute="Rainbow", img='enemy.png'):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.health = hp
        self.pow = atk
        self.type = attribute
        self.img = img
        self.update()
  
        #Load image and scale down
   
        
    def attack(self):
        print("attack")
        
    def update(self,dmg=0):
        self.health -= dmg
        full_img = load_image(self.img, -1)[0]
        self.image = pygame.transform.scale(full_img,(150,150))
        self.rect = self.image.get_rect()
        
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
 
        #set position = 80vw,50vh
        self.rect.topleft = (screen.get_width()*.8), screen.get_size()[1]*.5
        
        #Display health 
        font = pygame.font.Font(None, 36)
        font.set_underline(1)
        self.text = font.render("HP:"+str(self.health), 1, (255, 0, 0))
        text_center = (self.rect.topleft[0]+75,self.rect.topleft[1]+10)
        textpos = self.text.get_rect(center=text_center)
        screen.blit(self.text, textpos)
    
        