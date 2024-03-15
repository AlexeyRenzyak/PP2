import pygame
pygame.init()



screen = pygame.display.set_mode((700, 525), pygame.RESIZABLE)
pygame.display.set_caption("Circle")



clock = pygame.time.Clock()
pos = (350,525/2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and (pos[0] - 20 >= 25):
                pos = (pos[0]-20, pos[1])
            if event.key == pygame.K_RIGHT and (pos[0] + 20 <= screen.get_size()[0] - 25):
                pos = (pos[0]+20, pos[1])
            if event.key == pygame.K_UP and (pos[1] - 20 >= 25):
                pos = (pos[0], pos[1]-20)
            if event.key == pygame.K_DOWN and (pos[1] + 20 <= screen.get_size()[1] - 25):
                pos = (pos[0], pos[1]+20)

        if event.type == pygame.QUIT:
            exit()
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0),pos, 25)
    clock.tick(60)
    pygame.display.flip()