         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   # метод для управления спрайтом стрелками клавиатуры
   def updatel(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.x > 0:
           self.rect.x -= self.speed
       if keys[K_DOWN] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
   def updater(self):
       keys = key.get_pressed()
       if keys[K_W] and self.rect.x > 0:
           self.rect.x -= self.speed
       if keys[K_S] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
rocket1 = Player('racket.png' ,0, 250, 30, 100, 10)
rocket2 = Player('racket.png' ,670, 250, 30, 100, 10)
ball = GameSprite('tenis_ball.png', 250, 250, 50, 50, 10)
game = True
while game:
    window.blit(background, (0, 0))
    rocket1.reset()
    rocket2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
                game = False
    display.update()
    clock.tick(60)
