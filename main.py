import pygame
from random import randint
from hero import Hero
from objects import Enemy
from dop import collide


# ширина и высота окна
WIDTH = 800
HEIGHT = 800

# инициализация героя
x, y, size_x, size_y, speed, power, hp, cooldown = 300, HEIGHT - 100, 50, 50, 10, 1, 10, 5
hero = Hero(x, y, size_x, size_y, speed, power, hp, cooldown)

# в очереди будут отрисовываться все объекты кроме героя
# пока можно без очереди, обычным списком
queue = []
count = 0

# список пуль героя
bullets = []

# типы врагов
types = [[0, 0, 50, 72, 0, 0, 20, 'enemy_kind1.png', 30], [0, 0, 55, 52, 0, 0, 5, 'enemy_kind2.png', 60],
         [0, 0, 55, 62, 0, 0, 10, 'enemy_kind3.png', 45]]

# список пуль врагов
enemy_bullets = []

# инициализация pygame и окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# название и иконка игры
pygame.display.set_caption('Touhou')
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# фпс
clock = pygame.time.Clock()

run = True
while run:
    # 30 фпс, фон белый
    clock.tick(30)
    screen.fill((255, 255, 255))

    # движение персонажа
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero.go_right()
    if keys[pygame.K_LEFT]:
        hero.go_left()
    if keys[pygame.K_UP]:
        hero.go_up()
    if keys[pygame.K_DOWN]:
        hero.go_down()
    if keys[pygame.K_SPACE]:
        if hero.can_shoot():
            bullet = hero.shoot()
            bullets.append(bullet)

    hero.tick_time()

    # рисую пули героя и удаляю лишние из списка
    for heart in bullets:
        # проверка нужна ли пуля
        if not heart.is_alive() or heart.get_y() < -heart.get_size_y():
            bullets.remove(heart)
        # отрисовка пули
        heart.draw_rect(screen)
        heart.go()

    # генерация объектов
    count += 1
    if count % max(5, 30 - count // 240) == 0:  # со временем враги будут появляться быстрее, но не быстрее, 5
        # генерация врага со случайными характеристиками
        enemy_type = types[randint(0, 2)]
        enemy_type[0], enemy_type[1], enemy_type[4], enemy_type[5] = randint(0, WIDTH - 100),\
                                                                     randint(0, HEIGHT // 2),\
                                                                     randint(-5, 5),\
                                                                     randint(0, 5)
        enemy = Enemy(enemy_type[0], enemy_type[1], enemy_type[2], enemy_type[3],
                      enemy_type[4], enemy_type[5], enemy_type[6], enemy_type[7], enemy_type[8])
        # добавление врага в список объектов
        queue.append(enemy)

    # обработка коллизии
    # не важно как, оно работает
    for enem in queue:
        # проверка жив ли враг и находится ли он на экране
        if (not enem.is_alive() or enem.get_x() < -enem.get_size_x() or enem.get_x() > WIDTH
                or enem.get_y() > HEIGHT or enem.get_y() < -enem.get_size_y()):
            # удаление из списка если нет
            queue.remove(enem)

        # действия врага
        enem.tick_time()
        if enem.can_shoot():
            ball = enem.shoot()
            enemy_bullets.append(ball)

        enem.draw_rect(screen)
        enem.go()

        if collide(hero.get_x(), hero.get_y(), hero.get_x() + hero.get_size_x(), hero.get_y() + hero.get_size_y(),
                   enem.get_x(), enem.get_y(),
                   enem.get_x() + enem.get_size_x(), enem.get_y() + enem.get_size_y()):
            hero.set_hp(-1)
            enem.set_hp(-1)

        # коллизия с пулями
        for heart in bullets:
            if collide(heart.get_x(), heart.get_y(), heart.get_x() + heart.get_size_x(),
                       heart.get_y() + heart.get_size_y(),
                       enem.get_x(), enem.get_y(),
                       enem.get_x() + enem.get_size_x(), enem.get_y() + enem.get_size_y()):
                heart.set_hp(-1)
                enem.set_hp(-1)

    # рисую пули врагов и удаляю лишние из списка и проверяю коллизию с героем
    for shot in enemy_bullets:
        # проверка нужна ли пуля
        if not shot.is_alive() or shot.get_y() < -shot.get_size_y():
            enemy_bullets.remove(shot)
        # отрисовка пули
        shot.draw_rect(screen)
        shot.go()

        # коллизия пули с героем
        if collide(hero.get_x(), hero.get_y(), hero.get_x() + hero.get_size_x(), hero.get_y() + hero.get_size_y(),
                   shot.get_x(), shot.get_y(),
                   shot.get_x() + shot.get_size_x(), shot.get_y() + shot.get_size_y()):
            hero.set_hp(-1)
            shot.set_hp(-1)

    if hero.is_alive():
        hero.draw_rect('hero.png', screen)
    else:
        print('you lose')
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
quit()
