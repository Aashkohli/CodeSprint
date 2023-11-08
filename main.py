import pygame
import random 
pygame.init()
pygame.font.Font

display = pygame.display.set_mode((1100,660))
background_color = (0, 0, 0)
display.fill(background_color)
pygame.display.set_caption("Math Calculator") 
clock = pygame.time.Clock()
currentlyDragging = None
trianglePoints = [] 
mousex = 0
mousey = 0
FPS = 30
def drawGraph():
    #top most line is at y = 30, 10 lines from y 0 to 600, gets incremented by 60
    #left most line is at x = 50, 10 lines from x 0 to 1000, gets incremented by 100
    # draw x lines

    for i in range(0, 11):
        if (i == 0):
            pygame.draw.line(display, (255, 255, 255), (i*100+50, 0), (i*100+50, 660), 3)
        else:
            pygame.draw.line(display, (255, 255, 255), (i*100+50, 0), (i*100+50, 660), 1)

    #draw y lines
    for i in range(0, 11):
        if (i == 10):
            pygame.draw.line(display, (255, 255, 255), (0, i*60+30), (1100, i*60+30), 3)
        else:
            pygame.draw.line(display, (255, 255, 255), (0, i*60+30), (1100 ,i*60+30), 1)

#is not fully working, can only take in n as 100
#n is the interval between each y axis
def setXScale(n):
    
    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(n*(i)), False, (0, 255, 0))
        display.blit(text_surface, (n*(i)+50-text_surface.get_width()/2,640))
        
    
        
        
   
def setYScale(n):
    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(660-n*(i+1)), False, (0, 255, 0))
        display.blit(text_surface, (30-text_surface.get_width()/2 , n*(i)+30-text_surface.get_height()/2))
        
def draw_triangle(arr):
    for i in range(len(arr)):
        if(i<len(arr)-1):
            pygame.draw.line(display, (0, 255, 255), (arr[i].x,arr[i].y), (arr[i+1].x,arr[i+1].y), 1)
            
    if(len(arr)>0):
        pygame.draw.line(display, (0, 255, 255), (arr[len(arr)-1].x,arr[len(arr)-1].y), (arr[0].x,arr[0].y), 1)


#textboxes
font = pygame.font.Font(None, 40)
text_input = "Length: " 
text_rect = pygame.Rect(800, 40, 200, 40)
rect_color_active = 0, 242, 255
rect_color_off = 0, 255, 0
rect_color = rect_color_off
isTextboxOn = False

while True: 
    display.fill("black")
    """
    for point in trianglePoints:
    
        pygame.draw.rect(display,"purple",point)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                mousex,mousey = pygame.mouse.get_pos()
                if(len(trianglePoints)<3):
                    point = pygame.Rect(mousex-4,mousey-4,8,8)
                    trianglePoints.append(point)
                else:
                    for index,point in enumerate(trianglePoints):
                        if(point.collidepoint(event.pos)):
                            currentlyDragging = index
        if event.type == pygame.MOUSEBUTTONUP:
            currentlyDragging = None
        if event.type == pygame.MOUSEMOTION:
            if(currentlyDragging != None):
                trianglePoints[currentlyDragging].move_ip(event.rel)
        """
                
        #textboxes
        
        #set color
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(event.pos):
                isTextboxOn = True
            else:
                isTextboxOn = False
        if isTextboxOn:
            rect_color = rect_color_active
        else:
            rect_color = rect_color_off
        #add or remove from text
        
        if event.type == pygame.KEYDOWN:
            if isTextboxOn:
                
                if event.key == pygame.K_BACKSPACE:
                    text_input = text_input[0:len(text_input)-1]
                elif len(text_input)<13:
                    if event.unicode.isdigit():
                        text_input += event.unicode
                if len(text_input) < 8:
                    text_input = 'Length: '
          
                
        


            
                   
                

    
    clock.tick(FPS)
    #code below
    draw_triangle(trianglePoints)
    drawGraph()
    setXScale(100)
    setYScale(60)
    
    #adding textbook to screen
    pygame.draw.rect(display, rect_color, text_rect, 2)
    text_surface = font.render(text_input, True,(255, 255, 255))
    display.blit(text_surface,(text_rect.x+5 ,text_rect.y+5))
    text_rect.width = max(100, text_surface.get_width()+10)
    
    pygame.display.update()
