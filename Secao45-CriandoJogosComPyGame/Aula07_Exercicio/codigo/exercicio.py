import pygame

# Importação realizada para acessar as constantes de teclado
from pygame.locals import *

# Iniciando o pygame
pygame.init()

# Definindo o tamanho da tela
screen = pygame.display.set_mode((400, 400))

# Variável para manter nosso loop principal executando
running = True
# Definindo o conteúdo da variável de controle para
# carregar a imagem esquerda
imagem = 'esquerda'

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
            # Se a tecla seta para esquerda for pressionada,
            # muda a variável imagem para 'esquerda'
            elif event.key == K_LEFT:
                imagem = "esquerda"
            # Se a tecla seta para direita for pressionada,
            # muda a variável imagem para 'direita'
            elif event.key == K_RIGHT:
                imagem = "direita"
        # Verificando se o evento foi o QUIT (quando fechamos a janela)
        # e setamos running para False
        elif event.type == QUIT:
            running = False

    # Preenchendo a superfície com branco
    screen.fill((255, 255, 255))
    # Carregando a imagem de acordo com o conteúdo
    # da variável imagem
    if imagem == 'esquerda':
        imagem = pygame.image.load('naruto_esquerda.png')
    elif imagem == 'direita':
        imagem = pygame.image.load('naruto_direita.png')
    # Desenha a imagem na tela
    # blit(objeto_imagem, uma_lista_com_largura_altura)
    screen.blit(imagem, [80, 50])
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()