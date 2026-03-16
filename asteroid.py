import pygame
import random
from constants import *
from circleshape import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        self.kill()                                             # Kills the shot asteroid
        if old_radius <= ASTEROID_MIN_RADIUS:                   # Stops split if the asteroid was at the min radius
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)                    # Generates a random angle for the split
        first_vector = self.velocity.rotate(split_angle)        # Creates 2 vectors based on the existing velocity and rotation of the shot asteroid
        second_vector = self.velocity.rotate(-split_angle)      # Uses negative angle
        new_radius = old_radius - ASTEROID_MIN_RADIUS           # Shrinks the new asteroids' radius
        first_splitter = Asteroid(self.position.x, self.position.y, new_radius)         # Creates a new asteroid object
        second_splitter = Asteroid(self.position.x, self.position.y, new_radius)        # 
        first_splitter.velocity = first_vector * ASTEROID_SPLIT_VELOCITY_MULTIPLIER     # Increases speed by multiplier
        second_splitter.velocity = second_vector * ASTEROID_SPLIT_VELOCITY_MULTIPLIER



