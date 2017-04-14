# Snake Game!
# by root

# game imports
import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initalising errors, exiting...". format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame succesfully initialised!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colours
red = pygame.Color(255, 0, 0)# game over
green = pygame.Color(0, 255, 0)# snake
#blue = pygame.Color(0, 0, 255)#
black = pygame.Color(0, 0, 0)# score
white = pygame.Color(255, 255, 255)# backgroynd
brown = pygame.Color(165, 42, 42)# food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()#pygame exit
    sys.exit()#console exit
    
# Logic for the game.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d')
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a')
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w')
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s')
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            