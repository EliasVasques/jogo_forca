import pygame
from pygame.locals import *
from sys import exit

from forca import Forca
from funções import msg

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (30, 172, 235, 92)
VERMELHO = (235, 69, 15)
VERDE = (83, 172, 37, 67)
AZUL_FORTE = (40, 154, 240, 94)
MARROM = (107, 84, 0, 86)

LARGURA = 640
ALTURA = 480

pygame.init()

palavras_descricoes = [['alienigina', 'outro planeta'], ['mouse', 'pc'], ['caderno', 'escola'], ['chinelo', 'calçado'], ['arroz', 'comida']] 
indice_ult_palavra = len(palavras_descricoes)
cont = 1

forca = Forca(palavras_descricoes[0][0], palavras_descricoes[0][1]) # primeiro

tela = pygame.display.set_mode((LARGURA, ALTURA))

letras = {"a": K_a, "b": K_b, "c": K_c, "d": K_d, "e": K_e, "f": K_f, "g": K_g, "h": K_h, "i":K_i, "j": K_j, "k": K_k, "l": K_l, "m": K_m, "n": K_n, "o": K_o, "p": K_p, "q": K_q, "r": K_r, "s": K_s, "t": K_t, "u": K_u, "v": K_v, "w": K_w, "x": K_x, "y": K_y, "z": K_z}

pontos_jogador = 0
pontos_pc = 0

while True:
    tela.fill(BRANCO)

    x = 0
    y = 40
    while True:
        pygame.draw.rect(tela, AZUL, (x, y, LARGURA, 1))
        y += 30
        if y > ALTURA:
            break

    if not forca.vivo() or forca.venceu():
        if cont >= indice_ult_palavra:
            msg(tela, "Fim Jogo", 150, 280, 80, MARROM)
            espaco = "sair"
        elif not forca.vivo():
            msg(tela, "Você perdeu", 180, 300, 50, VERMELHO)
            espaco = "continuar"
        elif forca.venceu():
            msg(tela, "Você venceu", 180, 300, 50, VERDE)
            espaco = "continuar"
        msg(tela, f"espaço para {espaco}", 225, 380, 20, PRETO)

        # mostrar palavra
        for letra in forca.palavra: # mostrar toda palavra
            forca.certo.append(letra)
    
    
    # pontos
    msg(tela, f"você: {pontos_jogador}", 20, 50, 20, VERDE)
    msg(tela, f"pc: {pontos_pc}", 580, 50, 20, VERMELHO)

    # descrição
    msg(tela, forca.descricao, 225, 80, 35, PRETO)

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

                    if cont <= indice_ult_palavra: 
                        forca = Forca(palavras_descricoes[cont][0], palavras_descricoes[cont][1])
                        cont += 1
                    else:
                        pygame.quit()
                        exit()
            else:
                for letra in letras.keys(): # letras alfabeto
                    if letras[letra] == event.key:  # keydown das letras == pressionou
                        forca.tentativa(letra)

