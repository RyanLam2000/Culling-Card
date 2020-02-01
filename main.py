#!/usr/bin/env python
"""
This simple example is used for the line-by-line tutorial
that comes with pygame. It is based on a 'popular' web banner.
Note there are comments here, but for the full explanation,
follow along in the tutorial.
"""


# Import Modules
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
from card import Card
from hero import Hero
from enemy import Enemy
from helpers import *



def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
#     fullname = os.path.join(data_dir, name)
#     try:
#         sound = pygame.mixer.Sound(fullname)
#     except pygame.error:
#         print("Cannot load sound: %s" % fullname)
#         raise SystemExit(str(geterror()))
    return




def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Culling Card")
    pygame.mouse.set_visible(1)

    # Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Culling Card", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()
    hero = Hero()
    enemy = Enemy()
    all_cards = pygame.sprite.RenderPlain((hero,enemy))

    cards = pygame.sprite.RenderPlain()
    for i in range(0,5): 
        card=Card(i)
        all_cards.add(card)
        cards.add(card)
        
    # Main Loop
    going = True
    enemy_turn = True
    while going:
        clock.tick(60)

        # Handle Input Events
        if enemy_turn:
            enemy.attack()
            enemy_turn=False
            
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = [s for s in cards if s.rect.collidepoint(pos)]
                for card in clicked: 
                    card.clicked()

        all_cards.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_cards.draw(screen)
        pygame.display.flip()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()