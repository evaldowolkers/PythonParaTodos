import pygame

from pygame.locals import *

pygame.init()
# Definindo o tamanho da tela
screen = pygame.display.set_mode((400, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Preenchendo a superfície com branco
    screen.fill((255, 255, 255))

    # Criando um objeto fonte especificando o arquivo da fonte
    font = pygame.font.Font("VINERITC.TTF", 32)
    text = font.render('PyGame', True, (0, 255, 0), (0, 0, 128))
    screen.blit(text, [100,50])
    pygame.display.flip()

pygame.quit()