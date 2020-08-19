import pygame

# Importação realizada para acessar as constantes de teclado
from pygame.locals import *

# Iniciando o pygame
pygame.init()

# Desenhando a tela
screen = pygame.display.set_mode((400, 300))

# Variável para manter nosso loop principal executando
running = True

# Loop principal
while running:
    # Preenche a superfície com branco
    screen.fill((255, 255, 255))

    # Desenha um polígono vermelho na tela
    # (255, 0, 0): Cor vermelha
    # [(x,y), (x,y), (x,y]: Lista contendo as tuplas com as coordenadas
    pygame.draw.polygon(screen, (255, 0, 0), [(10,12), (10,28), (30,20)])
    # Polígono azul
    pygame.draw.polygon(screen, (0, 0, 255), [(30,20), (50,28), (50,12)])

    # Atualiza o conteúdo de toda a tela
    pygame.display.flip()
    # Percorrendo a fila de eventos
    for event in pygame.event.get():
        # Verificando o evento KEYDOWN, q é uma constante definida em pygame.locals
        if event.type == KEYDOWN:
            # Se a tecla Esc for pressionada, setamos a variável
            # running para False para sair do loop principal
            if event.key == K_ESCAPE:
                running = False
            # Verificando se o evento foi o QUIT e setamos running para False
        elif event.type == QUIT:
            running = False
