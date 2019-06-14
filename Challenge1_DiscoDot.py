# DiscoDot.py
import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800, 600])

keepGoing = True
PURPLE = (128,0,128) # RGB color triplet for GREEN
radius = 75

while keepGoing:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keepGoing = False
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #for i in range(150):
        #x = random.randint(1, 700)
        #y = random.randint(0, 500)
        #ls.append([x, y])    
    pygame.draw.circle(screen, color, (100,100), radius)
    pygame.display.update()
   
pygame.quit()
