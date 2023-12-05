import pygame,math,Textbox,Point,Button

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
display = pygame.display.set_mode((1300, 800))
button_image = pygame.image.load("images/blue_square.jpg").convert_alpha()
switch_triangle = Button.Button(0,0,button_image,1)
switch_graphing = Button.Button(display.get_width()/2-button_image.get_width()/2,display.get_height()/2-button_image.get_height()/2,button_image,0.75)
switch_polygon = Button.Button(display.get_width()-button_image.get_width(),display.get_height()-button_image.get_height(),button_image,0.5)
background_color = (0, 0, 0)
display.fill(background_color)
pygame.display.set_caption("Math Calculator") 
clock = pygame.time.Clock()
drag = None
points = [
    Point.Point(50, 630, "A"),
    Point.Point(500, 630, "B"),
    Point.Point(250, 200, "C")
] 
mousex = 0
mousey = 0

mode = "main_menu"

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
    
           
   
triangleLengths = ["", "", ""]
triangleAngles = ["", "", ""]
xCoords = ["", "", ""]
yCoords = ["", "", ""]




xScale = 120
yScale = 200


#is not fully working, can only take in n as 100
#n is the interval between each y axis
def setXScale(n):

    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(n*(i)), False, (0, 255, 0))
        display.blit(text_surface, (100*(i)+50-text_surface.get_width()/2,640))

def setYScale(n):
    for i in range(0, 11):
        my_font = pygame.font.SysFont('Arial', 15)
        text_surface = my_font.render("" + str(660-n*(i+1)), False, (0, 255, 0))
        display.blit(text_surface, (30-text_surface.get_width()/2 , 60*(i)+30-text_surface.get_height()/2))

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
        points[0].x = xCoords[0]
        points[1].x = xCoords[1]
        points[2].x = xCoords[2]
        points[0].y = yCoords[0]
        points[1].y = yCoords[1]
        points[2].y = yCoords[2]
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
   
    
def updateTriangleImage():
    pygame.draw.line(display,pygame.Color("purple"),[points[0].x,points[0].y],[points[1].x,points[1].y])
    pygame.draw.line(display,pygame.Color("purple"),[points[1].x,points[1].y],[points[2].x,points[2].y])
    pygame.draw.line(display,pygame.Color("purple"),[points[2].x,points[2].y],[points[0].x,points[0].y]) 
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
        points[0].x = xCoords[0]
        points[1].x = xCoords[1]
        points[2].x = xCoords[2]
        points[0].y = yCoords[0]
        points[1].y = yCoords[1]
        points[2].y = yCoords[2]
   

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
bottom_solve_rect = pygame.Rect(450, 680, 120, 45)
bottom_solve_rect_color = (255, 0, 0)
bottom_solve_text_color = (0, 255, 0)
#bottomclearBox

font = pygame.font.Font(None, 50)
bottom_clear_text = "Clear"
bottom_clear_rect = pygame.Rect(450, 730, 120, 45)
bottom_clear_rect_color = (255, 0, 0)
bottom_clear_text_color = (0, 255, 0)




def poly_sort(points):
  # Get center of mass
  if(len(points)!=0):
    center = [sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)]

  # Sort by polar angle, centered at the center of mass
  points.sort(key=lambda p: (math.atan2(p[1] - center[1], p[0] - center[0]) + 2 * math.pi) % (2 * math.pi))

sideLengthATextBox = Textbox.Textbox("Length A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 675, 120, 30), (0, 255, 255), (0, 255, 0), 2)
sideLengthBTextBox= Textbox.Textbox("Length B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 710, 120, 30), (0, 255, 255), (0, 255, 0), 2)
sideLengthCTextBox= Textbox.Textbox("Length C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(150, 745, 120, 30), (0, 255, 255), (0, 255, 0), 2)

angleATextBox = Textbox.Textbox("Angle A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(300, 675, 120, 30), (0, 255, 255), (0, 255, 0 ), 3)
angleBTextBox= Textbox.Textbox("Angle B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(300, 710, 120, 30), (0, 255, 255), (0, 255, 0), 3)
angleCTextBox= Textbox.Textbox("Angle C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(300, 745, 120, 30), (0, 255, 255), (0, 255, 0), 3)
x_pointA = Textbox.Textbox("x Point A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(590, 690, 120, 28), (0, 255, 255), (0, 255, 0), 3)
y_pointA = Textbox.Textbox("y Point A: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(590, 730, 120, 28), (0, 255, 255), (0, 255, 0), 3)
x_pointB = Textbox.Textbox("x Point B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(760, 690, 120, 28), (0, 255, 255), (0, 255, 0), 3)
y_pointB = Textbox.Textbox("y Point B: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(760, 730, 120, 28), (0, 255, 255), (0, 255, 0), 3)
x_pointC = Textbox.Textbox("x Point C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(930, 690, 120, 28), (0, 255, 255), (0, 255, 0), 3)
y_pointC = Textbox.Textbox("y Point C: ", pygame.font.Font(None, 30), (255, 255, 255), pygame.Rect(930, 730, 120, 28), (0, 255, 255), (0, 255, 0), 3)
#stats
def clearText():
    pointA_text.text = pointA_text.startingText
    pointB_text.text = pointB_text.startingText
    pointC_text.text = pointC_text.startingText
    sideLengthA_text.text = sideLengthA_text.startingText
    sideLengthB_text.text = sideLengthB_text.startingText
    sideLengthC_text.text = sideLengthC_text.startingText
    angleA_text.text = angleA_text.startingText
    angleB_text.text = angleB_text.startingText
    angleC_text.text = pointC_text.startingText
    perimeter_text.text = perimeter_text.startingText
    semiperimeter_text.text = semiperimeter_text.startingText
    heightA_text.text = heightA_text.startingText
    heightB_text.text = heightB_text.startingText
    heightC_text.text = heightC_text.startingText
    angleClassification_text.text = angleClassification_text.startingText
    triangleClassification_text.text = angleClassification_text.startingText
    inradius_text.text = inradius_text.startingText
    incenter_text.text = incenter_text.startingText
    circumradius_text.text = circumradius_text.startingText
    circumcenter_text.text = circumcenter_text.startingText
    medianA_text.text = medianA_text.startingText
    medianB_text.text = medianB_text.startingText
    medianC_text.text = medianC_text.startingText
    
base = 40
counter = 30
pointA_text = Textbox.Textbox("Point A:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 120, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
pointB_text = Textbox.Textbox("Point B:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 150, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
pointC_text = Textbox.Textbox("Point C:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
sideLengthA_text = Textbox.Textbox("Side Length A:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 120, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
sideLengthB_text = Textbox.Textbox("Side Length B:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 150, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
sideLengthC_text = Textbox.Textbox("Side Length C:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
angleA_text = Textbox.Textbox("Angle A:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 120, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
angleB_text = Textbox.Textbox("Angle B:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 150, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
angleC_text = Textbox.Textbox("Angle C:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
perimeter_text = Textbox.Textbox("Perimeter:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
semiperimeter_text = Textbox.Textbox("Semiperimeter:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
heightA_text = Textbox.Textbox("Height A:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 120, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
heightB_text = Textbox.Textbox("Height B:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 150, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
heightC_text = Textbox.Textbox("Height C:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
angleClassification_text = Textbox.Textbox("Angle Classification:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
triangleClassification_text = Textbox.Textbox("Triangle Classification:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
inradius_text = Textbox.Textbox("Inradius:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
incenter_text = Textbox.Textbox("Incenter:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
circumradius_text = Textbox.Textbox("Circumradius:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
circumcenter_text = Textbox.Textbox("Circumcenter:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
medianA_text = Textbox.Textbox("Median A:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
medianB_text = Textbox.Textbox("Median B:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
medianC_text = Textbox.Textbox("Median C:  ", pygame.font.Font(None, 18), (255, 255, 255), pygame.Rect(1120, base, 180, 20), (0, 255, 255), (0, 255, 255), 3, False)
base += counter
"""


~~~ GAME LOOP


"""
while True: 
    if (mode == "main_menu"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        display.fill("black")
        switch_graphing.draw(display)
        switch_polygon.draw(display)
        switch_triangle.draw(display)
        if(switch_triangle.is_clicked()):
            mode = "triangle_calculator"
        elif(switch_graphing.is_clicked()):
            mode = "graphing_calculator"
        elif(switch_polygon.is_clicked()):
            mode = "polygon_calculator"
        
    elif (mode == "triangle_calculator"):
        display.fill("black")
        # if len(points) > 1:
        #     pygame.draw.polygon(display, (0,255,255), points, 2)
        for point in points:
            point.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mode = "main_menu"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                # if (x <= 1100 and y<630):
                    
                    # match = next(((i, p) for i, p in enumerate(points) if abs(p[0] - x) + abs(p[1] - y) <= 6), None)
                    # if match:
                    #     index, _ = match
                    #     points.pop(index)
                    #     poly_sort(points)
                    # elif (len(points) < 5):
                    #     points.append((x, y))
                    #     poly_sort(points)
                pygame.draw.line(display,pygame.Color("purple"),[points[0].x,points[0].y],[points[1].x,points[1].y])
                pygame.draw.line(display,pygame.Color("purple"),[points[1].x,points[1].y],[points[2].x,points[2].y])
                pygame.draw.line(display,pygame.Color("purple"),[points[2].x,points[2].y],[points[0].x,points[0].y]) 
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
                    clearText()
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

        #code below
        drawGraph()
        setXScale(100)
        setYScale(60)
        updateTriangleImage()
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

        pos = pygame.mouse.get_pos()
        if bottom_solve_rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1:
        
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
       
        sideLengthA_text.draw(display)
        sideLengthB_text.draw(display)
        sideLengthC_text.draw(display)
        pointA_text.draw(display)
        pointB_text.draw(display)
        pointC_text.draw(display)
        angleA_text.draw(display)
        angleB_text.draw(display)
        angleC_text.draw(display)
        perimeter_text.draw(display)
        semiperimeter_text.draw(display)
        heightA_text.draw(display)
        heightB_text.draw(display)
        heightC_text.draw(display)
        angleClassification_text.draw(display)
        triangleClassification_text.draw(display)
        inradius_text.draw(display)
        incenter_text.draw(display)
        circumradius_text.draw(display)
        circumcenter_text.draw(display)
        medianA_text.draw(display)
        medianB_text.draw(display)
        medianC_text.draw(display)
        
    elif (mode == "polygon_calculator"):
        display.fill(pygame.Color("green"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mode = "main_menu"
            

    
    elif(mode == "graphing_calculator"):
        display.fill(pygame.Color("purple"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mode = "main_menu"
    pygame.display.flip()
    clock.tick(FPS)
