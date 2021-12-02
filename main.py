import pygame
from pygame.locals import *
from sys import exit

from forca import Forca

forca = Forca("alienigina", 10)

pygame.init()
LARGURA = 640
ALTURA = 480
tela = pygame.display.set_mode((LARGURA, ALTURA))

while True:
    tela.fill((255,255,255))
    forca.exibir_palavra(tela)
    forca.exibir_forca(tela)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

