# Snake Game!
# by root

# game imports
import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initalising errors, exiting...". format(check_error[1]))
    sys.exit(-1)
else:
    print("(+) PyGame succesfully initialised!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colours
red = pygame.Color(255, 0, 0)# game over
green = pygame.Color(0, 255, 0)# snake
blue = pygame.Color(0, 0, 255)#
black = pygame.Color(0, 0, 0)# score
white = pygame.Color(255, 255, 255)# backgroynd
brown = pygame.Color(165, 42, 42)# food