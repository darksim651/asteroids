import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()           # Creates a 'Group' to store things that can be updated
    drawable = pygame.sprite.Group()            # Created a Group to store drawables

    Player.containers = (updatable, drawable)   # Add any Player instances to both groups
    player = Player(x, y, PLAYER_RADIUS, 0)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)                    #
        for asteroid in asteroids:              
            if asteroid.collides_with(player):  # Collision detection
                log_event("player_hit")
                print("Game over!")
                sys.exit() 
        for object in drawable:                 # Iterates through the group of drawables and updates the screen
            object.draw(screen)
        
        pygame.display.flip()
                                                        # Pauses game loop until 1/60th of a second has passed, for 60fps target
        dt = my_clock.tick(60) / 1000                   # Convert to ms



if __name__ == "__main__":
    main()
