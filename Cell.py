# -*- coding: utf-8 -*-
# aluna: siuanny.rocha (117210395)
# atividade: damas (unidade 11 - Miniprojeto 1)
# 2017.2, programação 1 - ufcg

# imports
import sys
import pygame
from Const import *
from pygame.locals import *


# classe das células (modelo para a célula)
class Cell(pygame.sprite.Sprite):

    # inicialização
    def __init__(self, posicao_no_tabuleiro, peca = None):
        pygame.sprite.Sprite.__init__(self)
        self.posicao_no_tabuleiro = posicao_no_tabuleiro
        self.peca = peca
        self.atualizar_imagem()
        l, c = posicao_no_tabuleiro
        posicao = tamanho_casas * (c + deslocamento_coluna), tamanho_casas * (l + deslocamento_linha)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = posicao

    # desenha células
    def desenhar_celula(self):
        l, c = self.posicao_no_tabuleiro

        if (c % 2 == 0 and l % 2 == 0) or (c % 2 != 0 and l % 2 != 0):
            cor = cores[bloqueado]
        else:
            cor = cores[livre]

        self.image = pygame.Surface([tamanho_casas, tamanho_casas])
        self.image.fill(cor)

    # desenha peça
    def desenhar_peca(self):
        if self.tem_peca():
            cor = cores[self.peca.jogador][0]
            centro = cores[self.peca.jogador][1]
            pygame.draw.circle(self.image, cor, (tamanho_casas / 2, tamanho_casas / 2), tamanho_circulos)
            pygame.draw.circle(self.image, centro , (tamanho_casas / 2, tamanho_casas / 2), tamanho_casas/3, 5)

            if self.peca.eh_dama:
                imagem = self.image
                fundo = pygame.image.load("imagens/coroa.png")
                imagem.blit(fundo, ((tamanho_casas / 2 - 12.5, tamanho_casas / 2 - 11)))

    def atualizar_imagem(self):
        self.desenhar_celula()
        self.desenhar_peca()

    def cor_tabuleiro(self, disponiveis):
        cor = disponivel if disponiveis else nao_disponivel
        self.image = pygame.Surface([tamanho_casas, tamanho_casas])
        self.image.fill(cores[cor])
        self.desenhar_peca()

    def tabuleiro(self):
        self.image = pygame.Surface([tamanho_casas, tamanho_casas])
        self.image.fill(cores[sugerido])

    def atualizar_posicao(self, position):
        self.rect.x, self.rect.y = position

    def tem_peca(self):
        return self.peca is not None
