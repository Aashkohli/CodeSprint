import pygame
import random 
import math


WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
display = pygame.display.set_mode((1300, 800))
background_color = (0, 0, 0)
display.fill(background_color)
pygame.display.set_caption("Math Calculator") 
clock = pygame.time.Clock()
drag = None
points = [] 
mousex = 0
mousey = 0

mode = 1

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
    
class Point:
    
    def __init__(self, xcoord, ycoord, label):
        self.x = xcoord
        self.y = ycoord
        self.name = label
        
    def getStringPoint(self):
        
        return str(self.x) + ", " + str(self.y)
            
   
triangleLengths = ["", "", ""]
triangleAngles = ["", "", ""]
xCoords = ["", "", ""]
yCoords = ["", "", ""]

PointA = Point(0, 0, "A")
PointB = Point(0, 0, "B")
PointC = Point(0, 0, "C")


xScale = 120
yScale = 200


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


#solve triangle, should give you data about triangle you plotted or it should draw the given triangle from the inputted side lengths and provide data
#def solve():
    


def solveLengths():
    #use to solve triangle with lengths later
    
    updateTriangleInfo()
    

 
    
    

def solvePoints():
    #use to solve triangle with points later
    updateTriangleInfo()
    if (isPointsInputValid()):
        
        PointA.x = xCoords[0]
        PointB.x = xCoords[1]
        PointC.x = xCoords[2]
        PointA.y = yCoords[0]
        PointB.y = yCoords[1]
        PointC.y = yCoords[2]
    else:
        print("Enter a value for each x and y.")
        
   

def clearLengths():
    
    #clear graph and lengths input
    sideLengthATextBox.text = sideLengthATextBox.startingText
    sideLengthBTextBox.text = sideLengthBTextBox.startingText
    sideLengthCTextBox.text = sideLengthCTextBox.startingText
    angleATextBox.text = angleATextBox.startingText
    angleBTextBox.text = angleBTextBox.startingText
    angleCTextBox.text = angleCTextBox.startingText
    
    triangleLengths[0] = ""
    triangleLengths[1] = ""
    triangleLengths[2] = ""
    triangleAngles[0] = ""
    triangleAngles[1] = ""
    triangleAngles[2] = ""

def clearPoints():
    #clear graph and points input
    x_pointA.text = x_pointA.startingText
    y_pointA.text = y_pointA.startingText
    x_pointB.text = x_pointB.startingText
    y_pointB.text = y_pointB.startingText
    x_pointC.text = x_pointC.startingText
    y_pointC.text = y_pointC.startingText
 
    
    xCoords[0] = ""
    xCoords[1] = ""
    xCoords[2] = ""
    yCoords[0] = ""
    yCoords[1] = ""
    yCoords[2] = ""
   
    
 
def isPointsInputValid():
    
    if (xCoords[0] == "" or xCoords[1] == "" or xCoords[2] == "" or yCoords[0] == "" or yCoords[1] == "" or yCoords[2] == ""):
        return False
    else:
        return True
   
def updateTriangleInfo():
    if (len(sideLengthATextBox.text) >= len(sideLengthATextBox.startingText)):
        triangleLengths[0] = (sideLengthATextBox.text)[len(sideLengthATextBox.startingText):]
        
    if (len(sideLengthBTextBox.text) >= len(sideLengthBTextBox.startingText)):
        triangleLengths[1] = (sideLengthBTextBox.text)[len(sideLengthBTextBox.startingText):]
        
    if (len(sideLengthCTextBox.text) >= len(sideLengthCTextBox.startingText)):
        triangleLengths[2] =(sideLengthCTextBox.text)[len(sideLengthCTextBox.startingText):]
        
    if (len(angleATextBox.text) >= len(angleATextBox.startingText)):
        triangleAngles[0] =  (angleATextBox.text)[len(angleATextBox.startingText):]
        
    if (len(angleBTextBox.text) >= len(angleBTextBox.startingText)):
        triangleAngles[1] =  (angleBTextBox.text)[len(angleBTextBox.startingText):]
        
    if (len(angleCTextBox.text) >= len(angleCTextBox.startingText)):
        triangleAngles[2] =  (angleCTextBox.text)[len(angleCTextBox.startingText):]
    
    if (len(x_pointA.text) >= len(x_pointA.startingText)):
        xCoords[0] =  (x_pointA.text)[len(x_pointA.startingText):]
    
    if (len(x_pointB.text) >= len(x_pointB.startingText)):
        xCoords[1] =  (x_pointB.text)[len(x_pointB.startingText):]
        
    if (len(x_pointC.text) >= len(x_pointC.startingText)):
        xCoords[2] =  (x_pointC.text)[len(x_pointC.startingText):]
        
    if (len(y_pointA.text) >= len(y_pointA.startingText)):
        yCoords[0] =  (y_pointA.text)[len(y_pointA.startingText):]
        
    if (len(y_pointB.text) >= len(y_pointB.startingText)):
        yCoords[1] =  (y_pointB.text)[len(y_pointB.startingText):]
        
    if (len(y_pointC.text) >= len(y_pointC.startingText)):
        yCoords[2] =  (y_pointC.text)[len(y_pointC.startingText):]
   
    
    if (isPointsInputValid()):
        PointA.x = xCoords[0]
        PointB.x = xCoords[1]
        PointC.x = xCoords[2]
        PointA.y = yCoords[0]
        PointB.y = yCoords[1]
        PointC.y = yCoords[2]
   

        
class Textbox:
    
    def __init__(self, startingText, font, font_color, rect, rect_color_active, rect_color_off, digitsMax):
        self.text = startingText
        self.startingText = startingText
        self.font = font
        self.font_color = font_color
        self.rect = rect
        self.color = rect_color_off
        self.color_active = rect_color_active
        self.color_off = rect_color_off
        self.isTextboxOn = False
        self.max = digitsMax
        
    
    
    def handleEvent(self, event):
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
                elif len(self.text)<(len(self.startingText)+self.max):
                    if event.unicode.isdigit():
                        self.text += event.unicode
                if len(self.text) < len(self.startingText):
                    self.text  = self.startingText
                    
    def draw(self, display):
        
        pygame.draw.rect(display, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True,(self.font_color))
        display.blit(text_surface,(self.rect.x+5 ,self.rect.y+5))
        self.rect.width = max(100, text_surface.get_width()+10)
        
    def getText(self):
        return self.text
    
    def setText(self, input):
        self.text = input
        
    
    
def squared_polar(point, center):
  return [
      math.atan2(point[1] - center[1], point[0] - center[0]),
      (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2  # Square of distance
  ]
  
#topsolveTriangleBox

font = pygame.font.Font(None, 50)
top_solve_text = "Solve"
top_solve_rect = pygame.Rect(10, 680, 120, 45)
top_solve_rect_color = (255, 0, 0)
top_solve_text_color = (0, 255, 0)
#topclearBox

font = pygame.font.Font(None, 50)
top_clear_text = "Clear"
top_clear_rect = pygame.Rect(10, 730, 120, 45)
top_clear_rect_color = (255, 0, 0)
top_clear_text_color = (0, 255, 0)

#bottomsolveTriangleBox

font = pygame.font.Font(None, 50)
bottom_solve_text = "Solve"
bottom_solve_rect = pygame.Rect(480, 680, 120, 45)
bottom_solve_rect_color = (255, 0, 0)
bottom_solve_text_color = (0, 255, 0)
#bottomclearBox

font = pygame.font.Font(None, 50)
bottom_clear_text = "Clear"
bottom_clear_rect = pygame.Rect(480, 730, 120, 45)
bottom_clear_rect_color = (255, 0, 0)
bottom_clear_text_color = (0, 255, 0)




def poly_sort(points):
  # Get center of mass
  if(len(points)!=0):
    center = [sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)]

  # Sort by polar angle, centered at the center of mass
  points.sort(key=lambda p: (math.atan2(p[1] - center[1], p[0] - center[0]) + 2 * math.pi) % (2 * math.pi))

sideLengthATextBox = Textbox("Length A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 675, 120, 30), (0, 255, 255), (0, 255, 0), 2)
sideLengthBTextBox= Textbox("Length B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 710, 120, 30), (0, 255, 255), (0, 255, 0), 2)
sideLengthCTextBox= Textbox("Length C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 745, 120, 30), (0, 255, 255), (0, 255, 0), 2)

angleATextBox = Textbox("Angle A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(320, 675, 120, 30), (0, 255, 255), (0, 255, 0 ), 3)
angleBTextBox= Textbox("Angle B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(320, 710, 120, 30), (0, 255, 255), (0, 255, 0), 3)
angleCTextBox= Textbox("Angle C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(320, 745, 120, 30), (0, 255, 255), (0, 255, 0), 3)

x_pointA = Textbox("x Point A: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(615, 690, 120, 34), (0, 255, 255), (0, 255, 0), 2)
y_pointA = Textbox("y Point A: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(615, 730, 120, 34), (0, 255, 255), (0, 255, 0), 2)

x_pointB = Textbox("x Point B: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(780, 690, 120, 34), (0, 255, 255), (0, 255, 0), 2)
y_pointB = Textbox("y Point B: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(780, 730, 120, 34), (0, 255, 255), (0, 255, 0), 2)

x_pointC = Textbox("x Point C: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(945, 690, 120, 34), (0, 255, 255), (0, 255, 0), 2)
y_pointC = Textbox("y Point C: ", pygame.font.Font(None, 34), (255, 255, 255), pygame.Rect(945, 730, 120, 34), (0, 255, 255), (0, 255, 0), 2)

while True: 
    if (mode == 1):
        display.fill("black")
        if len(points) > 1:
            pygame.draw.polygon(display, (0,255,255), points, 2)
        for point in points:
            pygame.draw.circle(display, (0,255,255), point, 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if (x <= 1100 and y<630):
                    
                    match = next(((i, p) for i, p in enumerate(points) if abs(p[0] - x) + abs(p[1] - y) <= 6), None)
                    if match:
                        index, _ = match
                        points.pop(index)
                        poly_sort(points)
                    elif (len(points) < 5):
                        points.append((x, y))
                        poly_sort(points)

            sideLengthATextBox.handleEvent(event) 
            sideLengthBTextBox.handleEvent(event)       
            sideLengthCTextBox.handleEvent(event) 
            angleATextBox.handleEvent(event) 
            angleBTextBox.handleEvent(event) 
            angleCTextBox.handleEvent(event) 
            x_pointA.handleEvent(event)
            y_pointA.handleEvent(event)
            x_pointB.handleEvent(event)
            y_pointB.handleEvent(event)
            x_pointC.handleEvent(event)
            y_pointC.handleEvent(event)

                        
            #solve text hover and click effect
            mouse_pos = pygame.mouse.get_pos()
            
                
            if top_solve_rect.collidepoint(mouse_pos):
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    top_solve_text_color = (255, 0, 255)
                    solveLengths()
                else:
                    top_solve_text_color = 0, 255, 255
            else:
                top_solve_text_color = (0, 255, 0)
                
            #clear text hover effect
            if top_clear_rect.collidepoint(mouse_pos):
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    top_clear_text_color = (255, 0, 255)
                    clearLengths()
                else:
                    top_clear_rect_clear_text_color = 0, 255, 255
            else:
                top_clear_text_color = (0, 255, 0)
            #solve
            if bottom_solve_rect.collidepoint(mouse_pos):
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    bottom_solve_text_color = (255, 0, 255)
                    solvePoints()
                else:
                    bottom_solve_text_color = 0, 255, 255
            else:
                bottom_solve_text_color = (0, 255, 0)
                
            #clear text hover effect
            if bottom_clear_rect.collidepoint(mouse_pos):
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    bottom_clear_text_color = (255, 0, 255)
                    clearPoints()
                else:
                    bottom_clear_text_color = 0, 255, 255
            else:
                bottom_clear_text_color = (0, 255, 0)
        
        clock.tick(FPS)

        #code below
        drawGraph()
        setXScale(100)
        setYScale(60)
        
        #top solve rect
        pygame.draw.rect(display, top_solve_rect_color, top_solve_rect, 2)
        top_solve_surface = font.render(top_solve_text, True, top_solve_text_color)
        display.blit( top_solve_surface,(top_solve_rect.x+14, top_solve_rect.y+5))

        #top clear rect
        pygame.draw.rect(display, top_clear_rect_color, top_clear_rect, 2)
        top_clear_surface = font.render(top_clear_text, True, top_clear_text_color)
        display.blit( top_clear_surface,(top_clear_rect.x+14, top_clear_rect.y+5))
        
        #solve rect
        pygame.draw.rect(display, bottom_solve_rect_color, bottom_solve_rect, 2)
        bottom_solve_surface = font.render(bottom_solve_text, True, bottom_solve_text_color)
        display.blit( bottom_solve_surface,(bottom_solve_rect.x+14, bottom_solve_rect.y+5))

        #clear rect
        pygame.draw.rect(display, bottom_clear_rect_color, bottom_clear_rect, 2)
        bottom_clear_surface = font.render(bottom_clear_text, True, bottom_clear_text_color)
        display.blit( bottom_clear_surface,(bottom_clear_rect.x+14, bottom_clear_rect.y+5))

        updateTriangleInfo()

        #adding textbook to screen
        
            
        sideLengthATextBox.draw(display) 
        sideLengthBTextBox.draw(display)
        sideLengthCTextBox.draw(display)
        angleATextBox.draw(display) 
        angleBTextBox.draw(display)
        angleCTextBox.draw(display)
        x_pointA.draw(display)
        y_pointA.draw(display)
        x_pointB.draw(display)
        y_pointB.draw(display)
        x_pointC.draw(display)
        y_pointC.draw(display)
       
    elif (mode == 2):
        display.fill("black")
        if len(points) > 1:
            pygame.draw.polygon(display, (0,255,255), points, 2)
        for point in points:
            pygame.draw.circle(display, (0,255,255), point, 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
    pygame.display.flip()
    clock.tick(FPS)