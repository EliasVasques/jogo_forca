import pygame
from pygame.locals import *
from sys import exit

from forca import Forca

letras = {"a": K_a, "b": K_b, "c": K_c, "d": K_d, "e": K_e, "f": K_f, "g": K_g, "h": K_h, "i":K_i, "j": K_j, "k": K_k, "l": K_l, "m": K_m, "n": K_n, "o": K_o, "p": K_p, "q": K_q, "r": K_r, "s": K_s, "t": K_t, "u": K_u, "v": K_v, "w": K_w, "x": K_x, "y": K_y, "z": K_z}

forca = Forca("alienigina", 10)


pygame.init()


LARGURA = 640
ALTURA = 480
tela = pygame.display.set_mode((LARGURA, ALTURA))

while True:
    tela.fill((255,255,255))

    

    forca.exibir_forca(tela)
    forca.exibir_palavra(tela)
        
    pygame.display.flip()

    

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if not forca.vivo(): # não tá vivo, não adianta teclar
            continue
        
        if event.type == KEYDOWN:
            for letra in letras.keys(): # letras alfabeto
                if letras[letra] == event.key:  # keydown das letras == pressionado
                    forca.tentativa(letra)


