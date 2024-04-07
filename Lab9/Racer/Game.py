import pygame, sys
from pygame.locals import *
import random, time


pygame.init()
pygame.display.set_caption("Racer")

FPS = 60
FramePerSec = pygame.time.Clock()


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ESPEED = 5
SPEED = 5
SCORE = 0

#Coin score variable
COINS = 0



font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("Lab9/Racer/AnimatedStreet.png")


DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self, r):
        super().__init__() 
        self.image = pygame.image.load("Lab9/Racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.r = r
        self.rect.center = (random.randint(40+self.r[0],self.r[1]-40), 0)
        self.speed = ESPEED + random.randrange(-1, 1)

      def move(self):
        global SCORE
        self.rect.move_ip(0,self.speed)
        if (self.rect.bottom > 800):
            SCORE += 1
            self.rect.top = -50
            self.speed = ESPEED + random.randrange(-1, 1)
            self.rect.center = (random.randint(40+self.r[0],self.r[1]-40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab9/Racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Coin class, similar to enemy, but can spawn anywhere, moves with global speed without random, 
#self-destructs in the end and has value property
class Coin(pygame.sprite.Sprite):
      def __init__(self, value):
        super().__init__() 
        self.image = pygame.image.load("Lab9/Racer/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        self.value = value

      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 800):
            coins.remove(self)
            all_sprites.remove(self)

                  

      
P1 = Player()
E1 = Enemy([0, 200])
E2 = Enemy([200, 400])





enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
#Coin group
coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)



INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


#How many coins are needed for speedup
N = 10

while True:
      
    #Increase base enemy speed by 1 every N coins
    ESPEED = SPEED + (COINS//N)

    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.2      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Random Coin Spawn
    if random.randint(1, 150) == 1:
        coin = Coin(random.randint(1,5))
        coins.add(coin)
        all_sprites.add(coin)


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))



    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        


    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('Lab9/Racer/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()    

    #Collision with coins
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += pygame.sprite.spritecollide(P1, coins, 0)[0].value
        all_sprites.remove(pygame.sprite.spritecollide(P1, coins, 0)[0])
        coins.remove(pygame.sprite.spritecollide(P1, coins, 0)[0])
        
    #Coin counter render
    scores = font_small.render("Coins: "+str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (300,10))
        
    pygame.display.update()
    FramePerSec.tick(FPS)
