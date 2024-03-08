from pygame.sprite import Group
from pygame import* 
from random import randint
raket = 'raket.png'
monster = 'monster.png'
galeks = 'galeksi.PNG'
#pulae = 'pulae.png'

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
        if keys_pressed [K_UP] and self.rect.x > 5 : 
            self.rect.x -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_DOWN] and self.rect.x < win_width - 50 : 
            self.rect.x += self.speed 


raket = Player('racket.png', 30, 200, 4, 50, 150) 
monster = Player('monster.png', 520, 200, 4, 50, 150)
font.init()
font = font.Font(None, 35)
win_width = 700 
win_height = 500 

window = display.set_mode((win_width, win_height)) 
display.set_caption("Shooter Game") 
background = transform.scale(image.load("galeksi.PNG"), (win_width, win_height))


raket = Player('raket.png', 30, 20, 4, 50, 150)
finish = True

 
while run: 
 
    #подія натискання на кнопку закрити 
     
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 

        # elif e.type == KEYDOWN:
        #     if e.key == K_SPACE:
 




    if not finish: 
 
        window.blit(background, (0, 0)) 
         
 
    display.update() 
 
    time.delay(50)