import pygame
import os
pygame.init()



screen = pygame.display.set_mode((700, 525))
pygame.display.set_caption("Player")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 40)

currenttrack = ''

text1 = font.render("Music Player", True, (0, 0, 0))
text2 = font.render("Play - P", True, (0, 0, 0))
text3 = font.render("Stop - S", True, (0, 0, 0))
text4 = font.render("Next - RArrow", True, (0, 0, 0))
text5 = font.render("Previous - LArrow", True, (0, 0, 0))
text6 = font.render("Nothing is playing", True, (0, 0, 0))



#Put any mp3 there. Non-audio files may crash the player
path = "Lab7/Music!"



playlist = []
current_pos = 0

for x in os.listdir(path):
    if not os.path.isdir(path+"\\"+x): playlist.append(x)
print(len(playlist))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            currenttrack = playlist[current_pos]
            pygame.mixer.music.load("Lab7/Music!/"+currenttrack)
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and currenttrack != "":
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pygame.mixer.music.stop()
            if (current_pos + 1) == 1:
                current_pos = len(playlist) - 1
            else:
                current_pos -= 1
            currenttrack = playlist[current_pos]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pygame.mixer.music.stop()
            if (current_pos + 1) == len(playlist):
                current_pos = 0
            else:
                current_pos += 1
            currenttrack = playlist[current_pos]
        if event.type == pygame.QUIT:
            exit()
    screen.fill((255,255,255))
    if currenttrack == '':
        text6 = font.render("Nothing is Playing", True, (0, 0, 0))
    elif pygame.mixer.music.get_busy():
        text6 = font.render("Playing: " + currenttrack, True, (0, 0, 0))
    else:
        text6 = font.render("Selected: " + currenttrack, True, (0, 0, 0))


    screen.blit(text1,(700/2 - text1.get_width() // 2, text1.get_height() // 2))
    screen.blit(text2,(700/2 - text2.get_width() // 2, 130/2 - text2.get_height() // 2))
    screen.blit(text3,(700/2 - text3.get_width() // 2, 200/2 - text3.get_height() // 2))
    screen.blit(text4,(700/2 - text4.get_width() // 2, 270/2 - text4.get_height() // 2))
    screen.blit(text5,(700/2 - text5.get_width() // 2, 330/2 - text5.get_height() // 2))
    screen.blit(text6,(700/2 - text6.get_width() // 2, 750/2 - text6.get_height() // 2))

    clock.tick(60)
    pygame.display.flip()