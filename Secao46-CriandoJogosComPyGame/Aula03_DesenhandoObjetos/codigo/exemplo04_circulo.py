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

    # Desenha um círculo Vermelho
    # Devemos informar a superfície onde vamos desenhar, a cor, uma tupla com x e y para o Centro e o Raio
    # (255, 0, 0) é uma tupla para a cor vermelho
    # (200, 140), onde X é 200 e y, 140, lembrando que nossa tela tem x=400 e y=300
    # Vamos definir um raio de 80 pixels
    pygame.draw.circle(screen, (255, 0, 0), (200,140), 80)

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
