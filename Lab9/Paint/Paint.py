import pygame
import math


def main():
    pygame.init()
    pygame.display.set_caption("Paint")
    screen = pygame.display.set_mode((1280, 720))
    drawsurface = pygame.Surface((1280, 720))
    drawsurface.fill((255,255,255))
    color_sel = pygame.Surface((1280, 720))
    color_sel.fill((0,0,0))

    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
    
    
    mode = "line"


    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Verdana", 26)
    
    drawing = False

    in_colorsel = False
    counter = 0

    caption = font.render("Black - Q", True, (255,255,255))
    color_sel.blit(caption, (15, 40 +(counter*20)))
    counter += 1
    caption = font.render("Red - R", True, (255,0,0))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1
    caption = font.render("Green - G", True, (0,255,0))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1
    caption = font.render("Blue - B", True, (0,0,255))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1
    caption = font.render("Yellow - Y", True, (255,255,0))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1
    caption = font.render("Cyan - C", True, (0,255,255))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1
    caption = font.render("Magenta - M", True, (255,0,255))
    color_sel.blit(caption, (15, 40 +(counter*40)))
    counter += 1




    color = (0, 0, 0)
    usingcolor = (0, 0, 0)

    eraser = False


    pos1 = (0, 0)
    pos2 = (0, 0)
    drag_init_pos = (0,0)
    screen.fill((255, 255, 255))
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_e:
                    if eraser == False:
                        eraser = True
                        usingcolor = (255, 255, 255)
                    else:
                        eraser = False
                        usingcolor = color
                if event.key == pygame.K_r and in_colorsel == False:
                    mode = "rectangle"
                if event.key == pygame.K_i and in_colorsel == False:
                    mode = "circle"
                if event.key == pygame.K_s and in_colorsel == False:
                    mode = "square"
                if event.key == pygame.K_t and in_colorsel == False:
                    mode = "rtri"
                if event.key == pygame.K_q and in_colorsel == False:
                    mode = "etri"
                if event.key == pygame.K_h and in_colorsel == False:
                    mode = "rhombus"
                #Color Selection
                if in_colorsel:
                    if event.key == pygame.K_q:
                        in_colorsel = False
                        color = (0,0,0)
                    if event.key == pygame.K_r:
                        in_colorsel = False
                        color = (255,0,0)
                    if event.key == pygame.K_g:
                        in_colorsel = False
                        color = (0,255,0)
                    if event.key == pygame.K_b:
                        in_colorsel = False
                        color = (0,0,255)
                    if event.key == pygame.K_y:
                        in_colorsel = False
                        color = (255,255,0)
                    if event.key == pygame.K_c:
                        in_colorsel = False
                        color = (0,255,255)
                    if event.key == pygame.K_m:
                        in_colorsel = False
                        color = (255,0,255)
                if event.key == pygame.K_w:
                    if in_colorsel == False:
                        in_colorsel = True
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    drag_init_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    #Draw a rectangle on main surface and clear preview surface
                    if mode == "rectangle":
                        left = 0
                        right = 0
                        up = 0
                        down = 0
                        if drag_init_pos[0] < pygame.mouse.get_pos()[0]:
                            left = drag_init_pos[0]
                            right = pygame.mouse.get_pos()[0] - drag_init_pos[0]
                        else:
                            left = pygame.mouse.get_pos()[0]
                            right = drag_init_pos[0] - pygame.mouse.get_pos()[0]
                        if drag_init_pos[1] < pygame.mouse.get_pos()[1]:
                            up = drag_init_pos[1]
                            down = pygame.mouse.get_pos()[1] - drag_init_pos[1]
                        else:
                            up = pygame.mouse.get_pos()[1]
                            down = drag_init_pos[1] - pygame.mouse.get_pos()[1]

                        pygame.draw.rect(drawsurface, usingcolor, pygame.Rect(left, up, right, down), 5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"

                    #Draw a circle on main surface and clear preview surface
                    elif mode == "circle":
                        pygame.draw.circle(drawsurface, usingcolor, drag_init_pos, math.sqrt(math.pow(drag_init_pos[0]-pygame.mouse.get_pos()[0],2) + math.pow(drag_init_pos[1]-pygame.mouse.get_pos()[1],2)),5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"

                    #Draw a square on main surface and clear preview surface
                    elif mode == "square":
                        pygame.draw.rect(drawsurface, usingcolor, pygame.Rect(drag_init_pos[0], drag_init_pos[1], max(pygame.mouse.get_pos()[0]-drag_init_pos[0], pygame.mouse.get_pos()[1]-drag_init_pos[1]), max(pygame.mouse.get_pos()[0]-drag_init_pos[0], pygame.mouse.get_pos()[1]-drag_init_pos[1])), 5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"

                    #Draw a right triangle on main surface and clear preview surface
                    elif mode == "rtri":
                        p1 = (drag_init_pos[0], drag_init_pos[1])
                        p2 = (drag_init_pos[0], pygame.mouse.get_pos()[1])
                        p3 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                        pygame.draw.line(drawsurface, usingcolor, p1, p2, 5)
                        pygame.draw.line(drawsurface, usingcolor, p2, p3, 5)
                        pygame.draw.line(drawsurface, usingcolor, p3, p1, 5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"

                    #Draw an equilateral triangle on main surface and clear preview surface
                    elif mode == "etri":
                        p1 = (drag_init_pos[0], drag_init_pos[1])
                        p2 = (pygame.mouse.get_pos()[0], drag_init_pos[1])
                        p3 = ((p1[0]+p2[0])/2, drag_init_pos[1]+math.copysign(abs((p1[0]-p2[0]))*math.sqrt(3)/2, pygame.mouse.get_pos()[1]- p1[1]))
                        pygame.draw.line(drawsurface, usingcolor, p1, p2, 5)
                        pygame.draw.line(drawsurface, usingcolor, p2, p3, 5)
                        pygame.draw.line(drawsurface, usingcolor, p3, p1, 5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"

                    #Draw a rhombus on main surface and clear preview surface
                    elif mode == "rhombus":
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        preview.fill((255,255,255, 0))
                        p1 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0])/2, drag_init_pos[1])
                        p2 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0]), drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1])/2)
                        p3 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0])/2, drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1]))
                        p4 = (drag_init_pos[0], drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1])/2)
                        pygame.draw.line(drawsurface, usingcolor, p1, p2, 5)
                        pygame.draw.line(drawsurface, usingcolor, p2, p3, 5)
                        pygame.draw.line(drawsurface, usingcolor, p3, p4, 5)
                        pygame.draw.line(drawsurface, usingcolor, p4, p1, 5)
                        preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                        mode = "line"
                    drag_init_pos = (0,0)



    
            #Changed painting logic for better flexibility
            if event.type == pygame.MOUSEMOTION:
                pos1 = pygame.mouse.get_pos()
                if drawing and in_colorsel == False and mode == "line":
                    pygame.draw.line(drawsurface, usingcolor, pos2, pos1, 5)
                    #For smooting jagged lines
                    pygame.draw.circle(drawsurface, usingcolor, pos2, 1)
                #Drawing rectangle and rendering as dynamic preview surface
                elif drawing and in_colorsel == False and mode == "rectangle":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    left = 0
                    right = 0
                    up = 0
                    down = 0
                    if drag_init_pos[0] < pygame.mouse.get_pos()[0]:
                        left = drag_init_pos[0]
                        right = pygame.mouse.get_pos()[0] - drag_init_pos[0]
                    else:
                        left = pygame.mouse.get_pos()[0]
                        right = drag_init_pos[0] - pygame.mouse.get_pos()[0]
                    if drag_init_pos[1] < pygame.mouse.get_pos()[1]:
                        up = drag_init_pos[1]
                        down = pygame.mouse.get_pos()[1] - drag_init_pos[1]
                    else:
                        up = pygame.mouse.get_pos()[1]
                        down = drag_init_pos[1] - pygame.mouse.get_pos()[1]

                    pygame.draw.rect(preview, usingcolor, pygame.Rect(left, up, right, down), 5)

                #Drawing a square by selecting the bigger of horizontal or vertical drag offset and rendering as preview
                elif drawing and in_colorsel == False and mode == "square":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    pygame.draw.rect(preview, usingcolor, pygame.Rect(drag_init_pos[0], drag_init_pos[1], max(pygame.mouse.get_pos()[0]-drag_init_pos[0], pygame.mouse.get_pos()[1]-drag_init_pos[1]), max(pygame.mouse.get_pos()[0]-drag_init_pos[0], pygame.mouse.get_pos()[1]-drag_init_pos[1])), 5)

                #Drawing Right Triangle as preview
                elif drawing and in_colorsel == False and mode == "rtri":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    p1 = (drag_init_pos[0], drag_init_pos[1])
                    p2 = (drag_init_pos[0], pygame.mouse.get_pos()[1])
                    p3 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    pygame.draw.line(preview, usingcolor, p1, p2, 5)
                    pygame.draw.line(preview, usingcolor, p2, p3, 5)
                    pygame.draw.line(preview, usingcolor, p3, p1, 5)

                #Drawing Equilateral Triangle from its base as preview
                elif drawing and in_colorsel == False and mode == "etri":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    p1 = (drag_init_pos[0], drag_init_pos[1])
                    p2 = (pygame.mouse.get_pos()[0], drag_init_pos[1])
                    p3 = ((p1[0]+p2[0])/2, drag_init_pos[1]+math.copysign(abs((p1[0]-p2[0]))*math.sqrt(3)/2, pygame.mouse.get_pos()[1]- p1[1]))
                    pygame.draw.line(preview, usingcolor, p1, p2, 5)
                    pygame.draw.line(preview, usingcolor, p2, p3, 5)
                    pygame.draw.line(preview, usingcolor, p3, p1, 5)

                #Drawing rhombus by calculating points in relation to origin and drag offset from its base as preview
                elif drawing and in_colorsel == False and mode == "rhombus":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    p1 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0])/2, drag_init_pos[1])
                    p2 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0]), drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1])/2)
                    p3 = (drag_init_pos[0]+(pygame.mouse.get_pos()[0]-drag_init_pos[0])/2, drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1]))
                    p4 = (drag_init_pos[0], drag_init_pos[1]+(pygame.mouse.get_pos()[1]-drag_init_pos[1])/2)
                    pygame.draw.line(preview, usingcolor, p1, p2, 5)
                    pygame.draw.line(preview, usingcolor, p2, p3, 5)
                    pygame.draw.line(preview, usingcolor, p3, p4, 5)
                    pygame.draw.line(preview, usingcolor, p4, p1, 5)

              
                #Drawing circle and rendering as dynamic preview surface
                elif drawing and in_colorsel == False and mode == "circle":
                    preview = pygame.Surface((1280, 720),pygame.SRCALPHA)
                    preview.fill((255,255,255, 0))
                    pygame.draw.circle(preview, usingcolor, drag_init_pos, math.sqrt(math.pow(drag_init_pos[0]-pygame.mouse.get_pos()[0],2) + math.pow(drag_init_pos[1]-pygame.mouse.get_pos()[1],2)), 5)

                pos2 = pos1
        if eraser == False:
            usingcolor = color
        #Labels
        gui = pygame.Surface((1280, 720), pygame.SRCALPHA)
        caption1 = font.render("Color Selection - W", True, (75,75,75))
        gui.blit(caption1, (20,640))
        if eraser == False:
            caption2 = font.render("Eraser - E", True, (75,75,75))
            gui.blit(caption2, (20,680))
        else:
            caption2 = font.render("Color Mode - E", True, (75,75,75))
            gui.blit(caption2, (20,680))
        caption3 = font.render("Rectangle - R", True, (75,75,75))
        caption4 = font.render("Circle - I", True, (75,75,75))
        caption5 = font.render("Square - S", True, (75,75,75))
        caption6 = font.render("R. Triangle - T", True, (75,75,75))
        caption7 = font.render("Equilat. Triangle - Q", True, (75,75,75))
        caption8 = font.render("Rhombus - H", True, (75,75,75))
        gui.blit(caption3, (1000,640))
        gui.blit(caption4, (1000,680))
        gui.blit(caption5, (1000,600))
        gui.blit(caption6, (1000,560))
        gui.blit(caption7, (1000,520))
        gui.blit(caption8, (1000,480))
        screen.blit(drawsurface, (0,0))  
        if mode == "rectangle" or mode == "circle" or mode == "square" or mode == "rtri" or mode == "etri" or mode == "rhombus":
            screen.blit(preview, (0,0))
        screen.blit(gui, (0,0))
        if in_colorsel:
            screen.blit(color_sel, (0,0))
        pygame.display.flip()
        clock.tick(60)



main()