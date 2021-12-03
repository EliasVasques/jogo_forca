import pygame
PRETO = (0,0,0)

def msg(tela, texto, x, y, tamanho_fonte):
    fonte = pygame.font.SysFont('arial', tamanho_fonte)
    letra = fonte.render(texto, True, PRETO)
    tela.blit(letra, (x, y))
