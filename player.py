import pygame

from circleshape import CircleShape
from constants import PLAY_SPEED, PLAYER_IFRAME_TIME, PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_IFRAME_TIME
from shot import Shot



class Player(CircleShape):
    
    def __init__(self,x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0
        self.iframe_cooldown = 0
        self.health = 3

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.triangle(),2)
    
    def update(self, dt):
        self.shoot_cooldown_timer -= dt
        self.iframe_cooldown -= dt 
        keys = pygame.key.get_pressed()
         
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def take_damage(self, dt):
        if self.iframe_cooldown > 0:
            return
        self.iframe_cooldown = PLAYER_IFRAME_TIME * dt
        self.health -= 1
        



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAY_SPEED * dt 
    
    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return
        
        self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


        
