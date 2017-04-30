import pygame
import random
import math

pygame.init()

background_colour = (0,0,0)
(width,height)=(600,600)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Tutorial 2')
screen.fill(background_colour)

pygame.display.flip()


running = True

main_character_colour = (255,255,255)
w, h = pygame.display.get_surface().get_size()
mainx=w/2
destinationx=mainx
mainy=h/2
destinationy=mainy
main_radius = 16
speedx = 0
speedy = 0
speed=0
distance=0
fps = 60
while running:
    
    if pygame.mouse.get_pressed()[2]:
        x,y = pygame.mouse.get_pos()
        destinationx = x
        destinationy= y
    diffy = destinationy-mainy
    diffx = destinationx-mainx
    distance = math.sqrt((diffy*diffy) +(diffx*diffx))
    direction = math.atan2(diffy,diffx)
    speed = min(distance,4.0)
    speedx = speed * math.cos(direction)
    speedy = speed * math.sin(direction)
    mainx += int(speedx)
    mainy += int(speedy)

    screen.fill(background_colour)
    pygame.draw.circle(screen,main_character_colour,(mainx,mainy),main_radius, 0)
    pygame.draw.circle(screen,main_character_colour,(mainx,mainy),64, 1)
    
    print(str(mainx)+"," +str(destinationx)+","+ str(mainy)+","+ str(destinationy))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.display.quit()
