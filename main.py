import pygame
from sys import exit
# imports "exit()" to finish the while loop

# initializes pygame
pygame.init()

# set screen width and height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game")
# object that controls time and frames
clock = pygame.time.Clock()
# variable for surface
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')
# game loop
while True:

    # checks for events
    for event in pygame.event.get():

        # checks if the X in the screen is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (0, 0))

    # update everything in the screen
    pygame.display.update()
    # tells while loop to not run faster than 60fps
    clock.tick(60)
