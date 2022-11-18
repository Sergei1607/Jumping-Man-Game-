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
from random import randint


# =============================================================================
# Functions
# =============================================================================

def display_score():

    #Display the score
    
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):

    #Movement of the obstacle
    
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4 
            
    # deciding with surface to display
            
            if obstacle_rect.bottom == 300:   
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)
            
    # to delete snails that are outside the window
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else:
        return []
    
def collisions(player,obstacles):
    
    # handle collision 
    
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    
    #play walking animation when the player is on the floor or the jump animation
    
    global player_surface, player_index
    
    if player_rect.bottom < 300:
        player_surface = player_jump
        
    else:
        player_index += 0.1
        if player_index >= len(player_walk_list):
            player_index = 0
        player_surface = player_walk_list[int(player_index)]
        
    
    

# =============================================================================
# Must have
# =============================================================================

# iniciate pygame

pygame.init()

# Window for the game

screen = pygame.display.set_mode((800, 400))

# Name of the window

pygame.display.set_caption("Pixel Runner")

# clock object for controling the frame rate

clock = pygame.time.Clock()

# =============================================================================
# Fonts for text
# =============================================================================

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# =============================================================================
# Backgroud Surfaces
# =============================================================================

# sky

sky_surface = pygame.image.load("graphics/Sky.png").convert()

# groud

ground_surface = pygame.image.load("graphics/ground.png").convert()

# =============================================================================
# Player Surfaces
# =============================================================================

# player

player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()

player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()

player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_jump_rect = player_jump.get_rect(midbottom= (80, 300))

# list of player images

player_walk_list = [player_walk_1, player_walk_2]

# player index

player_index = 0 

# choosing the image

player_surface = player_walk_list[player_index]

# creating the rectangle

player_rect = player_surface.get_rect(midbottom= (80, 300))


# player for end screen

player_stand_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()

# scaling the image 

player_stand_surface = pygame.transform.scale2x(player_stand_surface)

# another way of scaling

# player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 2)

player_stand_rect_scaled = player_stand_surface.get_rect(center= (400, 200))

# =============================================================================
# Text Surfaces
# =============================================================================

# text for game title

game_title_surface = test_font.render("Pixel Runner", False, (111,196,169))
game_title_rect = game_title_surface.get_rect(center = (400,50))

# text for instructions

instructions_surface = test_font.render("Press Start to Play", False, (111,196,169))
instructions_rect = instructions_surface.get_rect(center = (400,350))

# =============================================================================
# Enemies
# =============================================================================

# snail

snail_frame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()

snail_frames_list = [snail_frame1, snail_frame2]

snail_frame_index = 0

snail_surface = snail_frames_list[snail_frame_index]

# fly

fly_frame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()

fly_frames_list = [fly_frame1, fly_frame2]

fly_frame_index = 0

fly_surface = fly_frames_list[fly_frame_index]

## list of obstacles

obstacle_rect_list = []

# =============================================================================
# Variables
# =============================================================================

# animating the snail

snail_x_pos = 800

# gravity

player_gravity = 0

# game state

game_active = False

# time

start_time = 0

# score

score = 0

# =============================================================================
# Timer
# =============================================================================

obstacle_timer = pygame.USEREVENT + 1

# triggering the timer

pygame.time.set_timer(obstacle_timer, 1500)

# snail animation timer

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

# fly animation timer

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


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
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
            # jumping when we click the player
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = - 20

     # implementing a jump with space bar

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = - 20
                    
     # spawning enemies               
            if event.type == obstacle_timer:
                #setting a random value to decide if we spawn a fly or a snail
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom= (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom= (randint(900, 1100), 210)))
    
    # animating the snail
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames_list[snail_frame_index]
                
    # animating the fly
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames_list[snail_frame_index]
                
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)
            
# =============================================================================
# Displaying surfaces Main Screen
# =============================================================================

    if game_active:
    # sky
    
        screen.blit(sky_surface ,(0,0))
    
    # ground
    
        screen.blit(ground_surface ,(0,300))
    
    # player
        player_animation()
        screen.blit(player_surface,(player_rect))
        
    
# =============================================================================
# Drawings and text
# =============================================================================
    
    # adding score
    
        score = display_score()
    
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
    
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    
# =============================================================================
# Collisions
# =============================================================================
            
        game_active = collisions(player_rect, obstacle_rect_list)
                   
# =============================================================================
# Displaying surfaces End game Screen
# =============================================================================
            
    else:
        screen.fill((64,129,162))
        
    # displaying the player
    
        screen.blit(player_stand_surface, (player_stand_rect_scaled))
    
    # displaying the title
    
        screen.blit(game_title_surface, game_title_rect)
        
   
    # displaying the score
    
        score_message = test_font.render(f"Your Score: {score}", False, (111,196,169))
        score_mesagge_rect = score_message.get_rect(center = (400, 340))
        
        if score == 0:
             # displaying the instructions
             screen.blit(instructions_surface, instructions_rect)
        else:
            screen.blit(score_message,(score_mesagge_rect))
        
    # eliminating everything in the obstacle list when the game end
        
        obstacle_rect_list.clear()
        
    # setting the player at the bottom
    
        player_rect.bottom = 300
        player_gravity = 0
    

# =============================================================================
#Technical Stuff
# =============================================================================

    # update the game

    pygame.display.update()

    # setting the frames

    clock.tick(60)
