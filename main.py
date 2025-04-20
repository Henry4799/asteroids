import pygame
from constants import *
from circleshape import CircleShape
from player import Player

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt = 0
fps = pygame.time.Clock()

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updateable, drawable)

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateable.update(dt)

    fill_color = (0,0,0)
    screen.fill(fill_color, rect=None)
    for obj in drawable:
        obj.draw(screen)
    pygame.display.flip()

    dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()