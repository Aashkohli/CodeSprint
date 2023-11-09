import pygame
import random 
pygame.init()
pygame.font.Font

display = pygame.display.set_mode((1300,800))
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
    
    #draw cyan border
    
   



xScale = 120
yScale = 200

def setXScale(n):
    
    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(n*(i)), False, (0, 255, 0))
        display.blit(text_surface, (100*(i)+50-text_surface.get_width()/2,640))
        
    
        
        
   
def setYScale(n):
    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(n*11-n*(i+1)), False, (0, 255, 0))
        display.blit(text_surface, (30-text_surface.get_width()/2 , 60*(i)+30-text_surface.get_height()/2))
        
def draw_triangle(arr):
    for i in range(len(arr)):
        if(i<len(arr)-1):
            pygame.draw.line(display, (0, 255, 255), (arr[i].x,arr[i].y), (arr[i+1].x,arr[i+1].y), 1)
            
    if(len(arr)>0):
        pygame.draw.line(display, (0, 255, 255), (arr[len(arr)-1].x,arr[len(arr)-1].y), (arr[0].x,arr[0].y), 1)

#solve triangle, should give you data about triangle you plotted or it should draw the given triangle from the inputted side lengths and provide data
#def solve():
    
#length: textboxes

class Textbox:
    
    def __init__(self, startingText, font, font_color, rect, rect_color_active, rect_color_off):
        self.text = startingText
        self.startingText = startingText
        self.font = font
        self.font_color = font_color
        self.rect = rect
        self.color = rect_color_off
        self.color_active = rect_color_active
        self.color_off = rect_color_off
        self.isTextboxOn = False
        
    
        
    def draw(self):
        
        pygame.draw.rect(display, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True,(self.font_color))
        display.blit(text_surface,(self.rect.x+5 ,self.rect.y+5))
        self.rect.width = max(100, text_surface.get_width()+10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.isTextboxOn = True
            else:
                self.isTextboxOn = False
        if self.isTextboxOn:
            self.color = self.color_active
        else:
            self.color = self.color_off
        #add or remove from text
        
        if event.type == pygame.KEYDOWN:
            if self.isTextboxOn:
                
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[0:len(self.text)-1]
                elif len(self.text)<13:
                    if event.unicode.isdigit():
                        self.text += event.unicode
                if len(self.text) < len(self.startingText):
                    self.text  = 'Length: '
                
                
              
                   
                    
                
                    
        
        
                    
            
        
   
        
        




font = pygame.font.Font(None, 40)
text_input = "Length: " 
text_rect = pygame.Rect(50, 680, 200, 40)
rect_color_active = 0, 255, 255
rect_color_off = 0, 255, 0
rect_color = rect_color_off
isTextboxOn = False


#solveTriangleBox

font = pygame.font.Font(None, 50)
solve_text = "Solve"
solve_rect = pygame.Rect(1140, 10, 120, 45)
solve_rect_color = (255, 0, 0)
solve_text_color = (0, 255, 0)


box = Textbox("Length: ", pygame.font.Font(None, 40), (255, 255, 255), pygame.Rect(50, 740, 200, 40), (0, 255, 255), (0, 255, 0))
while True: 
    display.fill("black")
    
    for point in trianglePoints:
    
        pygame.draw.rect(display,"purple",point)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
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
        
        box.draw()     
        #textboxes
        
        #set color
        '''
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
        '''
        #solve text hover effect
        mouse_pos = pygame.mouse.get_pos()
        if solve_rect.collidepoint(mouse_pos):
            solve_text_color = 0, 255, 255
        else:
            solve_text_color = (0, 255, 0)
    
            
        
          
                
        


            
                   
                

    
    clock.tick(FPS)
    #code below
    draw_triangle(trianglePoints)
    drawGraph()
    setXScale(xScale)
    setYScale(yScale)
    
    
    
    
    #adding textbook to screen
    '''
    pygame.draw.rect(display, rect_color, text_rect, 2)
    text_surface = font.render(text_input, True,(255, 255, 255))
    display.blit(text_surface,(text_rect.x+5 ,text_rect.y+5))
    text_rect.width = max(100, text_surface.get_width()+10)
    '''
    
    #solve rect
    pygame.draw.rect(display, solve_rect_color, solve_rect, 2)
    solve_surface = font.render(solve_text, True, solve_text_color)
    display.blit( solve_surface,(solve_rect.x+14, solve_rect.y+5))
    
    
    pygame.display.update()
