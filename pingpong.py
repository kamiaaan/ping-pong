from pygame import *
window = display.set_mode((700, 500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[W_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys_pressed[S_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
   
  
game = True
finish = True
racket1 = Player('racket.png', 20, 200, 30, 100, 15)
racket2 = Player('racket.png', 650, 200, 30, 100, 15)
ball = GameSprite('tenis_ball.png', 300, 200, 50, 50, 20)
while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
           game = False
        
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(60)
    