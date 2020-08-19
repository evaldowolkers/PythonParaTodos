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

    # Desenha uma elipse Vermelha
    # Devemos informar a superfície onde vamos desenhar, uma tupla com a cor, e um objeto Rect, que armazena
    # coordenadas retangulares e indica a posição e as dimensões da elipse, a elipse será centralizada dentro
    # do retângulo e delimitada por ele.
    # (255, 0, 0) é uma tupla para a cor vermelho
    # Os parâmetros de um Rect são:
    # Rect(esquerda, topo, largura, altura)
    retangulo = pygame.Rect(140, 120, 120, 80)
    pygame.draw.ellipse(screen, (255, 0, 0), retangulo)

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
