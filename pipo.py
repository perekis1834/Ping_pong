from pygame import *

win = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
back = transform.scale(image.load('фон типа.jpg'), (700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, w, h, pl_x, pl_y, pl_speed):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (w,h))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 335:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 335:
            self.rect.y += self.speed
    ##global sp_y
    def move3(self):
        self.rect.x += self.speed
        self.rect.y -= self.speed
        #self.rect.x += sp_x
        #self.rect.y += sp_y
        if self.rect.y < 25 or self.rect.y > 475:
            self.speed *= -1
        if sprite.collide_rect(pl1, ball):
            self.speed *= -1
        if sprite.collide_rect(pl2, ball):
            self.speed *= -1

pl1 = Player('синька.png', 20, 165, 30, 100, 3)
pl2 = Player('зеленка.png', 20, 165, 650, 100, 3)
ball = Player('мишин мяч.png', 50, 50, 300, 50, 3)

font.init()
font1 = font.Font(None, 50)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

run = True
finish = False
while run:
    for e in event.get(): 
        if e.type == QUIT:
            run = False
    win.blit(back, (0,0))
    pl1.move2()
    pl2.move1()
    ball.reset()
    ball.move3()
    pl1.reset()
    pl2.reset()
    if ball.rect.x < 0:
        finish = True
        win.blit(lose1, (200,200))
    if ball.rect.x > 700:
            finish = True
            win.blit(lose2, (200,200))
    display.update()
    clock.tick(60)









