import pygame
from constants import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt = 0
fps = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fill_color = (0,0,0)
    screen.fill(fill_color, rect=None)
    pygame.display.flip()
    dt = fps.tick(60)/1000


if __name__ == "__main__":
    main()