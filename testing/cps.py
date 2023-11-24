import pygame
from pygame.locals import *
pygame.init()
X = 400
Y = 400
FPS = 60
clicks = 0
screen = pygame.display.set_mode((X,Y))
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.display.set_caption('CPS')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
best = 0
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()
start = False
while True:
    screen.fill("purple")
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print(str(best))
            exit()
        if(event.type == pygame.MOUSEBUTTONDOWN):   
            if(pygame.mouse.get_pressed()[0]):
                clicks+=1
                start = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                clicks=0
                start_ticks = pygame.time.get_ticks()
                start = False
    if(start==False):
        start_ticks = pygame.time.get_ticks()
    if(seconds!=0):
        text = font.render("{:.2f}".format(clicks/seconds), True, green, blue)
        if(clicks>3 and clicks/seconds >= best):
            best = clicks/seconds
    screen.blit(text, textRect)
    pygame.display.update()
pygame.quit() 
