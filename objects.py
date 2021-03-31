import pygame


class Object:
    def __init__(self, x, y, size_x, size_y, speed_x, speed_y, hp, image):
        self.x = int(x)
        self.y = int(y)
        self.size_x = int(size_x)
        self.size_y = int(size_y)
        self.speed_x = int(speed_x)
        self.speed_y = int(speed_y)
        self.hp = int(hp)
        self.image = image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_hp(self):
        return int(self.hp)

    def set_x(self, shift):
        self.x += shift

    def set_y(self, shift):
        self.y += shift

    def set_size_x(self, shift):
        self.size_x += shift

    def set_size_y(self, shift):
        self.size_y += shift

    def set_speed_x(self, shift):
        self.speed_x += shift

    def set_speed_y(self, shift):
        self.speed_y += shift

    def set_hp(self, shift):
        self.hp += shift

    def draw_rect(self, screen):
        art = pygame.image.load(self.image)
        screen.blit(art, (self.x, self.y))

    def go(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def is_alive(self):
        if self.hp > 0:
            return True
        return False


class Enemy(Object):
    def __init__(self, x, y, size_x, size_y, speed_x, speed_y, hp, image, cooldown):
        super().__init__(x, y, size_x, size_y, speed_x, speed_y, hp, image)
        self.cooldown = cooldown
        self.time = 0

    def get_cooldown(self):
        return self.cooldown

    def get_time(self):
        return self.time

    def tick_time(self):
        self.time += 1

    def shoot(self):
        self.time = 0
        ball = Bullet(self.x + self.size_x // 2, self.y + self.size_y + 10, 5, 5, 0, 8, 1, 'ball.png')
        return ball

    def can_shoot(self):
        if self.time >= self.cooldown:
            return True
        return False


class Bullet(Object):
    def __init__(self, x, y, size_x, size_y, speed_x, speed_y, hp, image):
        super().__init__(x, y, size_x, size_y, speed_x, speed_y, hp, image)


class Upgrade(Object):
    def __init__(self, x, y, size_x, size_y, speed_x, speed_y, hp, image):
        super().__init__(x, y, size_x, size_y, speed_x, speed_y, hp, image)
