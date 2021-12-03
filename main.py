import pygame
from pygame.locals import *
from sys import exit

from forca import Forca

BRANCO = (255,255,255)
LARGURA = 640
ALTURA = 480

pygame.init()

palavras_descricoes = [['alienigina', 'outro planeta'], ['mouse', 'pc'], ['caderno', 'escola'], ['chinelo', 'calçado'], ['arroz', 'comida']] 
cont = 1

forca = Forca(palavras_descricoes[0][0], palavras_descricoes[0][1]) # primeiro

tela = pygame.display.set_mode((LARGURA, ALTURA))

letras = {"a": K_a, "b": K_b, "c": K_c, "d": K_d, "e": K_e, "f": K_f, "g": K_g, "h": K_h, "i":K_i, "j": K_j, "k": K_k, "l": K_l, "m": K_m, "n": K_n, "o": K_o, "p": K_p, "q": K_q, "r": K_r, "s": K_s, "t": K_t, "u": K_u, "v": K_v, "w": K_w, "x": K_x, "y": K_y, "z": K_z}

pontos_jogador = 0
pontos_pc = 0

while True:
    tela.fill(BRANCO)

    if not forca.vivo() or forca.venceu():
        if cont > 4:  # ult indice da lista de palavras_descricoes
            forca.msg_fim_jogo(tela)
        elif not forca.vivo():
            forca.msg_game_over(tela)
        elif forca.venceu():
            forca.msg_venceu(tela)
    else:
        forca.exibir_pontos(tela, pontos_jogador, pontos_pc)
        forca.exibir_descricao(tela)
        forca.exibir_forca(tela)
        forca.exibir_palavra(tela)


        
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if not forca.vivo() or forca.venceu():
                if event.key == K_SPACE:
                    if not forca.vivo():
                        pontos_pc += 1
                    elif forca.venceu():
                        pontos_jogador += 1

                    if cont <= 4:
                        forca = Forca(palavras_descricoes[cont][0], palavras_descricoes[cont][1])
                        cont += 1
                    else:
                        pygame.quit()
                        exit()
            else:
                for letra in letras.keys(): # letras alfabeto
                    if letras[letra] == event.key:  # keydown das letras == pressionou
                        forca.tentativa(letra)


