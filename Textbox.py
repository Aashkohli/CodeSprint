import pygame

class Textbox():
    
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
