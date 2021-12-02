import pygame

class Forca:

    def __init__ (self, palavra, qtd_chances):
        self.palavra = palavra
        self.qtd_chances = qtd_chances
        self.todas_tentativas = list()
        self.certo = list()
        self.errado = list()

    def exibir_letra (self, tela, letra, x, y):
        self.fonte = pygame.font.SysFont('arial', 20)
        letra = self.fonte.render(letra, True, (0,0,0))
        tela.blit(letra, (x + 10, y - 20))

    def exibir_palavra(self, tela):
        x = 200  # inicial
        y = 250 
        largura = 25
        altura = 1
        for letra in self.palavra:
            if letra not in self.certo:
                pygame.draw.rect(tela, (0,0,0), (x, y, largura, altura))
            else:
                self.exibir_letra(tela, letra, x, y)
            x += 30

    def exibir_forca(self, tela):
        x = 80
        y = 135
        forca = pygame.image.load("forca.png")
        forca = pygame.transform.scale(forca, (128, 128))

        cabeca = pygame.image.load("cabeça.png")
        corpo = pygame.image.load("corpo.png")
        perna_braco_direito = pygame.image.load("perna_braço_direito.png")
        perna_braco_esquerdo = pygame.image.load("perna_braço_esquerdo.png")

        tela.blit(forca, (x, y))

        qtd_erros = len(self.errado)
        if qtd_erros >= 1: 
            tela.blit(cabeca, (x+73, y+30))
        if qtd_erros >= 2:
            tela.blit(corpo, (x+75, y+42))
        if qtd_erros >= 3:
            tela.blit(perna_braco_direito, (x+72, y+38))
        if qtd_erros >= 4:
            tela.blit(perna_braco_direito, (x+72, y+56))
        if qtd_erros >= 5:
            tela.blit(perna_braco_esquerdo, (x+78, y+38))
        if qtd_erros >= 6:
            tela.blit(perna_braco_esquerdo, (x+78, y+56))
    