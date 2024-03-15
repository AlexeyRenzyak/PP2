import pygame
import datetime
pygame.init()



screen = pygame.display.set_mode((700, 525))
pygame.display.set_caption("Clock")
im2 = pygame.image.load(r"Lab7\Assets\leftarm2.png")
im2ref = im2
im2 = pygame.transform.scale(im2, (32, 525))

im3 = pygame.image.load(r"Lab7\Assets\rightarm.png")
im3 = pygame.transform.scale(im3, (700, 525))
im3ref = im3

im1 = pygame.image.load("Lab7\Assets\mainclock.png")
im1 = pygame.transform.scale(im1, (700, 525))

t = datetime.datetime.now()

clock = pygame.time.Clock()

angle1 = 0 - (t.microsecond/1000000)*6
angle2 = -47 - t.minute*6 - (angle1/60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255,0,0))
    t = datetime.datetime.now()


    angle1 = (0 - t.second - (t.microsecond/1000000))*6
    angle2 = -47 - (t.minute+(t.second/60))*6

    im2 = pygame.transform.rotozoom(im2ref, angle1, 0.5)
    im3 = pygame.transform.rotozoom(im3ref, angle2, 1)

    c = im2.get_rect(center = im2ref.get_rect(center = im1.get_rect().move(0,0).center).center)
    c2 = im3.get_rect(center = im3ref.get_rect(center = im1.get_rect().move(0,0).center).center)
    screen.blit(im1, (0, 0))
    screen.blit(im3, c2)
    screen.blit(im2, c)

    clock.tick(60)
    pygame.display.flip()
    