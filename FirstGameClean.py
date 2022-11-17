# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:17:06 2022

@author: Sergei
"""

# =============================================================================
# Packages
# =============================================================================

import pygame
from sys import exit

# =============================================================================
# Must have
# =============================================================================

# iniciate pygame

pygame.init()

# Window for the game

screen = pygame.display.set_mode((800,400))

# Name of the window

pygame.display.set_caption("Runner")

# clock object for controling the frame rate

clock = pygame.time.Clock()

# =============================================================================
# Fonts for text
# =============================================================================

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# =============================================================================
# Surfaces 
# =============================================================================

# sky

sky_surface = pygame.image.load("graphics/Sky.png").convert()

# groud

ground_surface = pygame.image.load("graphics/ground.png").convert()

# text

score_surface = test_font.render("0", False, (64,64,64))
score_rect = score_surface.get_rect(midbottom= (750,50))

# snail

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom= (800, 300))

# player

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom= (80, 300))

#creating this variable to be able to animate de snail

# =============================================================================
# Variables for animation
# =============================================================================

# animating the snail 

snail_x_pos = 800

# gravity

player_gravity = 0


# =============================================================================
# ############################### Run the game ###############################
# =============================================================================

while True:
    # event to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
     # implementing a jump with the mouse
     
        if event.type == pygame.MOUSEBUTTONDOWN:
            # jumping when we click the player
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                 player_gravity = - 20
        
     # implementing a jump with space bar
     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = - 20


    
# =============================================================================
# Displaying surfaces
# =============================================================================
    
# sky
 
    screen.blit(sky_surface ,(0,0))
    
# ground

    screen.blit(ground_surface ,(0,300))
    
# snail
    
    screen.blit(snail_surface, (snail_rect))
    # displaying the snail and animate it.
    
# player
    
    screen.blit(player_surface,(player_rect))
    
# =============================================================================
# Drawings and text
# =============================================================================
    
# adding a rectagle with color around the text
    
    pygame.draw.rect(screen, "#c0e9ec", score_rect)
    pygame.draw.rect(screen, "#c0e9ec", score_rect, 10,20)
    
    #text

    screen.blit(score_surface,(score_rect))


# =============================================================================
# Animations 
# =============================================================================
    

########### Player #########


# increasing the gravity 

    player_gravity += 1
    
    
# applying gravity to the player
    
    player_rect.y += player_gravity
    
# creating a floor 
    
    if player_rect.bottom >=300: 
        player_rect.bottom = 300
        
    
########### Snail #########

# animating the snail
     
    if snail_rect.left >= -100:
        snail_rect.left -= 4
    else:
        snail_rect.left = 800
    
  
# =============================================================================
# Collisions    
# =============================================================================
  
# collision between snail and player
    
    if player_rect.colliderect(snail_rect):
        print("Collision")

# collision between player and mouse

    # getting the mouse position
    
    mouse_position = pygame.mouse.get_pos()
    
    # using the position to detect colition between player and mouse
    
    if player_rect.collidepoint((mouse_position)):
        print("Collision")
        
    
# =============================================================================
#Technical Stuff
# =============================================================================
    
    # update the game
    
    pygame.display.update()
    
    # setting the frames 
    
    clock.tick(60)
    