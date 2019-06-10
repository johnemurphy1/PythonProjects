# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:05:56 2019

@author: John
"""

import pygame
pygame.init
screenHeight = 480
screenWidth = 600
screen = pygame.display.set_mode([screenWidth,screenHeight])
keep_going = True
pic = pygame.image.load("assets/CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
speedx = 5
speedy = 5

while keep_going: # Game Loop
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
    picx += speedx
    picy += speedy
    
    if picx <= 0 or picx + pic.get_width() >= screenWidth:
        speedx = 0 - speedx

    if picy <= 0 or picy + pic.get_height() >= screenHeight:
        speedy = 0 - speedy
        
    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    timer.tick(60)
    
pygame.quit()