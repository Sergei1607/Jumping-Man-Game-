# -*- coding: utf-8 -*-
import pygame
from sys import exit

## starts pygame 
## it should be always the first line. 

pygame.init()

# creating the window for the game
# we need to set the width and hight

screen = pygame.display.set_mode((800,400))

# setting the name of the window

pygame.display.set_caption("Runner")

# clock object for controling the frame rate

clock = pygame.time.Clock()

## creating a font for text

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)


# creating a surface
# we need to set the width and hight

#test_surface = pygame.Surface((100, 200))

# adding color to the surface

#test_surface.fill("Red")

# creating a surface with a image

sky_surface = pygame.image.load("graphics/Sky.png").convert()

ground_surface = pygame.image.load("graphics/ground.png").convert()

# adding the surface of the text



score_surface = test_font.render("0", False, (64,64,64))
score_rect = score_surface.get_rect(midbottom= (750,50))

# importing the snail image
# we use the convert_alpha() to avoid seeing a white backgroun in the image. 

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom= (800, 300))

#creating this variable to be able to animate de snail

snail_x_pos = 800

# importing the player surface

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()

# creating a rectangle to be able to adjust the location of the surfaces.

player_rect = player_surface.get_rect(midbottom= (80, 300))

# creating a variable for gravity

player_gravity = 0





######### Run the game ###########
# we need to keep the program running
# everything need to run inside the while loop

while True:
    # we need code to be able to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # another way of creating interactivy with the keyboard
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                 player_gravity = - 20
    
        # if event.type == pygame.KEYUP:
        #     # check a specific key
        #     if event.key == pygame.K_SPACE:
        #         print("key up")
        
        # implementing a jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = - 20
            
    
    # displaying the surface
    
    screen.blit(sky_surface ,(0,0))
    screen.blit(ground_surface ,(0,300))
    
    # displaying the snail and animate it.
    
    if snail_rect.left >= -100:
        snail_rect.left -= 4
    else:
        snail_rect.left = 800
        
    screen.blit(snail_surface, (snail_rect))
    
    # increasing the gravity 
    player_gravity += 1
    
    
    #applying gravity to the player
    
    player_rect.y += player_gravity
    
    # creating a floor
    
    if player_rect.bottom >=300: 
        player_rect.bottom = 300
        
    
    # displaying the player and animate it
    
    # if player_rect.left <= 900:
    #     player_rect.left += 4
    # else:
    #     player_rect.left = -50
    
    screen.blit(player_surface,(player_rect))
    
    
    # # adding interactivity with the keyboard
    
    # keys = pygame.key.get_pressed()
    
    # # grabbing the space bar
    
    # if keys[pygame.K_SPACE]:
    #     print("jump")
    
    # adding colision
    # .colliderect will return a true if there is a collision 
    # between surfaces
    
    if player_rect.colliderect(snail_rect):
        print("Collision")
    
    # adding colision with the mouse
    # .collidepoint
    
    # getting the mouse position
    
    mouse_position = pygame.mouse.get_pos()
    
    # using the position to detect colition between a 
    
    if player_rect.collidepoint((mouse_position)):
        print("Collision")
    
    
    # adding a rectagle with color around the text
    
   
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10,20)
    
    # drawing a line
    
    #pygame.draw.line(screen, "Red", (0,0), (800,400))
    
    # drawing a line with the mouse 
    
    #pygame.draw.line(screen, "Yellow", (0,0), (pygame.mouse.get_pos()))
    
   
    
    # displaying the text
    screen.blit(score_surface,(score_rect))
    
    # this need to be always in the lop.
    pygame.display.update()
    
    # here we are saying that the while lop should not run more than 60 times 
    # per second
    clock.tick(60)
    
    