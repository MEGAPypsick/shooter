from pygame.sprite import Group
from pygame import* 
from random import randint
raket = 'raket.png'
monster = 'monster.png'
galeks = 'galeksi.PNG'
pulae = 'pulae.png'
meteor = 'meteori.png'


class GameSprite(sprite.Sprite): 

    def __init__(self, player_image , player_x , player_y, size_x, size_y, player_speed,player_health): 
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(size_x , size_y))  
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
        self.health = player_health

    def reset (self): 
        window.blit(self.image,(self.rect.x , self.rect.y)) 

class Player(GameSprite): 

    def update_enemy(self): 
        #key = K_SPACE() 
        keys_pressed = key.get_pressed()
        if keys_pressed [K_UP] and self.rect.y > 5 : 
            self.rect.y -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_DOWN] and self.rect.y < win_width - 50 : 
            self.rect.y += self.speed 
            
    def update(self): 
        #key = K_SPACE() 
        keys_pressed = key.get_pressed()
        if keys_pressed [K_w] and self.rect.y > 5 : 
            self.rect.y -= self.speed   

            keys_pressed = key.get_pressed() 
        if keys_pressed [K_s] and self.rect.y < win_width - 50 : 
            self.rect.y += self.speed      
              
    def fire(self):
        keys_pressed = key.get_pressed()

        bullet = Bullet('pulae.png',self.rect.centerx+30,self.rect.top + 20,15,20,10,0)
        bullets.add(bullet)
        
    def fire_m(self):
        keys_pressed = key.get_pressed()
        bullet_m = Bullet_m('pulae_m.png',self.rect.centerx-30,self.rect.top + 100,45,45,10,0)
        bullets_m.add(bullet_m)

class Met(GameSprite):
    def update(self):
        if self.rect.y > 10 and  self.rect.y < 500:
            self.rect.y -= 15
        if self.rect.y <20 :
            self.rect.y += 450
        



class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 :
            self.kill()

class Bullet_m(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 0 :
            self.rect.x -= self.speed
        # if self.rect.x < win_width :
        #     self.rect.x -= self.speed



win_width = 700 
win_height = 500 





bullets = sprite.Group()
bullets_m = sprite.Group()

meteor_ing = 'meteori.png'
raket_img = 'raket.png' 
monster_img = 'monster.png'


font.init()
font = font.SysFont("Arial", 30)


window = display.set_mode((win_width, win_height)) 
display.set_caption("Shooter Game") 
background = transform.scale(image.load("galeksi.png"), (win_width, win_height))
met_y =200
met = Met(meteor, 300, met_y , 65 , 65 , 12.5, 10)
raket = Player('raket.png', 30, 20, 65, 65, 12.5,10)
enemy = Player(monster_img, 550, 120, 120, 140, 20,10)

finish = False
run = True
fly = True


while run: 
 
    #подія натискання на кнопку закрити 
    for e in event.get(): 
        if e.type == QUIT: 
            run = False 
            
        if e.type == KEYDOWN:
            if e.key == K_a:
                    raket.fire()
                    
            if e.key == K_LEFT:
                    enemy.fire_m()


        # elif e.type == KEYDOWN:
        #     if e.key == K_SPACE:


    if not finish: 
        text_win_1 = font.render( "Player 1 Win",True,(22,212,34))
        text_win_2 = font.render( "Player 2 Win",True,(22,212,34))
        health_1 = font.render( f"Health: {raket.health}",True,(22,212,34))
        health_2 = font.render( f"Health: {enemy.health}",True,(22,212,34))
        window.blit(background, (0, 0)) 
        window.blit(health_1,(10,10))
        window.blit(health_2,(win_width-130,10))
        met.reset()
        raket.reset()
        raket.update()
        enemy.reset()
        enemy.update_enemy()
        bullets.draw(window)
        bullets.update()
        bullets_m.draw(window)
        bullets_m.update()
    
        met.update()
        if sprite.spritecollide(raket,bullets_m, True):
            raket.health -=1
            
        if sprite.spritecollide(enemy,bullets, True):
            enemy.health -=1
            
          
        if raket.health < 0 :
            finish = True
            txt_lose_game = font.render('Player 1 Win',True,(255,15,51))
            window.blit(txt_lose_game,(200,150))
        
        if enemy.health < 0 :
            finish = True
            txt_lose_game = font.render('Player 2 Win',True,(255,15,51))
            window.blit(txt_lose_game,(200,150))
        # collide = sprite.groupcollide(monsters,bullets,True,True)
        # for c in collide:
        #     score+=1
        #     enemy = Enemy('m5\\shooter\\ufo.png',randint(0,win_width  - 100),0,100,80,randint(1,4))  
        #     monsters.add(enemy)
         
        if fly:
            met_y+=6
    display.update() 
 
    time.delay(50)