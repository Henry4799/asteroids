import pygame
from constants import *

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
    fill_color = (0,0,0)
    screen.fill(fill_color, rect=None)
    pygame.display.flip()

if __name__ == "__main__":
    main()