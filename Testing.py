import pygame

pygame.init()

x = 1920
y = 1000

display_surface = pygame.display.set_mode((x,y))

sword = pygame.image.load("sword.png")

pygame.mouse.set_visible(True)

# Game Loop
isRunning = True
while isRunning:
    display_surface.blit(sword, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        pygame.display.update()