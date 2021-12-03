import pygame

PRETO = (0,0,0)
class Forca:

    def __init__ (self, palavra, descricao):
        self.palavra = palavra
        self.descricao = descricao
        self.todas_tentativas = list()
        self.certo = list()
        self.errado = list()

    def exibir_texto (self, tela, texto, x, y, tamanho_fonte):
        self.fonte = pygame.font.SysFont('arial', tamanho_fonte)
        letra = self.fonte.render(texto, True, (0,0,0))
        tela.blit(letra, (x, y))

    def exibir_palavra(self, tela):
        x = 200
        y = 250 
        largura_traco = 25
        altura_traco = 1
        tamanho_fonte_letras = 20
        for letra in self.palavra:
            if letra not in self.certo:
                pygame.draw.rect(tela, PRETO, (x, y, largura_traco, altura_traco))
            else:
                self.exibir_texto(tela, letra, x + 10, y - 20, tamanho_fonte_letras)
            x += 30

    def exibir_descricao(self, tela):
        x = 225
        y = 80
        tamanho_fonte_descricao = 35
        self.exibir_texto(tela, self.descricao, x, y, tamanho_fonte_descricao)

    def msg_fim_jogo(self, tela):
        x_game_over = 115
        y_game_over = 100
        tamanho_fonte_game_over = 80
        self.exibir_texto(tela, "Fim de Jogo", x_game_over, y_game_over, tamanho_fonte_game_over)

        x_sair = 180
        y_sair = 200
        tamanho_fonte_sair = 30
        self.exibir_texto(tela, "espaço para sair", x_sair, y_sair, tamanho_fonte_sair)


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
        if qtd_erros == 6:
            return False
        return True

    def msg_game_over (self, tela) :
        x_game_over = 115
        y_game_over = 100
        tamanho_fonte_game_over = 80
        self.exibir_texto(tela, "Game Over", x_game_over, y_game_over, tamanho_fonte_game_over)

        x_ir_novamente = 150
        y_ir_novamente = 200
        tamanho_fonte_ir_novamente = 30
        self.exibir_texto(tela, "espaço para ir novamente", x_ir_novamente, y_ir_novamente, tamanho_fonte_ir_novamente)
    
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

    def msg_venceu(self, tela):
        x_venceu = 100
        y_venceu = 100
        tamanho_fonte_venceu = 80
        self.exibir_texto(tela, "Você venceu", x_venceu, y_venceu, tamanho_fonte_venceu)

        x_ir_novamente = 150
        y_ir_novamente = 200
        tamanho_fonte_ir_novamente = 30
        self.exibir_texto(tela, "espaço para ir novamente", x_ir_novamente, y_ir_novamente, tamanho_fonte_ir_novamente)
    
    def exibir_pontos(self, tela, jogador, pc):
        tamanho_fonte = 20
        y = 50

        x_jogador = 20
        self.exibir_texto(tela, "você: " + str(jogador), x_jogador, y, tamanho_fonte)

        x_pc = 580
        self.exibir_texto(tela, "pc: " + str(pc), x_pc, y, tamanho_fonte)
