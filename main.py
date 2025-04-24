import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dt = 0
fps = pygame.time.Clock()

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots_group = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroid.containers = (updateable, drawable, asteroids)
AsteroidField.containers = (updateable)
Shot.containers = (updateable, drawable, shots_group)

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
asteroid_field = AsteroidField()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updateable.update(dt)
    for asteroid in asteroids:
        if player.collides(asteroid) == True:
            print("Game over!")
            sys.exit()

    fill_color = (0,0,0)
    screen.fill(fill_color, rect=None)
    for obj in drawable:
        obj.draw(screen)
    pygame.display.flip()

    dt = fps.tick(60)/1000

if __name__ == "__main__":
    main()