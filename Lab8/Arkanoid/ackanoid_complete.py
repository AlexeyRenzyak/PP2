import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

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

#Catching sound
collision_sound = pygame.mixer.Sound('Lab8/Arkanoid/catch.mp3')

#Timer for difficulty increase
INC_DIFFICULTY = pygame.USEREVENT + 1
pygame.time.set_timer(INC_DIFFICULTY, 1500)

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
buffs = ["paddleplus", "slow", "paddlespeed", "paddleplus", "slow", "paddlespeed", "bossbrick"]
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
        
        #Applying difficulty modifiers with limits, not to make the game unplayable
        if event.type == INC_DIFFICULTY:
            if ballSpeed < 9:
                ballSpeed += 0.1
            if paddle.width > 75:
                paddle.width -= 1

    screen.fill(bg)
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

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
        collision_sound.play()
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        ballSpeed = 0
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    pygame.display.flip()
    clock.tick(FPS)