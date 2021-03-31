import pygame
from objects import Bullet


class Hero:
    def __init__(self, x, y, size_x, size_y, speed, power, hp, cooldown):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.speed = speed
        self.power = power
        self.hp = hp
        self.cooldown = cooldown
        self.time = 0

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def get_speed(self):
        return self.speed

    def get_power(self):
        return self.power

    def get_hp(self):
        return self.hp

    def set_x(self, shift):
        self.x += shift

    def set_y(self, shift):
        self.y += shift

    def set_size_x(self, shift):
        self.size_x += shift

    def set_size_y(self, shift):
        self.size_y += shift

    def set_speed(self, shift):
        self.speed += shift

    def set_power(self, shift):
        self.power += shift

    def set_hp(self, shift):
        self.hp += shift

    def go_right(self):
        self.x += self.speed

    def go_left(self):
        self.x -= self.speed

    def go_up(self):
        self.y -= self.speed

    def go_down(self):
        self.y += self.speed

    def is_alive(self):
        if self.hp > 0:
            return True
        return False

    def draw_rect(self, path, screen):
        art = pygame.image.load(f'{path}')
        screen.blit(art, (self.x, self.y))

    def get_cooldown(self):
        return self.cooldown

    def get_time(self):
        return self.time

    def tick_time(self):
        self.time += 1

    def shoot(self):
        self.time = 0
        ball = Bullet(self.x + self.size_x // 2, self.y, 5, 5, 0, -17, 1, 'bullet.png')
        return ball

    def can_shoot(self):
        if self.time >= self.cooldown:
            return True
        return False
