import pygame

pygame.init()

display = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

FPS = 30
def game():
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()

