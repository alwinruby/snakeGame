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
time.sleep(5)
