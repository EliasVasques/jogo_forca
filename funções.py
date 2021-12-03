import pygame

def msg(tela, texto, x, y, tamanho_fonte, cor):
    fonte = pygame.font.SysFont('arial', tamanho_fonte)
    letra = fonte.render(texto, True, cor)
    tela.blit(letra, (x, y))
