from pygame import *
colour = 255, 255, 255
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

racket1 = Player('player1.png', 20, 250, 3, 30, 100)
racket2 = Player('player1.png', 650, 250, 3, 30, 100)
ball = GameSprite('player123-transformed.png', 350, 250, 3, 50, 50)

font.init()
font = font.Font(None, 70)
win1 = font.render('Player 1 wins!!!', True, (255, 215, 0))
win2 = font.render('Player 2 wins!!!', True, (255, 215, 0))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(colour)
        racket1.update_l()
        racket2.update()

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball_speed_y *= -1 
        if ball.rect.x <= 0:
            window.blit(win2, (180, 200))
            finish = True
        if ball.rect.x >= 700:
            window.blit(win1, (180, 200))
            finish = True

        racket1.reset()
        racket2.reset()
        ball.reset()

    
    display.update()
    clock.tick(fps)