import pygame

pygame.init()
pygame.font.Font

display = pygame.display.set_mode((1000,600))
background_color = (0, 0, 0)
display.fill(background_color)
pygame.display.set_caption("Math Calculator") 
clock = pygame.time.Clock()

FPS = 30
def drawGraph():
    #top most line is at y = 30, 10 lines from y 0 to 600, gets incremented by 60
    #left most line is at x = 50, 10 lines from x 0 to 1000, gets incremented by 100
    # draw x lines

    for i in range(0, 10):
        if (i == 0):
            pygame.draw.line(display, (255, 255, 255), (i*100+50, 0), (i*100+50, 600), 3)
        else:
            pygame.draw.line(display, (255, 255, 255), (i*100+50, 0), (i*100+50, 600), 1)

    #draw y lines
    for i in range(0, 10):
        if (i == 9):
            pygame.draw.line(display, (255, 255, 255), (0, i*60+30), (1000, i*60+30), 3)
        else:
            pygame.draw.line(display, (255, 255, 255), (0, i*60+30), (1000 ,i*60+30), 1)

#is not fully working, can only take in n as 100
#n is the interval between each y axis
def setXScale(n):
    
    for i in range(0, 10):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(n*(i)), False, (0, 255, 0))
        display.blit(text_surface, (n*(i)+50-text_surface.get_width()/2,580))
        
    
        
        
   
def setYScale(n):
    for i in range(0, 10):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(600-n*(i+1)), False, (0, 255, 0))
        display.blit(text_surface, (30-text_surface.get_width()/2 , n*i+30-text_surface.get_height()/2))
        
    
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(FPS)
    #code below
    drawGraph()
    setXScale(100)
    setYScale(60)

