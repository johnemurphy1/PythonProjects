# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:19:52 2019

@author: John
"""

import pygame
import random as rand

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")
keep_going= True
colorkey = rand.randrange(0,255)
radius = 15
mousedown = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, colorkey, spot, radius)
    pygame.display.update()
    
pygame.quit()