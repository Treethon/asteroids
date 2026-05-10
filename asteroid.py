from circleshape import CircleShape
from logger import log_event
import random
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        first_aster_angle = self.velocity.rotate(rand_angle)
        second_aster_angle = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_aster = Asteroid(self.position.x, self.position.y, new_radius)
        second_aster = Asteroid(self.position.x, self.position.y, new_radius)
        first_aster.velocity = first_aster_angle * 1.2
        second_aster.velocity = second_aster_angle * 1.2