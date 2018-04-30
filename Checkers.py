# -*- coding: utf-8 -*-
# aluna: siuanny.rocha (117210395)
# atividade: damas (unidade 11 - Miniprojeto 1)
# 2017.2, programação 1 - ufcg

# imports
import sys
import pygame
from Peca import *
from Cell import *
from Const import *
from pygame.locals import *


# classe do jogo de damas (manipulação do tabuleiro)
class Checkers:

    # iniciar o jogo
    def __init__(self, tela, vez):
        self.tela = tela
        self.saltando = False
        self.jogador_atual = vez
        self.movimentos_das_escuras, self.movimentos_das_claras = 0, 0
        self.setar_tabuleiro()
        self.desenhar()

    # iniciar tabuleiro
    def setar_tabuleiro(self):
        self.selecionada = None
        self.tabuleiro = []
        tabuleiro = self.tabuleiro

        for l in range(8):
            tabuleiro.append([])
            for c in range(8):
                posicao_no_tabuleiro = (l, c)
                celula = Cell(posicao_no_tabuleiro)
                tabuleiro[l].append(celula)

        self.setar_jogadores(self.tabuleiro)

    # iniciar peças
    def setar_jogadores(self, tabuleiro):
        for l in range(3):
            for c in range(len(tabuleiro[l])):
                if eh_casa_valida(l, c):
                    tabuleiro[l][c].peca = Peca(escuras)

                if eh_casa_valida(l-3, c):
                    tabuleiro[l-3][c].peca = Peca(claras)

    # renderiza o tabuleiro na tela com base no atributo 'tabuleiro' (matriz)
    def renderizar(self):
        tabuleiro = self.tabuleiro
        for l in range(len(tabuleiro)):
            for c in range(len(tabuleiro[l])):
                celula = tabuleiro[l][c]
                self.tela.blit(celula.image, celula.rect)

    # desenhar tabuleiro
    def desenhar(self):
        tela = self.tela
        tabuleiro = self.tabuleiro
        for l in range(len(tabuleiro)):
            for c in range(len(tabuleiro[l])):
                celula = tabuleiro[l][c]
                celula.atualizar_imagem()
                self.tela.blit(celula.image, celula.rect)

    # analisa sugestões para a célula selecionada
    def celula_selecionada(self, celula, permanece_saltando = False):
        if not self.saltando or (self.saltando and permanece_saltando):
            self.selecionada = None
            tabuleiro = self.tabuleiro
            possui_celula = celula.peca.jogador == self.jogador_atual
            if celula.tem_peca():
                if possui_celula:
                    self.desenhar()                                             # limpa células disponiveis
                    if celula in self.obter_celulas_disponiveis():
                        celula.cor_tabuleiro(True)
                        self.selecionada = celula

                        celulas = self.obter_movimentos(celula)

                        oponente = claras if self.jogador_atual == escuras else escuras

                        for celulas_adjacentes in celulas:
                            if not celulas_adjacentes.tem_peca():
                                celulas_adjacentes.tabuleiro()
                        return
                    else:
                        celula.cor_tabuleiro(False)
                        return
                else:
                    pass

            self.desenhar()

    # dada uma célula, retorna celulas adjacentes
    def obter_adjacentes(self, celula):
        l, c = celula.posicao_no_tabuleiro
        tabuleiro = self.tabuleiro
        celulas = []
        if celula.peca.eh_dama:
            # se tiver uma peça aliada na diagonal, para de sugerir celulas após ela
            # já que a dama não pode pular por cima de suas proprias peças
            row_plus_col_plus = True
            row_plus_col_minus = True
            row_minus_col_plus = True
            row_minus_col_minus = True

            for i in range(1, len(tabuleiro)):
                if l + i < len(tabuleiro):
                    if c + i < len(tabuleiro[l]) and row_plus_col_plus:
                        proxima_celula = tabuleiro[l+i][c+i]
                        if proxima_celula.tem_peca() and proxima_celula.peca.jogador == celula.peca.jogador:
                            row_plus_col_plus = False
                        else:
                            celulas.append(proxima_celula)
                    if c - i >= 0 and row_plus_col_minus:
                        proxima_celula = tabuleiro[l+i][c-i]
                        if proxima_celula.tem_peca() and proxima_celula.peca.jogador == celula.peca.jogador:
                            row_plus_col_minus = False
                        else:
                            celulas.append(proxima_celula)
                if l - i >= 0:
                    if c + i < len(tabuleiro[l]) and row_minus_col_plus:
                        proxima_celula = tabuleiro[l-i][c+i]
                        if proxima_celula.tem_peca() and proxima_celula.peca.jogador == celula.peca.jogador:
                            row_minus_col_plus = False
                        else:
                            celulas.append(proxima_celula)
                    if c - i >= 0 and row_minus_col_minus:
                        proxima_celula = tabuleiro[l-i][c-i]
                        if proxima_celula.tem_peca() and proxima_celula.peca.jogador == celula.peca.jogador:
                            row_minus_col_minus = False
                        else:
                            celulas.append(proxima_celula)
        else:
            # adj_row = l + direcao[celula.peca.jogador]
            if l + 1 < len(tabuleiro):
                if c + 1 < len(tabuleiro[l]):
                    celulas.append(tabuleiro[l+1][c+1])
                if c - 1 >= 0:
                    celulas.append(tabuleiro[l+1][c-1])
            if l - 1 >= 0:
                if c + 1 < len(tabuleiro[l]):
                    celulas.append(tabuleiro[l-1][c+1])
                if c - 1 >= 0:
                    celulas.append(tabuleiro[l-1][c-1])

        # remove as células do jogador da vez
        for i in range(len(celulas) - 1, -1, -1):
            if celulas[i].tem_peca() and celula.peca.jogador == celulas[i].peca.jogador:
                celulas.pop(i)
        return celulas

    # obtem peças de um dado jogador
    def obter_pecas(self, jogador = None):
        if jogador is None:
            jogador = self.jogador_atual

        pecas = []
        for l in range(len(self.tabuleiro)):
            for c in range(len(self.tabuleiro[l])):
                celula = self.tabuleiro[l][c]
                if celula.tem_peca() and celula.peca.jogador == jogador:
                    pecas.append(celula)
        return pecas

    # analisa as possibilidades de 'comer' outra peça
    def eh_um_pulo(self, origem, destino):
        if origem.tem_peca() and not destino.tem_peca():
            linha_de_origem, coluna_de_origem = origem.posicao_no_tabuleiro
            linha_de_destino, coluna_de_destino = destino.posicao_no_tabuleiro
            distancia = abs(linha_de_destino - linha_de_origem)

            if distancia >= 2:
                if origem.peca.eh_dama:
                    dir_l = 1 if linha_de_destino - linha_de_origem >= 0 else -1
                    dir_c = 1 if coluna_de_destino - coluna_de_origem >= 0 else -1

                    oponentes_entre = 0
                    for n in range(1, distancia):
                        l_intermediaria = linha_de_origem + n * dir_l
                        c_intermediaria = coluna_de_origem + n * dir_c
                        celula_intermediaria = self.tabuleiro[l_intermediaria][c_intermediaria]

                        # Se houver uma peça entre a origem e o destino
                        if celula_intermediaria.tem_peca():
                            # E a peça for do oponente, incrementa um no número de inimigos entre a origem e o destino
                            if celula_intermediaria.peca.jogador == capturar(self.jogador_atual):
                                oponentes_entre += 1
                            # Se a peça for aliada, o pulo não é possível
                            else:
                                return False
                    # Só é um pulo se o número de inimigos entre a origem e o destino for igual a 1
                    return oponentes_entre == 1
                else:
                    return distancia == 2

        return False

    # analisa se há peças que podem ser capturadas
    def tem_celula_saltavel(self, pecas):
        for peca in pecas:
            movimentos = self.obter_movimentos(peca)
            linha_de_origem, coluna_de_origem = peca.posicao_no_tabuleiro
            for movimento in movimentos:
                linha_de_destino, coluna_de_destino = movimento.posicao_no_tabuleiro
                if self.eh_um_pulo(peca, movimento):
                    return True
        return False

    # obtém peças que podem ser capturadas
    def obter_celulas_saltaveis(self, pecas, jogador = None):
        if jogador is None:
            jogador = self.jogador_atual

        saltaveis = []
        if self.tem_celula_saltavel(pecas):
            for peca in pecas:
                movimentos = self.obter_movimentos(peca, jogador)
                linha_de_origem, coluna_de_origem = peca.posicao_no_tabuleiro
                for movimento in movimentos:
                    linha_de_destino, coluna_de_destino = movimento.posicao_no_tabuleiro

                    if self.eh_um_pulo(peca, movimento):
                        saltaveis.append(peca)
                        break

        return saltaveis

    # obtém as células que possuiem movimento disponivel
    def obter_celulas_disponiveis(self, jogador = None):
        if jogador is None:
            jogador = self.jogador_atual

        pecas = self.obter_pecas(jogador)
        disponiveis = []

        celulas_saltaveis = self.obter_celulas_saltaveis(pecas, jogador)

        if celulas_saltaveis == []:
            for peca in pecas:
                movimentos = self.obter_movimentos(peca, jogador)

                if movimentos == []:
                    continue

                disponiveis.append(peca)
        else:
            disponiveis = celulas_saltaveis

        return disponiveis

    # analise se há peças que podem ser capturadas partindo da origem
    def pode_comer(self, origem, alvo):
        tabuleiro = self.tabuleiro
        if origem.tem_peca() and alvo.tem_peca():
            if origem.peca.eh_dama:
                origem_l, origem_c = origem.posicao_no_tabuleiro
                alvo_l, alvo_c = alvo.posicao_no_tabuleiro

                distancia = abs(origem_l - alvo_l)
                dir_l = -1 if alvo_l - origem_l < 0 else 1
                dir_c = -1 if alvo_c - origem_c < 0 else 1

                for i in range(1, distancia):
                    meio_l = origem_l + dir_l * i
                    meio_c = origem_c + dir_c * i
                    celula_intermediaria = tabuleiro[meio_l][meio_c]

                    if celula_intermediaria.tem_peca():
                        return False

                proxima_l = origem_l + dir_l * (distancia + 1)
                proxima_c = origem_c + dir_c * (distancia + 1)
                linha_tabuleiro = proxima_l >= 0 and proxima_l < len(tabuleiro)
                coluna_tabuleiro = proxima_c >= 0 and proxima_c  < len(tabuleiro[0])

                if linha_tabuleiro and coluna_tabuleiro:
                    proxima_celula = tabuleiro[proxima_l][proxima_c]
                    return not proxima_celula.tem_peca()
            else:
                origem_l, origem_c = origem.posicao_no_tabuleiro
                alvo_l, alvo_c = alvo.posicao_no_tabuleiro

                if abs(origem_l - alvo_l) == 1:
                    dir_l = alvo_l - origem_l
                    dir_c = alvo_c - origem_c

                    proxima_l = origem_l + dir_l * 2
                    proxima_c = origem_c + dir_c * 2

                    linha_tabuleiro = proxima_l >= 0 and proxima_l < len(tabuleiro)
                    coluna_tabuleiro = proxima_c >= 0 and proxima_c < len(tabuleiro[0])
                    distancia = abs(origem_l - proxima_l)

                    if linha_tabuleiro and coluna_tabuleiro and distancia == 2:
                        proxima_celula = tabuleiro[proxima_l][proxima_c]
                        return not proxima_celula.tem_peca()

        return False

    # analisa se pode ir da célula de origem a célula de destino
    def pode_ir(self, origem, destino):
        linha_de_destino, coluna_de_destino = destino.posicao_no_tabuleiro
        linha_de_origem, coluna_de_origem = origem.posicao_no_tabuleiro
        # não permitir pulos que deêm a volta no tabuleiro
        distancia = abs(linha_de_destino - linha_de_origem)
        dir_l = 1 if linha_de_destino - linha_de_origem >= 0 else -1
        dir_c = 1 if coluna_de_destino - coluna_de_origem >= 0 else -1

        if origem.peca.eh_dama:
            oponentes_entre = 0
            for i in range(distancia):
                celula = self.tabuleiro[linha_de_origem + dir_l * i][coluna_de_origem + dir_c * i]
                jogador = origem.peca.jogador
                if celula.tem_peca() and capturar(jogador) == celula.peca.jogador:
                    oponentes_entre += 1

            if oponentes_entre <= 1:
                return True
        else:
            if direcao[origem.peca.jogador] == dir_l:
                if distancia == 2:
                    saltada_l = (linha_de_origem + linha_de_destino) / 2
                    saltada_c = (coluna_de_origem + coluna_de_destino) / 2
                    celula_saltada = self.tabuleiro[saltada_l][saltada_c]

                    if self.pode_comer(origem, celula_saltada):
                        return True
                    else:
                        return False
                elif distancia == 1:
                    return not destino.tem_peca()

        return False

    # obtém os movimentos possíveis partindo da célula de origem
    def obter_movimentos(self, origem, jogador = None):
        if jogador is None:
            jogador = self.jogador_atual

        tabuleiro = self.tabuleiro
        oponente = capturar(jogador)
        movimentos = []

        if origem.tem_peca():
            celulas = self.obter_adjacentes(origem)
            tem_movimento_de_captura = False

            for celula in celulas:
                if celula.tem_peca() and celula.peca.jogador == oponente and self.pode_comer(origem, celula):
                    tem_movimento_de_captura = True

            if tem_movimento_de_captura:
                if origem.peca.eh_dama:
                    for celula in celulas:
                        if self.pode_comer(origem, celula):
                            linha_de_destino, coluna_de_destino = celula.posicao_no_tabuleiro
                            linha_de_origem, coluna_de_origem = origem.posicao_no_tabuleiro

                            dir_l = 1 if linha_de_destino - linha_de_origem >= 0 else -1
                            dir_c = 1 if coluna_de_destino - coluna_de_origem >= 0 else -1

                            for i in range(1, 8):
                                proxima_l = linha_de_destino + dir_l * i
                                proxima_c = coluna_de_destino + dir_c * i

                                na_linha = proxima_l >= 0 and proxima_l < len(tabuleiro)
                                na_coluna = proxima_c >= 0 and proxima_c < len(tabuleiro[0])

                                if na_linha and na_coluna:
                                    proxima_celula = tabuleiro[proxima_l][proxima_c]

                                    if proxima_celula.tem_peca():
                                        break

                                    movimentos.append(proxima_celula)

                else:
                    for celula in celulas:
                        if self.pode_comer(origem, celula):
                            linha_de_destino, coluna_de_destino = celula.posicao_no_tabuleiro
                            linha_de_origem, coluna_de_origem = origem.posicao_no_tabuleiro

                            dir_l = 1 if linha_de_destino - linha_de_origem >= 0 else -1
                            dir_c = 1 if coluna_de_destino - coluna_de_origem >= 0 else -1

                            proxima_l = linha_de_origem + dir_l * 2
                            proxima_c = coluna_de_origem + dir_c * 2

                            proxima_celula = tabuleiro[proxima_l][proxima_c]
                            movimentos.append(proxima_celula)
            else:
                for i in range(len(celulas) - 1, -1, -1):
                    if self.pode_ir(origem, celulas[i]):
                        movimentos.append(celulas[i])

        return movimentos

    # retorna o destino das peças que podem ser movidas
    def pode_mover(self, origem, destino):
        return destino in self.obter_movimentos(origem)

    # retorna se há ou não damas no tabuleiro
    def procura_damas(self, tabuleiro):
        for l in range(len(tabuleiro)):
            for c in range(len(tabuleiro)):
                celula = tabuleiro[l][c]
                if celula.tem_peca() and celula.peca.eh_dama:
                    return True
        return False

    # Realiza um movimento da peça selecionada para a celula destino
    def movimento(self, destino):
        selecionada = self.selecionada
        linha_atual, coluna_atual = self.selecionada.posicao_no_tabuleiro
        linha_de_destino, coluna_de_destino = destino.posicao_no_tabuleiro
        saltou = False

        distancia = abs(linha_atual - linha_de_destino)
        if distancia >= 2:
            # apenas para peças comuns
            if not selecionada.peca.eh_dama:
                saltada_l = (linha_atual + linha_de_destino) / 2
                saltada_c = (coluna_atual + coluna_de_destino) / 2
                celula_saltada = self.tabuleiro[saltada_l][saltada_c]

                if self.pode_comer(selecionada, celula_saltada):
                    celula_saltada.peca = None
                    saltou = True
                    self.saltando = True
                else:
                    return
            # para damas
            else:
                if self.pode_ir(selecionada, destino):
                    for i in range(distancia):
                        dir_l = 1 if linha_de_destino - linha_atual >= 0 else -1
                        dir_c = 1 if coluna_de_destino - coluna_atual >= 0 else -1
                        saltada_l = linha_atual + dir_l * i
                        saltada_c = coluna_atual + dir_c * i
                        celula_saltada = self.tabuleiro[saltada_l][saltada_c]
                        jogador = selecionada.peca.jogador
                        if celula_saltada.tem_peca() and capturar(jogador) == celula_saltada.peca.jogador:
                            if self.pode_comer(selecionada, celula_saltada):
                                celula_saltada.peca = None
                                saltou = True
                                self.saltando = True
                            else:
                                return

        no_tabuleiro = linha_de_destino in [0, len(self.tabuleiro) - 1]
        nao_eh_dama = not selecionada.peca.eh_dama

        if direcao[selecionada.peca.jogador] == -1:
            eh_linha_de_coroacao = linha_de_destino == 0
        else:
            eh_linha_de_coroacao = linha_de_destino == 7

        destino.peca = selecionada.peca
        selecionada.peca = None
        selecionada = destino
        self.desenhar()

        permanece_tendo_captura = self.tem_celula_saltavel([selecionada])

        if permanece_tendo_captura:
            if saltou:
                self.celula_selecionada(selecionada, True)
                return

        if eh_linha_de_coroacao:
            selecionada.peca.eh_dama = True

        if self.jogador_atual == claras:
            self.movimentos_das_claras += 1
        else:
            self.movimentos_das_escuras += 1

        self.saltando = False
        self.jogador_atual = claras if self.jogador_atual == escuras else escuras
        self.desenhar()
