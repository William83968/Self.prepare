# Pygame template -- skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 460
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initilisation 
pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Processing input(events)
    for event in pygame.event.get():
        # Checking for close window
        if event.type == pygame.QUIT:
            running = False
    
    # Drawing stuff and update
    win.fill(BLACK)
    # *after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
sys.exit()
