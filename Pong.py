from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (width, height))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   # метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 0:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < 400:
           self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

racket1 = Player('racket.png', 0, 150, 30, 100, 15)
racket2 = Player('racket.png', 670, 100, 30, 100, 15)
ball = GameSprite('tenis_ball.png', 300, 300, 50, 50, 10)
finish = False
game = True
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None , 35)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
font1 = font.Font(None , 35)
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        racket1.update_r()
        racket2.update_l()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2,(200, 200))
    display.update()
    clock.tick(60)
