import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

pausescreen = pygame.Surface((1200, 800))
pausescreen.fill((255,255,255))



#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

ps1 = game_score_fonts.render("Arkanoid", True, (0, 0, 0))


settings = False

sound = True
DiffMultiplier = 1.0


#Catching sound
collision_sound = pygame.mixer.Sound('Lab9/Arkanoid/catch.mp3')

#Timer for difficulty increase
INC_DIFFICULTY = pygame.USEREVENT + 1
pygame.time.set_timer(INC_DIFFICULTY, 1500)

paused = True

status = "game"

contbutton = pygame.Surface((200,100))
ps2 = game_score_fonts.render("Continue", True, (0, 0, 0))
contbutton.fill((100,100,100))
contbutton.blit(ps2, (100 - ps2.get_size()[0]/2, 20))

settbutton = pygame.Surface((200,100))
ps3 = game_score_fonts.render("Settings", True, (0, 0, 0))
settbutton.fill((100,100,100))
settbutton.blit(ps3, (100 - ps3.get_size()[0]/2, 20))

soundbutton1 = pygame.Surface((200,100))
ps4 = game_score_fonts.render("Sound On", True, (0, 0, 0))
soundbutton1.fill((100,100,100))
soundbutton1.blit(ps4, (100 - ps4.get_size()[0]/2, 20))

soundbutton2 = pygame.Surface((200,100))
ps5 = game_score_fonts.render("Sound Off", True, (0, 0, 0))
soundbutton2.fill((100,100,100))
soundbutton2.blit(ps5, (100 - ps5.get_size()[0]/2, 20))

multbutton = pygame.Surface((400,100))
ps6 = game_score_fonts.render(f"Difficulty Mod: {DiffMultiplier}", True, (0, 0, 0))
multbutton.fill((100,100,100))
multbutton.blit(ps6, (200 - ps6.get_size()[0]/2, 20))

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]

#Overriden default random color system for designating buffed bricks
buff_list = []
color_list = []
buffs = ["paddleplus", "slow", "paddlespeed", "paddleplus", "slow", "paddlespeed", "bossbrick" ]
for x in range(4*10):
    if random.randint(0, 100) <= 30:
        buff_list.append(buffs[random.randint(0,len(buffs)-1)])
    else:
        buff_list.append("None")
for x in buff_list:
    if x == "None":
        color_list.append((200,0,0))
    elif x == "paddleplus":
        color_list.append((130,130,130))
    elif x == "slow":
        color_list.append((0,0,200))
    elif x == "paddlespeed":
        color_list.append((200,0,200))
    elif x == "bossbrick":
        color_list.append((255,255,255))


print(block_list)
#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

brickfont = pygame.font.SysFont('comicsansms', 25)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and status == "game" and paused == False:
                paused = True
            elif event.key == pygame.K_ESCAPE and status == "game" and paused == True:
                paused = False
                settings = False
        if event.type == pygame.MOUSEBUTTONUP and paused:
            if settings == False:
                if contbutton.get_rect(topleft=(500, 450)).collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    settings = False
                if settbutton.get_rect(topleft=(500, 300)).collidepoint(pygame.mouse.get_pos()): 
                    settings = True
            elif settings == True:
                if contbutton.get_rect(topleft=(500, 600)).collidepoint(pygame.mouse.get_pos()):
                    paused = False
                    settings = False
                if soundbutton1.get_rect(topleft=(500, 200)).collidepoint(pygame.mouse.get_pos()):
                    if sound:
                        sound = False
                    else:
                        sound = True
                if multbutton.get_rect(topleft=(400, 400)).collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        DiffMultiplier += 0.1
                    elif event.button == 3:
                        if DiffMultiplier > 0.2:
                            DiffMultiplier -= 0.1

        #Applying difficulty modifiers with limits, not to make the game unplayable
        if event.type == INC_DIFFICULTY:
            if ballSpeed < 9:
                ballSpeed += 0.1
            if paddle.width > 75:
                paddle.width -= 1*DiffMultiplier

    screen.fill(bg)
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    if paused == False:
        ball.x += ballSpeed * dx * DiffMultiplier
        ball.y += ballSpeed * dy * DiffMultiplier

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        if buff_list[hitIndex] != "bossbrick":
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            hitBuff = buff_list.pop(hitIndex)
            #Apply corresponding buff
            if hitBuff == "paddleplus":
                paddle.width += 20
            elif hitBuff == "slow":
                if ballSpeed >= 1.5:
                    ballSpeed -= 1.5
            elif hitBuff == "paddlespeed":
                paddleSpeed += 2
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        if sound:
            collision_sound.play()
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        status = "lose"
    elif not len(block_list):
        screen.fill((255,255, 255))
        ballSpeed = 0
        screen.blit(wintext, wintextRect)
        status = "win"
    # print(pygame.K_LEFT)
    #Paddle Control
    if paused == False:
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
    else:
        pausescreen.fill((255,255,255))
        pausescreen.blit(ps1, (600 - ps1.get_size()[0]/2, 100))
        if settings == False:
            pausescreen.blit(settbutton,(500, 300))
            pausescreen.blit(contbutton,(500, 450))
        else:
            ps6 = game_score_fonts.render(f"Difficulty Mod: {round(DiffMultiplier,1)}", True, (0, 0, 0))
            multbutton.fill((100,100,100))
            multbutton.blit(ps6, (200 - ps6.get_size()[0]/2, 20))
            pausescreen.blit(contbutton,(500, 600))
            if sound:
                pausescreen.blit(soundbutton1,(500, 200))
            else:
                pausescreen.blit(soundbutton2,(500, 200))
            pausescreen.blit(multbutton, (400, 400))
        screen.blit(pausescreen, (0,0))
    pygame.display.flip()
    clock.tick(FPS)