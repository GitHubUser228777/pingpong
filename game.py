from pygame import *
import time as pytime
colour = 144, 174, 255
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пин-понг')
window.fill(colour)

finish = False
run = True
fps = 60
clock = time.Clock()
ball_speed_x = 3
ball_speed_y = 3
score1 = 0
score2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def restart(self, player_x, player_y, player_speed):
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

racket1 = Player('player1.png', 10, 250, 3, 30, 100)
racket2 = Player('player1.png', 660, 250, 3, 30, 100)
ball = GameSprite('player123-transformed.png', 350, 250, 3, 50, 50)

font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 50)
win1 = font1.render('Игрок 1 забивает!!!', True, (255, 215, 0))
win2 = font1.render('Игрок 2 забивает!!!', True, (255, 215, 0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        score1_text = font2.render('Счёт: ' + str(score1) , True, (0, 0 , 0))
        score2_text = font2.render('Счёт: ' + str(score2), True, (0, 0 , 0))
        window.fill(colour)
        window.blit(score1_text, (10, 10))
        window.blit(score2_text, (550, 10))
        racket1.update_l()
        racket2.update()

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1
            ball_speed_x *= 1.1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball_speed_y *= -1 
        if ball.rect.x <= -60:
            window.blit(win2, (180, 200))
            score2 += 1
            ball_speed_x = 3
            ball.restart(350, 250, 3)
            time.delay(1500)
        if ball.rect.x >= 700:
            window.blit(win1, (180, 200))
            score1 += 1
            ball_speed_x = 3
            ball.restart(350, 250, 3)
            time.delay(1500)

        racket1.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(fps)