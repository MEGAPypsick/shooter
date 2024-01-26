#Створи власний Шутер!
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

from typing import Any
from pygame import* 
from random import randint
mixer.init() 
mixer.music.load("space.ogg") 
mixer.music.play() 
fire = mixer.Sound('fire.ogg') 
class GameSprite(sprite.Sprite): 

    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(50 , 50))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 

    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite): 
    def update(self): 
        #key = K_SPACE() 
        keys_pressed = key.get_pressed()
        if keys_pressed [K_LEFT] and self.rect.x > 5 : 
            self.rect.x -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_RIGHT] and self.rect.x < win_width - 50 : 
            self.rect.x += self.speed 
 
    def fire(self):
        pass   
        bullet = Bullet(bullet_png, self.rect.x, self.rect.y, 15, 20, -15)
        bullets.add(bullet)
bullets = sprite.Group()
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
skore = 0
lost = 0
class Enemi(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

win_width = 700 
win_height = 500 
 
window = display.set_mode((win_width, win_height)) 
display.set_caption("Shooter Game") 
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height)) 
#зображення 
bullet_png = "bullet.png" 
rocet = "rocket.png" 
ufo= "ufo.png" 
#створюємо спрайти  
rocet = Player(rocet, 10, win_height - 100, 80, 100, 20)
monsters = sprite.Group()
for i in range(1, 10):
    monster = Enemi(ufo,randint(80,win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
finish = False 
game = True

#шрифти
font.init()
font2 = font.Font(None, 45)
font1 = font.Font(None, 45)

txt_lose_game =  font1.render('YOU LOSE', True, [255, 0, 0])
txt_win_game =  font1.render('YOU WIN', True, [0, 255, 0])


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocet.fire()

    if not finish:



        window.blit(background, (0, 0))
        txt_lose = font1.render(f'Пропущено: {lost}', True, (255,255,255))
        window.blit(txt_lose, (10,50))

        txt_win = font1.render(f'Рахуно: {skore}', True, (255,255,255))
        window.blit(txt_win, (10,10))

        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        rocet.reset()
        rocet.update()

        if sprite.spritecollide(rocet, monsters, False):
            finish  = True
            window.blit(txt_lose_game, [200, 200])


        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            mon = Enemi('ufo.png', randint(0, win_width-80), 0, 80, 50, randint(1, 5))
            monsters.add(mon)
            skore += 1

        if skore == 200:
            finish = True
            window.blit(txt_win_game, [200,200])

        if lost == 1:
            finish = True
            window.blit(txt_lose_game, [200,200])


        display.update()
    else:
        skore = 0
        lost = 0
        finish = False
        for m in monsters:
            m.kill()

        for m in bullets:
            m.kill()

        time.delay(3000)
        for i in range(1, 10):
            monster = Enemi(ufo,randint(80,win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
    time.delay(50)






