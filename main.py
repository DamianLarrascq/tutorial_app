import pygame
from sys import exit
from random import randint
from pygame.constants import K_SPACE

# imports "exit()" to finish the while loop

game_active = False
game_score = 0
score_format = 'Int'


def calculate_score():
    current_time = pygame.time.get_ticks() - game_score

    return current_time


def display_score():
    score_surface = test_font.render(f'{ms_to_sec(calculate_score())}', False, 'Black')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)

    return None


def ms_to_sec(ms):
    result = ms
    if score_format == 'Float':
        result = float(ms / 1000)
    if score_format == 'Int':
        result = int(ms / 1000)

    return result


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


# initializes pygame


pygame.init()

# set screen width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Game")

# object that controls time and frames
clock = pygame.time.Clock()

# game font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# start text
game_title = test_font.render('Pixel Runner', False, 'Black')
game_title_rect = game_title.get_rect(center=(400, 100))
game_message = test_font.render('Press Space to Start', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 300))

# variables for background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_rect = snail_surface.get_rect(midbottom=(300, 300))
fly_surface = pygame.image.load('graphics/Fly/Fly1.png')
obstacle_rect_list = []

# player surface
player_surface = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# game loop
while True:

    # checks for events
    for event in pygame.event.get():

        # checks if the X in the screen is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # checks if the space key is pressed and jumps
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20

            # checks if a mouse button is pressed and jumps
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                player_gravity = -20

            if event.type == obstacle_timer and game_active:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom=(randint(900, 1100), 200)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                game_score = pygame.time.get_ticks()

    if game_active:
        # sky
        screen.blit(sky_surface, (0, 0))

        # ground
        screen.blit(ground_surface, (0, 300))

        # score
        display_score()

        # snail
        # screen.blit(snail_surface, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # if snail_rect.colliderect(player_rect):
        # game_active = False

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your Score: {ms_to_sec(calculate_score())}', False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 350))
        screen.blit(game_title, game_title_rect)

        if game_score == 0:
            screen.blit(game_message, game_message_rect)

        else:
            screen.blit(score_message, score_message_rect)

    # update everything in the screen
    pygame.display.update()

    # tells while loop to not run faster than 60fps
    clock.tick(60)
