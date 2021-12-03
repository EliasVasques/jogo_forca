import pygame
from funções import msg

PRETO = (0,0,0)
class Forca:

    def __init__ (self, palavra, descricao):
        self.palavra = palavra
        self.descricao = descricao
        self.todas_tentativas = list()
        self.certo = list()
        self.errado = list()
        self.max_erros = 6

    def exibir_palavra(self, tela):
        x = 200
        y = 250 
        largura_traco = 25
        altura_traco = 2
        tamanho_fonte_letras = 20
        for letra in self.palavra:
            if letra not in self.certo:
                pygame.draw.rect(tela, PRETO, (x, y, largura_traco, altura_traco))
            else:
                msg(tela, letra, x + 10, y - 20, tamanho_fonte_letras, PRETO)
            x += 30

    def exibir_forca(self, tela):
        x_forca = 80
        y_forca = 135
        forca = pygame.image.load("forca.png")
        forca = pygame.transform.scale(forca, (128, 128))
        tela.blit(forca, (x_forca, y_forca))

        qtd_erros = len(self.errado)
        if qtd_erros >= 1: 
            cabeca = pygame.image.load("cabeça.png")
            x_cabeca = 153
            y_cabeca = 165
            tela.blit(cabeca, (x_cabeca, y_cabeca))
        if qtd_erros >= 2:
            corpo = pygame.image.load("corpo.png")
            x_corpo = 155
            y_corpo = 177
            tela.blit(corpo, (x_corpo, y_corpo))
        if qtd_erros >= 3:
            braco_direito = pygame.image.load("perna_braço_direito.png")
            x_braco_direito = 152
            y_braco_direito = 173
            tela.blit(braco_direito, (x_braco_direito, y_braco_direito))
        if qtd_erros >= 4:
            braco_esquerdo = pygame.image.load("perna_braço_esquerdo.png")
            x_braco_esquerdo = 158
            y_braco_esquerdo = 173
            tela.blit(braco_esquerdo, (x_braco_esquerdo, y_braco_esquerdo))
        if qtd_erros >= 5:
            perna_direita = pygame.image.load("perna_braço_direito.png")
            x_perna_direita = 152
            y_perna_direita = 191
            tela.blit(perna_direita, (x_perna_direita, y_perna_direita))
        if qtd_erros >= 6:
            perna_esquerda = pygame.image.load("perna_braço_esquerdo.png")
            x_perna_esquerda = 158
            y_perna_esquerda = 191
            tela.blit(perna_esquerda, (x_perna_esquerda, y_perna_esquerda))

    def vivo (self):
        qtd_erros = len(self.errado)
        if qtd_erros == self.max_erros:
            return False
        return True

    def tentativa (self, letra):
        if letra in self.palavra:
            self.certo.append(letra)
        else:
            self.errado.append(letra)
        self.todas_tentativas.append(letra)

    def venceu(self):
        for letra in self.palavra:
            if letra not in self.certo:
                return False
        return True

    
