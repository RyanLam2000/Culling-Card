#!/usr/bin/env python
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""


# Import Modules
import os, pygame, time
from pygame.locals import *
from pygame.compat import geterror
from card import Card
from helpers import *
from hero import Hero
from enemy import Enemy
from helpers import *
from health_bar import Health
from energy_bar import Energy
from button import Button
from deck import Deck
from cards.red_attack import RedAttack
from bg_image import BackgroundImage

# def load_sound(name):
#     class NoneSound:
#         def play(self):
#             pass
# 
#     if not pygame.mixer or not pygame.mixer.get_init():
#         return NoneSound()
# #     fullname = os.path.join(data_dir, name)
# #     try:
# #         sound = pygame.mixer.Sound(fullname)
# #     except pygame.error:
# #         print("Cannot load sound: %s" % fullname)
# #         raise SystemExit(str(geterror()))
#     return

def redraw_screen(screen,ui_elements,all_sprites,click = False):
    
    background = BackgroundImage('data/background.png',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)
    
    #re-render all objects
    for element in ui_elements:
        element.update()
    if(not click):
        for sprite in all_sprites:
            sprite.update()
    all_sprites.draw(screen)




def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((600, 600),pygame.RESIZABLE)
    pygame.display.set_caption("Culling Card")
    pygame.mouse.set_visible(1)

    # Create The Backgound
    background = BackgroundImage('data/background.png',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)

    # Put Text On The Background, Centered

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Culling Card", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=screen.get_width() / 2)
        screen.blit(text, textpos)

    # Display The Background
    screen.blit(background.image, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    hero = Hero()
    enemy = Enemy(img = "enemy.png")
    health = Health(screen)
    energy = Energy(screen)
    deck = Deck()
    hand = []
    discard = []
    turn_button = Button(screen,"End Turn",.88,.8)
    
    all_sprites = pygame.sprite.RenderPlain((hero, enemy))
    
    ui_elements = [health,energy,turn_button,enemy]
    #used when checking for clicks on cards, avoid checking clicks on non card elements
    cards = pygame.sprite.RenderPlain()
    for i in range(0,5): 
        card=RedAttack(i)
        all_sprites.add(card)
        cards.add(card)
    
    # Main Loop
    going = True
    enemy_turn = False
    player_turn = True
    
    # Draw Everything
    all_sprites.update()
    all_sprites.draw(screen)

    
    while going:
        clock.tick(60)  
        # Handle Input Events
        while player_turn:# turn doesn't end until player clicks end turn
            for event in pygame.event.get():
                if event.type == QUIT:
                    player_turn = False
                    going = False
                    break
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if turn_button.rect.collidepoint(pos): # player clicked end turn
                        player_turn = False 
                        print("skipped a turn")
                    else:
                        clicked = [s for s in cards if s.rect.collidepoint(pos)]
                        for card in clicked: 
                            card.clicked(hero, enemy)
                        redraw_screen(screen,ui_elements,all_sprites,True)
                        pygame.display.flip()

                 
                elif event.type == RESIZABLE:
                    #redefine screen and fit background to screen
                    surface = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)
                    redraw_screen(screen,ui_elements,all_sprites)
                    pygame.display.flip()
                 

        enemy.attack()
         
        player_turn = True

        screen.blit(background.image, background.rect)
        all_sprites.update()

        if health.isDead():
            going = False
        all_sprites.draw(screen)
       
        pygame.display.flip()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()