import pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400))

texto = ""
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif pygame.key.name(event.key) == 'right':
                texto = "Direita"
            elif pygame.key.name(event.key) == 'left':
                texto = "Esquerda"
            elif pygame.key.name(event.key) == 'up':
                texto = "Para cima"
            elif pygame.key.name(event.key) == 'down':
                texto = "Para baixo"
        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    if texto != "":
        font = pygame.font.Font(None, 32)
        text = font.render(texto, True, (0, 255, 0), (0, 0, 128))
        screen.blit(text, [100,50])

    pygame.display.flip()

pygame.quit()