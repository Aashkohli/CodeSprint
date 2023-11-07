import pygame

pygame.init()

run = True

display = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
FPS = 30
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()