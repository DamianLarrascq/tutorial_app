import pygame
from sys import exit
# imports "exit()" to finish the while loop

# initializes pygame
pygame.init()

# set screen width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")

# object that controls time and frames
clock = pygame.time.Clock()

# game font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# variables for background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black').convert()

# enemy surface
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(300, 300))

# player surface
player_surface = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))

# game loop
while True:

    # checks for events
    for event in pygame.event.get():

        # checks if the X in the screen is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 25))
    snail_rect.left -= 2
    if snail_rect.left <= 0:
        snail_rect.right = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # update everything in the screen
    pygame.display.update()

    # tells while loop to not run faster than 60fps
    clock.tick(60)
