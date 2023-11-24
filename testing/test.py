



# Example file showing a basic pygame "game loop"
import pygame,math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill("purple")
clock = pygame.time.Clock()
FPS = 30


points = []
global drag
drag = None

def closest_points(point,points):
    minDistance = float('inf')
    if(len(points)==2):
        point1 = points[0]
        point2 = points[1]
    else:
        point1 = 0
        point2 = 0
    for i in range(len(points)):
        if(point!=points[i]):
            if(math.dist(([point.x,point.y]),([points[i].x,points[i].y])) <= minDistance):
                point1 = points[i]
                minDistance = math.dist([point.x,point.y],([points[i].x,points[i].y]))
    minDistance = float('inf')
    for i in range(len(points)):
        if(point!=points[i] and points[i]!=point1):
            if(math.dist(([point.x,point.y]),([points[i].x,points[i].y])) <= minDistance):                
                point2 = points[i]
                minDistance = math.dist(([point.x,point.y]),([points[i].x,points[i].y]))
    return (point1,point2)
    




def draw_triangle(points):
    for point in points:
        point1,point2 = closest_points(point,points)  
        x1,y1 = point1.center
        x2,y2 = point2.center
        pygame.draw.line(screen, (0, 255, 255), (x1,y1), (x2,y2), 1)
   



while True:
    # poll for events
    screen.fill("purple")
    for point in points:
        pygame.draw.rect(screen,"black",point)
        if(len(points)>1):
            draw_triangle(points)
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            mousex,mousey = pygame.mouse.get_pos()
            if(pygame.mouse.get_pressed()[0]):
                point = pygame.Rect(mousex-50,mousey-50,100,100)
                points.append(point)
                pygame.draw.rect(screen,"black",point)
            elif pygame.mouse.get_pressed()[2]:
                for index,point in enumerate(points):
                        if(point.collidepoint(event.pos)):
                            drag = index
        if event.type == pygame.MOUSEBUTTONUP:
            drag = None
        if event.type == pygame.MOUSEMOTION:
            if(drag != None):
                points[drag].move_ip(event.rel)
    pygame.display.update()

    clock.tick(FPS)  

pygame.quit()