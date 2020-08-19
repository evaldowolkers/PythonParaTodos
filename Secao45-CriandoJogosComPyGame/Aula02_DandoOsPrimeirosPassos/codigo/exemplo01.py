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
    # Percorrendo a fila de eventos
    for event in pygame.event.get():
        # Verificando o evento KEYDOWN, q é uma constante definida em pygame.locals
        if event.type == KEYDOWN:
            # Se a tecla Esc for pressionada, setamos a variável running para False para sair do loop principal
            if event.key == K_ESCAPE:
                running = False
                # Verificando se o evento foi o QUIT e setamos running para False
        elif event.type == QUIT:
            running = False
