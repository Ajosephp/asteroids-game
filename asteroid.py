import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y) ,self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_vector_one = self.velocity.rotate(angle)
        new_vector_two = self.velocity.rotate(-angle)
        
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_one.velocity = new_vector_one * 1.2
        asteroid_two.velocity = new_vector_two * 1.2