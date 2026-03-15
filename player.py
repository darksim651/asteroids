import pygame
from constants import *
from circleshape import *
from shot import *


class Player(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.cooldown_timer = 0.0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.cooldown_timer -= dt           # Subtracts delta-time from remaining cooldown timer each time update is called on player
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer > 0:     # Stops player from shooting if the timer is above 0
                return
            self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)      # Spawns a shot at player's position, with the parameters x, y, radius passed in
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)      # Sets the vector and rotation to player's rotation
        shot.velocity *= PLAYER_SHOOT_SPEED                             # Shot speed multiplier

            