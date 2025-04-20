from pygame import *
from random import randint

class Sprite(sprite.Sprite):
    def __init__(self, file_name, x=0, y=0, w=0, h=0, speed=2):
        if not(w == 0 and h == 0):
            self.image = transform.scale(image.load(file_name), (w, h))
        else:
            self.image = image.load(file_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed



class Platform(Sprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.x = random.randint(0, 350)
            self.rect.y -= 50





WINDOW_WIGTH = 350
WINDOW_HEIGHT = 600
FPS = 60
SPEED = 4

window = display.set_mode((WINDOW_WIGTH, WINDOW_HEIGHT))
player = Player("pngwing.com.png", 150, 500, 50, 50, 5)
background = transform.scale(image.load("6204882.jpg"), (WINDOW_WIGTH, WINDOW_HEIGHT))
platform = Platform("Scre0.png", 100, 400, 50, 50, 5)
clock = time.Clock()



run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    platform.update()
    platform.draw(window)
    window.blit(background, (0,0))
    player.update()
    player.draw(window)

    # enemy.update()
    # enemy.draw(window)

    display.update()
    clock.tick(FPS)