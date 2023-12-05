import pygame
import math

class Point():
    
    def __init__(self, xcoord, ycoord, label,color = pygame.Color("purple")):
        self.x = xcoord
        self.y = ycoord
        self.name = label
        self.color = color
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y  
    
    def set_x(self, x):
        self.x = x

    def set_y(self,y):
        self.y = y

    def distance(self,point):
        return math.sqrt(abs(self.x-point.x)*abs(self.x-point.x) + abs(self.y-point.y)*abs(self.y-point.y))
    
    def to_string(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def get_label(self):
        return self.label
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def draw(self,display):
        #circ = pygame.Rect(self.x,self.y,1,1)
        pygame.draw.circle(display,self.color,(self.x,self.y),3,0)