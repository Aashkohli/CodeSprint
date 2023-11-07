import pygame

pygame.init()

display = pygame.display.set_mode((1000,600))
background_color = (255, 255, 255)
display.fill(background_color)
pygame.display.set_caption("Math Calculator") 
clock = pygame.time.Clock()

FPS = 30
def game():
    #setup
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)
        #code below
        drawGraph()
    

def drawGraph():
    #top most line is at y = 30, 10 lines from y 0 to 600, gets incremented by 60
    #left most line is at x = 50, 10 lines from x 0 to 1000, gets incremented by 100
    # draw x lines
    
    for i in range(0, 10):
        if (i == 0):
            pygame.draw.line(display, (0, 0, 0), (i*100+50, 0), (i*100+50, 600), 3)
        else:
            pygame.draw.line(display, (0, 0, 0), (i*100+50, 0), (i*100+50, 600), 1)
        
    # drawa y lines
    
    for i in range(0, 10):
        if (i == 9):
            pygame.draw.line(display, (0, 0, 0), (0, i*60+30), (1000, i*60+30), 3)
        else:
            pygame.draw.line(display, (0, 0, 0), (0, i*60+30), (1000 ,i*60+30), 1)
    

game()


pygame.quit()

