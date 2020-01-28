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
            elif event.key == K_RIGHT:
                texto = "Direita"
            elif event.key == K_LEFT:
                texto = "Esquerda"
            elif event.key == K_UP:
                texto = "Para cima"
            elif event.key == K_DOWN:
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