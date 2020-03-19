import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640,480))
# Criando a variável "cor" com o nome da cor azul
cor = Color('blue')
# Definindo a representação HSVA da variável cor com
# 100 para tonalidade, 100 para saturação,
# 100 para brilho e 50 para transparência
cor.hsva = (100, 100, 100, 50)
# nova_cor recebendo as cores vermelho, verde e azul
# do objeto cor já alterado
nova_cor = Color(cor.r, cor.g, cor.b)

running = True
imagem = 'esquerda'

# Desenhando o primeiro retângulo
pygame.draw.rect(screen, nova_cor, [0, 0, 50, 50])
# Alterando várias vezes a tonalidade, saturação,
# brilho e transparência das cores e desenhando
# um retângulo diferente
nova_cor.hsva = (50, 100, 100, 50)
pygame.draw.rect(screen, nova_cor, [0, 50, 50, 50])
nova_cor.hsva = (0, 100, 100, 50)
pygame.draw.rect(screen, nova_cor, [0, 100, 50, 50])
nova_cor.hsva = (30, 30, 30, 50)
pygame.draw.rect(screen, nova_cor, [0, 150, 50, 50])
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

pygame.quit()