import pygame
from pygame import mixer
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
running = True
imagem = 'esquerda'

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_LEFT:
                imagem = "esquerda"
                mixer.music.load("rocklee.mp3")
                mixer.music.play()
            elif event.key == K_DOWN:
                imagem = "baixo"
                mixer.music.load("guy.mp3")
                mixer.music.play()
            elif event.key == K_RIGHT:
                imagem = "direita"
                mixer.music.load("sasuke.mp3")
                mixer.music.play()
            elif event.key == K_UP:
                imagem = "cima"
                mixer.music.load("naruto.mp3")
                mixer.music.play()
        elif event.type == QUIT:
            running = False

    screen.fill((255, 255, 255))
    if imagem == "esquerda":
        imagem = pygame.image.load('rocklee.jpg')
    if imagem == "direita":
        imagem = pygame.image.load('sasuke.jpg')
    if imagem == "cima":
        imagem = pygame.image.load('naruto-uzumaki.jpg')
    if imagem == "baixo":
        imagem = pygame.image.load('guy.jpg')
    screen.blit(imagem, [0,0])

    pygame.display.flip()
pygame.quit()
