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
from text import Text
from cards import *
from shield_bar import Shield


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
    
    background = BackgroundImage('data/background.jpg',[0,0])
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
    background = BackgroundImage('data/background.jpg',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)

    title_text = Text("Culling Card",0,0,screen,font,white,black)
    cont_rect = Text("Play",0,48,screen,font,white,black)
    score_text = Text("High Score: "+score,0,76,screen,font,white,black)
    streak_rect = Text("Choose Resolution",0,108,screen,font,white,black)
    pygame.display.flip()
    menu_text = [cont_rect,title_text,score_text,streak_rect]

    while True:

        ret_flag = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if cont_rect.rect.collidepoint(pos): # player clicked end turn
                        return True
                    elif streak_rect.rect.collidepoint(pos): 

                        background = BackgroundImage('data/background.jpg',[0,0])
                        screen.fill([255, 255, 255])
                        screen.blit(background.image, background.rect)
                        fs_rect = Text("Full Screen",0,0,screen,font,white,black)
                        med_rect = Text("960*720",0,48,screen,font,white,black)
                        sm_rect = Text("800*600",0,76,screen,font,white,black)
                        ret_rect = Text("Return",0,108,screen,font,white,black)   
                        res_text = [fs_rect,med_rect,sm_rect,ret_rect]
                        pygame.display.flip()
                        
                        while True:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                elif event.type == MOUSEBUTTONDOWN:
                                    pos = pygame.mouse.get_pos()
                                    if ret_rect.rect.collidepoint(pos):
                                        ret_flag = True
                                        break
                                    elif fs_rect.rect.collidepoint(pos):
#                                         pygame.display.set_mode((pygame.display.Info().current_w,pygame.display.Info().current_h),
#                                                                 pygame.FULLSCREEN)
#                                         print(str(pygame.display.Info().current_w)+ " " +str(pygame.display.Info().current_h))
                                        return "full"
                                    elif med_rect.rect.collidepoint(pos):
#                                         pygame.display.set_mode((960,720),pygame.NOFRAME)
                                        return "med"
                                    elif sm_rect.rect.collidepoint(pos):
#                                         pygame.display.set_mode((800,600),pygame.NOFRAME)
                                        return "sm"
                                elif event.type == RESIZABLE:
                                    #redefine screen and fit background to screen
                                    width,height = event.size
                                    if width<600:
                                        width=400
                                    if height<400:
                                        height=400
                                    screen = pygame.display.set_mode((width, height),RESIZABLE)
                                    background = BackgroundImage('data/background.jpg',[0,0])
                                    screen.fill([255, 255, 255])
                                    screen.blit(background.image, background.rect)
                     
                                    for txt in res_text:
                                        txt.update(screen)
                                     
                                    pygame.display.flip()
#                                                                 
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
                    screen = pygame.display.set_mode((width, height),RESIZABLE)
                    background = BackgroundImage('data/background.jpg',[0,0])
                    screen.fill([255, 255, 255])
                    screen.blit(background.image, background.rect)
                    for txt in menu_text:
                        txt.update(screen)
                    
                    pygame.display.flip()
                                                     
         
            if ret_flag:
                background = BackgroundImage('data/background.jpg',[0,0])
                screen.fill([255, 255, 255])
                screen.blit(background.image, background.rect)
                for txt in menu_text:
                    txt.update(screen)
                
                pygame.display.flip()
                break
                                     
    return False
     

def endgame(screen,high,won=True):
    background = BackgroundImage('data/background.jpg',[0,0])
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
        top_text = font.render('Game Over!', True, white, black)
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
    streak_rect = streak_text.get_rect(center=(width/2,height/2+20))
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
    fs = False
    size = startgame(screen) 
    if size=="sm":
        screen = pygame.display.set_mode((800, 600),RESIZABLE)
    elif size =="med":
        screen = pygame.display.set_mode((800, 600),RESIZABLE)
    elif size == "full":
        print(str(width)+ " " +str(height))
        screen = pygame.display.set_mode((width, height),FULLSCREEN)
        fs = True
    # Create The Backgound
    background = BackgroundImage('data/background.jpg',[0,0])
    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)

    # Display The Background
    screen.blit(background.image, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    score = 0
    mob_mult = 0
    clock = pygame.time.Clock()
    hero = Hero()
    enemy = get_enemy()
    health = Health(screen)
    energy = Energy(screen)
    shield = Shield(screen)
    deck = Deck()
    hand = []
    discard = []
    if not fs:
        turn_button = Button(screen,"End Turn",.88,.8)
        exit_button = Button(screen,"Exit", .9,.05)
      
    else: 
        turn_button = Button(screen,"End Turn",.8,.8)
        exit_button = Button(screen,"Exit", .8,.1)
        health = Health(screen,.15,.8)
        energy = Energy(screen,.15,.85)
        
    all_sprites = pygame.sprite.RenderPlain((hero, enemy))
    ui_elements = [health,energy, shield,turn_button,enemy,exit_button]

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
                    if turn_button.rect.collidepoint(pos):# player clicked end turn
                        all_sprites.remove(hand)
                        cards.empty()
                        discard.extend(hand)
                        hand = []
                        player_turn = False
                    elif exit_button.rect.collidepoint(pos):
                        exit()
                    else:
                        for card in hand.copy():
                            if card.rect.collidepoint(pos):
                                if energy.energy<=0:
                                    alert(screen,"Out of Energy!", 1)
                                else:
                                    hand.remove(card)
                                    card.kill()
                                    discard.append(card)
                                    if (type(card) == draw_card.DrawCard):
                                        alert(screen, "Player drew two cards!", 1)
                                    elif (type(card) == blue_attack.BlueAttack and enemy.type == "red") or (type(card) == green_attack.GreenAttack and enemy.type == "blue") or (type(card) == red_attack.RedAttack and enemy.type == "green"):
                                        alert(screen, "Player dealt 8 damage! It was super effective!", 1)
                                    elif (type(card) == red_attack.RedAttack and enemy.type == "red") or (type(card) == blue_attack.BlueAttack and enemy.type == "blue") or (type(card) == green_attack.GreenAttack and enemy.type == "green"):
                                        alert(screen, "Player dealt 5 damage!", 1)
                                    elif (type(card) == green_attack.GreenAttack and enemy.type == "red") or (type(card) == red_attack.RedAttack and enemy.type == "blue") or (type(card) == blue_attack.BlueAttack and enemy.type == "green"):
                                        alert(screen, "Player dealt 3 damage! It was not very effective...", 1)
                                    elif (type(card) == defend_card.DefendCard):
                                        alert(screen, "Player setup 2 block!", 1)
                                    energy.update(-card.en_cost)
                                    card.clicked(hero, enemy, deck, hand, discard)   
                                    shield.defense = hero.defense
                                    cards.add(hand)
                                    all_sprites.add(hand)
                                    break

                        redraw_screen(screen,ui_elements,all_sprites,True)
                        pygame.display.flip()

                        if health.health <= 0:
                            if endgame(screen,False):
                                pass
                        elif enemy.health <=0:
                            alert(screen, "Player killed the enemy!", 1)
                            score += 50
                            mob_mult += 1
#                             if endgame(screen,score,True):
                            enemy.kill()
                            hero.defense = 0
                            shield.defense = hero.defense
                            enemy = get_enemy(mob_mult)
                            ui_elements[-2] = enemy
                            energy.energy = 3
                            all_sprites.add(enemy)
                            redraw_screen(screen,ui_elements,all_sprites)
                            pygame.display.flip()

                elif event.type == RESIZABLE and not fs:
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
        if (not going):
            break
        energy.energy = 3
        enemy.attack()
        dmg_remaining = enemy.pow - hero.defense
        if (dmg_remaining > 0):
            alert(screen, f"Player took {dmg_remaining} damage.", 1)
            health.update(-dmg_remaining)
        else:
            hero.defense = hero.defense - enemy.pow
            alert(screen, f"Enemy hit player's shield for {enemy.pow} damage.", 1)
        hero.defense = 0
        shield.defense = hero.defense
        player_turn = True
        
        if health.isDead():
            going = endgame(screen, score, False)
            score = 0   
            health.health = 25
            enemy.kill()
            enemy = get_enemy()
            all_sprites.add(enemy)
            ui_elements[-2] = enemy
            deck.merge(discard) 
            discard.clear()

    pygame.quit()


# Game Over


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()