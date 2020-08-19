import pygame

# Importação realizada para acessar as constantes de teclado
from pygame.locals import *

# Iniciando o pygame
pygame.init()

# Definindo o tamanho da tela
screen = pygame.display.set_mode((400, 400))

# Variável para manter nosso loop principal executando
running = True

# Loop principal
while running:
    # Percorrendo a fila de eventos
    for event in pygame.event.get():
        # Verificando o evento KEYDOWN, q é uma constante definida em pygame.locals
        if event.type == KEYDOWN:
            # Se a tecla Esc for pressionada, setamos a variável
            # running para False para sair do loop principal
            if event.key == K_ESCAPE:
                running = False
        # Verificando se o evento foi o QUIT (quando fechamos a janela)
        # e setamos running para False
        elif event.type == QUIT:
            running = False

    # Preenchendo a superfície com branco
    screen.fill((255, 255, 255))
    # Carregando a imagem de um arquivo chamado
    # pygame.png
    imagem = pygame.image.load("pygame.png")
    # Desenha a imagem na tela
    # blit(objeto_imagem, uma_lista_com_posicao_x_y)
    screen.blit(imagem, [100, 50])
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()