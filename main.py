# Import Modules
import os, pygame, time
from pygame.locals import *
from pygame.compat import geterror
from card import Card
from helpers import *
from hero import Hero
from enemy import Enemy
from health_bar import Health
from energy_bar import Energy
from button import Button
from deck import Deck
from bg_image import BackgroundImage
from get_enemy import get_enemy
from pygame.examples.video import full
import pygame_sdl2
pygame_sdl2.import_as_pygame()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0,0,0)
  
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
def render_text(string,w,h,screen,font,c1,c2):
    text = font.render(string,True,c1,c2)
    text_rect = text.get_rect(center=(w,h))
    screen.blit(text,text_rect)
    return text_rect
    

def startgame(screen):
   
    title_font = pygame.font.Font("data/dpcomic.ttf",48)
    font = pygame.font.Font("data/dpcomic.ttf", 32) 
    width = screen.get_width()
    height = screen.get_height()
    
    with open('data/high_score.txt',"r+") as f:
        score=f.readline()
        f.close()  
    while True:
        print("redrawing")
        background = BackgroundImage('data/background.png',[0,0])
        screen.fill([255, 255, 255])
        screen.blit(background.image, background.rect)
        render_text("Culling Card",width/2,height/2,screen,font,white,black)
        cont_rect = render_text("Play",width/2,height/2+48,screen,font,white,black)
        render_text("High Score: "+score,width/2,height/2+76,screen,font,white,black)
        streak_rect = render_text("Choose Resolution",width/2,height/2+108,screen,font,white,black)
                    
        pygame.display.flip()
        ret_flag = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if cont_rect.collidepoint(pos): # player clicked end turn
                        return True
                    elif streak_rect.collidepoint(pos): 
                        print("res chose")
                        background = BackgroundImage('data/background.png',[0,0])
                        screen.fill([255, 255, 255])
                        screen.blit(background.image, background.rect)
                        fs_rect = render_text("Full Screen",width/2,height/2,screen,font,white,black)
                        med_rect = render_text("960*720",width/2,height/2+48,screen,font,white,black)
                        sm_rect = render_text("800*600",width/2,height/2+76,screen,font,white,black)
                        ret_rect = render_text("Return",width/2,height/2+108,screen,font,white,black)
                        pygame.display.flip()
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                elif event.type == MOUSEBUTTONDOWN:
                                    pos = pygame.mouse.get_pos()
                                    if ret_rect.collidepoint(pos):
                                        ret_flag = True
                                        break
                                    elif fs_rect.collidepoint(pos):
#                                         pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h),
#                                                                 pygame.FULLSCREEN)
#                                         print(str(pygame.display.Info().current_w)+ " " +str(pygame.display.Info().current_h))
                                        return "full"
                                    elif med_rect.collidepoint(pos):
#                                         pygame.display.set_mode((960,720),pygame.NOFRAME)
                                        return "med"
                                    elif sm_rect.collidepoint(pos):
#                                         pygame.display.set_mode((800,600),pygame.NOFRAME)
                                        return "sm"
                                    elif event.type == RESIZABLE:
                                        #redefine screen and fit background to screen
                                        width,height = event.size
                                        if width<600:
                                            width=400
                                        if height<400:
                                            height=400
                                        screen=pygame.display.set_mode((width, height),
                                                                          pygame.RESIZABLE|HWSURFACE|DOUBLEBUF)
                            if ret_flag:
                                break
                        if ret_flag:
                            break
                elif event.type == RESIZABLE:
                    #redefine screen and fit background to screen
                    width,height = event.size
                    if width<600:
                        width=400
                    if height<400:
                        height=400
                    screen=pygame.display.set_mode((width, height),
                                                      pygame.RESIZABLE|HWSURFACE|DOUBLEBUF)
        
            if ret_flag: 
                break
                                    
    return False
     

def endgame(screen,high,won=True):
    background = BackgroundImage('data/background.png',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)
    font = pygame.font.Font("data/dpcomic.ttf", 32) 
    width = screen.get_width()
    height = screen.get_height()
    
    #update high score
    with open('data/high_score.txt',"r+") as f:
        s=f.readline()
        score = int(s)
        if(score<high):
            f.seek(0)
            f.truncate()
            f.write(str(high))
        f.close()
        
    #render text
    if won:
        top_text = font.render('You Win!', True, white, black)  
    else:
        top_text = font.render('Defeat!', True, white, black)
    continue_text = font.render('Continue?', True, white, black)
    score_text = font.render('High Score: '+str(score), True, white, black)
    streak_text = font.render('Streak: '+str(high),True,white,black)
    
    streak_rect = streak_text.get_rect(center=(width/2,height/2+64))
    top_rect=top_text.get_rect(center=(width/2,height/2))
    score_rect=score_text.get_rect(center=(width/2,height/2+32))
    cont_rect = continue_text.get_rect(center=(width/2,height/2+96))
    
    screen.blit(top_text,top_rect)
    screen.blit(score_text,score_rect)
    screen.blit(continue_text,cont_rect)
    screen.blit(streak_text,streak_rect)
  
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if cont_rect.collidepoint(pos): # player clicked end turn
                    return True
    return False
    
def alert(screen,string,seconds): 
    width = screen.get_width()
    height = screen.get_height()
    font = pygame.font.Font("data/dpcomic.ttf", 32)      
    streak_text = font.render(string,True,white,black)
    streak_rect = streak_text.get_rect(center=(width/2,height/2+64))
    screen.blit(streak_text,streak_rect)
    pygame.display.flip()
    time.sleep(seconds)
    

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    screen = pygame.display.set_mode((600, 600),RESIZABLE)
    pygame.display.set_caption("Culling Card")
    pygame.mouse.set_visible(1)

    size = startgame(screen) 
    if size=="sm":
        screen = pygame.display.set_mode((800, 600),RESIZABLE)
    elif size =="med":
        screen = pygame.display.set_mode((800, 600),RESIZABLE)
    elif size == "full":
        print(str(width)+ " " +str(height))
        screen = pygame.display.set_mode((width, height),FULLSCREEN)
    # Create The Backgound
    background = BackgroundImage('data/background.png',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)

    # Display The Background
    screen.blit(background.image, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    score = 0
    clock = pygame.time.Clock()
    hero = Hero()
    enemy = get_enemy()
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
    
    # Main Loop
    going = True
    player_turn = True
    
    # Draw Everything
    all_sprites.update()
    all_sprites.draw(screen)

    
    while going:
        clock.tick(60)  
  
        deck.draw_n(5, hand, discard)
        all_sprites.add(hand)
        cards.add(hand)
        redraw_screen(screen, ui_elements, all_sprites)
        pygame.display.flip()
        
        # Handle Input Events
        while player_turn: # turn doesn't end until player clicks end turn
            for event in pygame.event.get():
                if event.type == QUIT:
                    player_turn = False
                    going = False
                    break
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if turn_button.rect.collidepoint(pos): # player clicked end turn
                        all_sprites.remove(hand)
                        cards.empty()
                        discard.extend(hand)
                        hand = []
                        player_turn = False
                    else:
                        for card in hand.copy():
                            if card.rect.collidepoint(pos):
                                if energy.energy<=0:
                                    alert(screen,"Out of Energy",2)
                                else:
                                    hand.remove(card)
                                    card.kill()
                                    discard.append(card)
                                    energy.update(-card.en_cost)
                                    card.clicked(hero, enemy, deck, hand, discard)                            
                                    cards.add(hand)
                                    all_sprites.add(hand)
                                    break

                        redraw_screen(screen,ui_elements,all_sprites,True)
                        pygame.display.flip()

                        if health.health <= 0:
                            if endgame(screen,False):
                                pass
                        elif enemy.health <=0:
                            score += 1
                            if endgame(screen,score,True):
                                enemy.kill()
                                enemy = get_enemy(score)
                                ui_elements[-1] = enemy
                                energy.energy = 3
                                all_sprites.add(enemy)
                                redraw_screen(screen,ui_elements,all_sprites)
                                pygame.display.flip()

                elif event.type == pygame.VIDEORESIZE:
                    #redefine screen and fit background to screen
                    width,height = event.size
                    if width<600:
                        width=400
                    if height<400:
                        height=400
                    screen=pygame.display.set_mode((width, height),
                                                      pygame.RESIZABLE|HWSURFACE|DOUBLEBUF)
                    redraw_screen(screen,ui_elements,all_sprites)
                    pygame.display.flip()
        energy.energy = 3
        enemy.attack()
        dmg_remaining = enemy.pow - hero.defense
        if (dmg_remaining > 0):
            health.update(-dmg_remaining)
        else:
            hero.defense = hero.defense - enemy.pow
        hero.defense = 0
        player_turn = True
        
        if health.isDead():
            going = False       

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()