# -*- coding: utf-8 -*-
# aluna: siuanny.rocha (117210395)
# atividade: damas (unidade 11 - Miniprojeto 1)
# 2017.2, programação 1 - ufcg

# imports
import sys
import Cell
import Peca
import pygame
from Const import *
from Checkers import *
from Game import *
from pygame.locals import *


# classe Game
class Game:

    def __init__(self):
        pygame.init()

    # execução
    def start(self):
#        self.musica()
        self.criar_tela()
        self.escolha = exibir_menu
        self.opcoes = {}
        self.exibir_menu()
        self.loop()

    # cria a janela de execução
    def criar_tela(self):
        pygame.display.set_caption("Jogo de Damas")
        largura = tamanho_casas * 14
        altura = tamanho_casas * 10
        self.tamanho_tela = largura, altura
        self.tela = pygame.display.set_mode(self.tamanho_tela)
        self.clock = pygame.time.Clock()

    # reprodução da música de fundo
    def musica(self):
        pygame.mixer.music.load("musica/amelie.mp3")
        pygame.mixer.music.play()

    # começo da 'partida'
    def iniciar_partida(self):
        self.jogo_de_damas = Checkers(self.tela, claras)    # o segundo parâmetro é quem começa

    # textos
    def objetos_de_texto(self, texto, cor, fonte):
        aparencia = fonte.render(texto, True, cor)
        return aparencia, aparencia.get_rect()

    # mensagens
    def tela_de_mensagens(self, texto, posicao, nome_da_fonte, tamanho, cor, bold=False, center=True):
        fonte = pygame.font.SysFont(nome_da_fonte, tamanho, bold)
        aparencia_do_texto, area_do_texto = self.objetos_de_texto(texto, cor, fonte)
        if center:
            area_do_texto.center = posicao
            self.tela.blit(aparencia_do_texto, area_do_texto)
            return aparencia_do_texto, area_do_texto
        else:
            self.tela.blit(aparencia_do_texto, posicao)

    # tela menu / inical
    def exibir_menu(self):
        inicar = pygame.display.set_mode(self.tamanho_tela)
        tela = self.tela
        fundo = pygame.image.load("imagens/menu.png")
        tela.blit(fundo, (0, 0))

        largura, altura = self.tamanho_tela
        x, x_s = largura / 2.01, largura / 2
        fonte = "purisa"
        h1, h2 = 100, 30
        cor_da_fonte, sombra = (255, 255, 255), (0, 0, 0)

        deslocamento_superior = 150
        self.tela_de_mensagens("Damas", (x_s, deslocamento_superior), fonte, h1, sombra, True)
        self.tela_de_mensagens("Damas", (x, deslocamento_superior), fonte, h1, cor_da_fonte, True)

        deslocamento_superior += 110
        msg = self.tela_de_mensagens(u"História", (x_s, deslocamento_superior), fonte, h2, sombra)
        msg = self.tela_de_mensagens(u"História", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
        self.opcoes[historia] = msg

        deslocamento_superior += 35
        msg = self.tela_de_mensagens("Iniciar", (x_s, deslocamento_superior), fonte, h2, sombra)
        msg = self.tela_de_mensagens("Iniciar", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
        self.opcoes[comecar] = msg

        deslocamento_superior += 35
        msg = self.tela_de_mensagens(u"Instruções", (x_s, deslocamento_superior), fonte, h2, sombra)
        msg = self.tela_de_mensagens(u"Instruções", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
        self.opcoes[ajuda] = msg

        deslocamento_superior += 35
        msg = self.tela_de_mensagens(u"Créditos", (x_s, deslocamento_superior), fonte, h2, sombra)
        msg = self.tela_de_mensagens(u"Créditos", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
        self.opcoes[creditos] = msg

        deslocamento_superior += 35
        msg = self.tela_de_mensagens("Sair", (x_s, deslocamento_superior), fonte, h2, sombra)
        msg = self.tela_de_mensagens("Sair", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
        self.opcoes[sair] = msg

#        deslocamento_superior += 40
#        msg = self.tela_de_mensagens("FIM", (x_s, deslocamento_superior), fonte, h2, sombra)
#        msg = self.tela_de_mensagens("FIM", (x, deslocamento_superior), fonte, h2, cor_da_fonte)
#        self.opcoes[FIM] = msg

        pygame.display.flip()

    # tela de historia
    def historia(self):
        inicar = pygame.display.set_mode(self.tamanho_tela)
        tela = self.tela
        fundo = pygame.image.load("imagens/historia.png")
        tela.blit(fundo, (0, 0))

        largura, altura = self.tamanho_tela
        x, x_s, y = largura / 2.01, largura / 2,  altura - 30
        fonte = "purisa"
        cor_da_fonte, sombra = (255, 255, 255), (0, 0, 0)
        h1, h2, h3 = 40, 17, 12
        deslocamento_superior, deslocamento_lateral = 10, 120
        deslocamento_lateral_s = 118.81188118811882

        self.tela_de_mensagens(u"História", (20, deslocamento_superior), fonte, h1, sombra, True, False)
        self.tela_de_mensagens(u"História", (20 / 1.01, deslocamento_superior), fonte, h1, cor_da_fonte, True, False)

        linha1  = u"    Uma nave da TECG cai no misterioso planeta NoBr3ak-IN4"
        linha2  = u"com um único sobrevivente, o alien Atreyu."
        linha3  = u"    No planeta, Atreyu encontra Neytiri, o Poderoso, e, ao"
        linha4  = u"passar pela  Forb1dd3n-Z, descobre  uma caverna com ruínas"
        linha5  = u"da cidade de BBS e alguns aliens da raça Boolean que reve-"
        linha6  = u"renciam um while True."
        linha7  = u"    Atreyu  tenta  conquistar o planeta NoBr3ak-IN4 e mos-"
        linha8  = u"trar aos Booleans a beleza  que existe em um break no for."
        linha9  = u"Para que isso aconteça, haverá uma partida  de Damas entre"
        linha10 = u"Atreyu e Neytiri que decidirá quem será o futuro governan-"
        linha11 = u"te do planeta."
        linha12 = u"Assim, fica a dúvida:"
        linha13 = u"-*- Será que teremos break no for?! -*-"

        deslocamento_superior += 85
        self.tela_de_mensagens(linha1, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha1, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha2, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha2, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha3, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha3, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha4, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha4, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha5, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha5, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha6, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha6, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)
        deslocamento_superior += 30
        self.tela_de_mensagens(linha7, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha7, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha8, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha8, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha9, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha9, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha10, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha10, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(linha11, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha11, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 47
        self.tela_de_mensagens(linha12, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(linha12, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 47
        deslocamento_lateral += 70
        deslocamento_lateral_s += 70
        self.tela_de_mensagens(linha13, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, True, False)
        self.tela_de_mensagens(linha13, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, True, False)

        self.tela_de_mensagens(u"Pressione 'ESC' para retornar ao menu", (x, y), fonte, h3, sombra, False, True)
        self.tela_de_mensagens(u"Pressione 'ESC' para retornar ao menu", (x_s, y), fonte, h3, cor_da_fonte, False, True)

        pygame.display.flip()

    # tela ajuda
    def exibir_ajuda(self):
        inicar = pygame.display.set_mode(self.tamanho_tela)
        tela = self.tela
        fundo = pygame.image.load("imagens/regras.png")
        tela.blit(fundo, (0, 0))

        largura, altura = self.tamanho_tela
        x_s, x, y = largura / 2.01, largura / 2, altura - 30
        cor_da_fonte, sombra = (255, 255, 255), (0, 0, 0)
        h1, h2, h3 = 40, 17, 12
        deslocamento_superior, deslocamento_lateral = 10, 35
        deslocamento_lateral_s = 34.653465347
        fonte = "purisa"

        # regras
        self.tela_de_mensagens("Regras", (20 / 1.01, deslocamento_superior), fonte, h1, sombra, True, False)
        self.tela_de_mensagens("Regras", (20, deslocamento_superior), fonte, h1, cor_da_fonte, True, False)

        regra1  = u"1. A pedra (peça comum) anda apenas para frente, uma casa por vez."
        regra2  = u"2. Quando a pedra atinge a oitava linha do tabuleiro, ela é promovida à dama."
        regra3  = u"3. A dama anda para frente e para trás, quantas casas quiser."
        regra4  = u"4. A dama não pode saltar uma peça da mesma cor."
        regra5  = u"5. Duas ou mais peças juntas, na mesma diagonal, não podem ser capturadas."
        regra6  = u"6. A pedra e a dama podem capturar tanto para frente como para trás, uma"
        regra61 = u"   ou mais peças."
        regra7  = u"7. Uma pedra só será coroada se no fim do turno ocupar uma casa de coroação."
        regra8  = u"8. A captura é obrigatória."
        regra9  = u"9. A vitória é obtida se o adversário não possuir mais peças ou jogadas possíveis."

        deslocamento_superior += 55
        self.tela_de_mensagens(regra1, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra1, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra2, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra2, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra3, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra3, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra4, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra4, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra5, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra5, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra6, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra6, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)
        deslocamento_superior += 30
        self.tela_de_mensagens(regra61, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra61, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra7, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra7, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(regra8, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(regra8, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        # como jogar
        deslocamento_superior += 30
        self.tela_de_mensagens("Como Jogar", (20 / 1.01, deslocamento_superior), fonte, h1, (0, 0, 0), True, False)
        self.tela_de_mensagens("Como Jogar", (20, deslocamento_superior), fonte, h1, cor_da_fonte, True, False)

        dica_a = u"Para movimentar uma peça, clique nela e em seguida em uma das casas sugeridas."
        dica_b = u"Caso a casa ficar vermelha, a peça não pode realizar nenhum movimento."
        dica_c = u"Uma peça não pode se mover quando:"
        dica_ca = u"Não há jogadas possíveis;"
        dica_cb = u"Existe alguma captura obrigatória."

        deslocamento_superior += 60
        self.tela_de_mensagens(dica_a, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(dica_a, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 25
        self.tela_de_mensagens(dica_b, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(dica_b, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 30
        self.tela_de_mensagens(dica_c, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, True, False)
        self.tela_de_mensagens(dica_c, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, True, False)

        deslocamento_lateral += 30
        deslocamento_lateral_s += 30
        deslocamento_superior += 30
        self.tela_de_mensagens(dica_ca, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(dica_ca, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        deslocamento_superior += 25
        self.tela_de_mensagens(dica_cb, (deslocamento_lateral_s, deslocamento_superior), fonte, h2, sombra, False, False)
        self.tela_de_mensagens(dica_cb, (deslocamento_lateral, deslocamento_superior), fonte, h2, cor_da_fonte, False, False)

        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x_s, y), fonte, h3, sombra, False, True)
        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x, y), fonte, h3, cor_da_fonte, False, True)

        pygame.display.flip()

    # tela de créditos
    def creditos(self):
        inicar = pygame.display.set_mode(self.tamanho_tela)
        tela = self.tela
        fundo = pygame.image.load("imagens/creditos.png")
        tela.blit(fundo, (0, 0))

        largura, altura = self.tamanho_tela
        x, x_s, y = largura / 2, largura / 2.001, altura - 30
        sombra, cor_da_fonte = (0, 0, 0), (255, 255, 255)
        h1, h2, h3, h4, h5 = 50, 24, 20, 12, 10
        deslocamento_superior, deslocamento_lateral = 90, 60
        deslocamento_lateral_s = 59.3
        fonte = "purisa"

        self.tela_de_mensagens(u"Créditos", (x_s, deslocamento_superior), fonte, h1, sombra)
        self.tela_de_mensagens(u"Créditos", (x, deslocamento_superior), fonte, h1, cor_da_fonte)

        deslocamento_superior += 100
        self.tela_de_mensagens("Siuanny Barbosa", (x_s, deslocamento_superior), fonte, h2, sombra, True, True)
        self.tela_de_mensagens("Siuanny Barbosa", (x, deslocamento_superior), fonte, h2, cor_da_fonte, True, True)

        deslocamento_superior += 30
        self.tela_de_mensagens(u"Miniprojeto de Programação I e Laboratório de Programação I", (x_s, deslocamento_superior), fonte, h3, sombra, False, True)
        self.tela_de_mensagens(u"Miniprojeto de Programação I e Laboratório de Programação I", (x, deslocamento_superior), fonte, h3, cor_da_fonte, False, True)

        deslocamento_superior += 30
        self.tela_de_mensagens(u"2017.2, Ciência da Computação - UFCG", (x_s, deslocamento_superior), fonte, h3, sombra, False, True)
        self.tela_de_mensagens(u"2017.2, Ciência da Computação - UFCG", (x, deslocamento_superior), fonte, h3, cor_da_fonte, False, True)

        deslocamento_lateral -= 7
        deslocamento_lateral_s -= 7
        deslocamento_superior += 162
        self.tela_de_mensagens("Ferramentas utilizadas", (deslocamento_lateral_s, deslocamento_superior), fonte, h5, sombra, True, False)
        self.tela_de_mensagens("Ferramentas utilizadas", (deslocamento_lateral, deslocamento_superior), fonte, h5, (0, 174, 136), True, False)

        deslocamento_lateral += 15
        deslocamento_lateral_s += 15
        deslocamento_superior += 20
        self.tela_de_mensagens("Python 2.7.x (https://www.python.org/)", (deslocamento_lateral_s, deslocamento_superior), fonte, h5, sombra, False, False)
        self.tela_de_mensagens("Python 2.7.x (https://www.python.org/)", (deslocamento_lateral, deslocamento_superior), fonte, h5, cor_da_fonte, False, False)

        deslocamento_superior += 15
        self.tela_de_mensagens("Pygame (http://www.pygame.org/)", (deslocamento_lateral_s, deslocamento_superior), fonte, h5, sombra, False, False)
        self.tela_de_mensagens("Pygame (http://www.pygame.org/)", (deslocamento_lateral, deslocamento_superior), fonte, h5, cor_da_fonte, False, False)

        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x_s, y), fonte, h4, sombra, False)
        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x, y), fonte, h4, (150, 150, 154), False)

        pygame.display.flip()

    # permanência
    def loop(self):
        while True:
            self.clock.tick(30)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit(0)
                elif evento.type == KEYDOWN and (self.escolha == exibir_historia or self.escolha == jogar or self.escolha == manual or self.escolha == FIM or self.escolha == exibir_creditos) and evento.key == K_ESCAPE:
                    self.escolha = exibir_menu
                    self.exibir_menu()

            if self.escolha == exibir_menu:
                left_click, middle_click, right_click = pygame.mouse.get_pressed()

                if left_click:
                    for key in self.opcoes:
                        opt = self.opcoes[key]
                        aparencia, rect = opt
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if key == historia:
                                self.historia()
                                self.escolha = exibir_historia
                            elif key == comecar:
                                self.iniciar_partida()
                                self.escolha = jogar
                            elif key == ajuda:
                                self.exibir_ajuda()
                                self.escolha = manual
                            if key == creditos:
                                self.creditos()
                                self.escolha = exibir_creditos
                            elif key == sair:
                                sys.exit(0)
#                            elif key == FIM:
#                                self.escolha = FIM
#                                self.vencedor("escuras", u"peças")
#                                continue

            elif self.escolha == jogar:
                jogador_atual = self.jogo_de_damas.jogador_atual
                jogo_de_damas = self.jogo_de_damas
                tabuleiro = jogo_de_damas.tabuleiro

                pecas_e = len(jogo_de_damas.obter_pecas(escuras))
                pecas_c = len(jogo_de_damas.obter_pecas(claras))

                movimento_disponivel_e = len(jogo_de_damas.obter_celulas_disponiveis(escuras))
                movimento_disponivel_c = len(jogo_de_damas.obter_celulas_disponiveis(claras))

                reta_final = False

                if pecas_c <= 2 and pecas_e <= 2 and jogo_de_damas.procura_damas(tabuleiro):
                    if not reta_final:
                        total_de_movimentos_no_momento = jogo_de_damas.movimentos_das_claras + jogo_de_damas.movimentos_das_escuras
                        reta_final = True
                        continue
                    elif (jogo_de_damas.movimentos_das_claras + jogo_de_damas.movimentos_das_escuras) - total_de_movimentos_no_momento == 5:
                        self.escolha = FIM
                        self.empate(pecas_c, pecas_e)
                        continue
                elif pecas_c <= 0:
                    self.escolha = FIM
                    self.vencedor("escuras", u"peças")
                    continue
                elif pecas_e <= 0:
                    self.escolha = FIM
                    self.vencedor("claras", u"peças")
                    continue
                elif jogo_de_damas.jogador_atual == claras and movimento_disponivel_c <= 0:
                    self.escolha = FIM
                    self.vencedor("escuras", "jogadas")
                    continue
                elif jogo_de_damas.jogador_atual == escuras and movimento_disponivel_e <= 0:
                    self.escolha = FIM
                    self.vencedor("claras", "jogadas")
                    continue

                left_click = pygame.mouse.get_pressed()

                if left_click:
                    pos = pygame.mouse.get_pos()
                    jogo_de_damas = self.jogo_de_damas
                    tabuleiro = self.jogo_de_damas.tabuleiro

                    for l in range(len(tabuleiro)):
                        for c in range(len(tabuleiro[l])):
                            celula = tabuleiro[l][c]
                            if celula.rect.collidepoint(pos):
                                if celula.tem_peca():
                                    movimento_disponivel_c = len(jogo_de_damas.obter_celulas_disponiveis())
                                    jogo_de_damas.celula_selecionada(celula)
                                elif not celula.tem_peca() and jogo_de_damas.selecionada:
                                    if jogo_de_damas.pode_mover(jogo_de_damas.selecionada, celula):
                                        jogo_de_damas.movimento(celula)
                                break
                self.renderizar(self.tela)

            elif self.escolha == FIM:
                left_click, middle_click, right_click = pygame.mouse.get_pressed()

                if left_click:
                    for key in self.opcoes:
                        opt = self.opcoes[key]
                        aparencia, rect = opt
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if key == jogar_novamente:
                                self.iniciar_partida()
                                self.escolha = jogar

    # renderização (renderiza o jogo a cada iteração do game.loop)
    def renderizar(self, tela):
        inicar = pygame.display.set_mode(self.tamanho_tela)
        tela = self.tela
        fundo = pygame.image.load("imagens/superior.png")
        tela.blit(fundo, (0, 0))

        largura, altura = self.tamanho_tela
        jogador_atual = self.jogo_de_damas.jogador_atual
        jogo_de_damas = self.jogo_de_damas
        srt_jogador = '>' if jogador_atual == escuras else '<'
        color = (229, 247, 243)
        fonte = "purisa"

        lateral_esquerda = pygame.Surface([deslocamento_coluna * tamanho_casas, altura - (2 * tamanho_casas * deslocamento_linha)])
        fundo = pygame.image.load("imagens/atreyu.png")
        lateral_esquerda.blit(fundo, (0, 0))
        self.tela.blit(lateral_esquerda, (0, tamanho_casas * deslocamento_linha))

        lateral_direita = pygame.Surface([deslocamento_coluna * tamanho_casas, altura - (2 * tamanho_casas * deslocamento_linha)])
        fundo = pygame.image.load("imagens/neytiri.png")
        lateral_direita.blit(fundo, (0, 0))
        self.tela.blit(lateral_direita, (largura - deslocamento_coluna * tamanho_casas, tamanho_casas * deslocamento_linha))

        self.tela_de_mensagens("Atreyu %s Neytiri" % srt_jogador, (largura / 2.01, 30), fonte, 25, (0, 0, 0), True)
        self.tela_de_mensagens("Atreyu %s Neytiri" % srt_jogador, (largura / 2, 30), fonte, 25, color, True)

        self.tela_de_mensagens("Atreyu (claras)", (10, (altura / 2) - tamanho_casas / 2), fonte, 15, color, True, False)
        self.tela_de_mensagens(u"Peças em jogo: %d" % len(jogo_de_damas.obter_pecas(claras)), (25, altura / 2), fonte, 10, color, True, False)
        self.tela_de_mensagens("Jogadas: %d" % jogo_de_damas.movimentos_das_claras, (25, (altura / 2) + 20), fonte, 10, color, True, False)

        self.tela_de_mensagens("Neytiri (escuras)", (tamanho_casas * 11 + 10, (altura / 2) - tamanho_casas / 2), fonte, 15, color, True, False)
        self.tela_de_mensagens(u"Peças em jogo: %d" % len(jogo_de_damas.obter_pecas(escuras)), (tamanho_casas * 11 + 25, altura / 2), fonte, 10, color, True, False)
        self.tela_de_mensagens("Jogadas: %d" % jogo_de_damas.movimentos_das_escuras, (tamanho_casas * 11 + 25, (altura / 2) + 20), fonte, 10, color, True, False)

        self.jogo_de_damas.renderizar()

        pygame.display.flip()

    # apresenta a tela informando qual jogador foi o vencedor da partida
    def vencedor(self, vencedor, motivo):
        tela = self.tela
        inicar = pygame.display.set_mode(self.tamanho_tela)
        fundo = pygame.image.load("imagens/vencedor.png")
        tela.blit(fundo, (0, -50))

        largura, altura = self.tamanho_tela
        x, x_s, y = largura / 2 + 5, largura / 2.001 + 5, altura - 30
        h1, h2, h3, h4, h5 = 35, 30, 20, 12, 9
        deslocamento_superior = 230
        fonte = "purisa"
        sombra, cor_da_fonte = (0, 0, 0), (53, 145, 148) if vencedor == "claras" else (164, 10, 105)

        alien = "Atreyu" if vencedor == "claras" else "Neytiri"
        oponente = "Neytiri" if vencedor == "claras" else "Atreyu"

        self.tela_de_mensagens("Fim de jogo", (x_s, deslocamento_superior), fonte, h1, sombra, True)
        self.tela_de_mensagens("Fim de jogo", (x, deslocamento_superior), fonte, h1, cor_da_fonte, True)

        deslocamento_superior += 45
        self.tela_de_mensagens("%s venceu!" % alien, (x_s, deslocamento_superior), fonte, h3, sombra, True)
        self.tela_de_mensagens("%s venceu!" % alien, (x, deslocamento_superior), fonte, h3, cor_da_fonte, True)

        deslocamento_superior += 30
        self.tela_de_mensagens(u"%s não possui mais %s!" % (oponente, motivo), (x_s, deslocamento_superior), fonte, h3, sombra, True)
        self.tela_de_mensagens(u"%s não possui mais %s!" % (oponente, motivo), (x, deslocamento_superior), fonte, h3, cor_da_fonte, True)

        deslocamento_superior += 40
        msg = self.tela_de_mensagens("Clique aqui para Jogar Novamente", (x_s, deslocamento_superior), fonte, h4, cor_da_fonte, True)
        self.opcoes[jogar_novamente] = msg

        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x_s, y), fonte, h5, sombra, True)

        pygame.display.flip()

    # apresenta a tela informando qual jogador foi o vencedor da partida
    def empate(self, qnt_c, qnt_e):
        tela = self.tela
        inicar = pygame.display.set_mode(self.tamanho_tela)
        fundo = pygame.image.load("imagens/vencedor.png")
        tela.blit(fundo, (0, -50))

        largura, altura = self.tamanho_tela
        x, x_s, y = largura / 2 + 5, largura / 2.001 + 5, altura - 30
        h1, h2, h3, h4, h5 = 35, 30, 20, 12, 9
        deslocamento_superior = 230
        fonte = "purisa"
        sombra, cor_da_fonte = (0, 0, 0), (0, 44, 50)

        self.tela_de_mensagens("Empate!", (x_s, deslocamento_superior), fonte, h1, sombra, True)
        self.tela_de_mensagens("Empate!", (x, deslocamento_superior), fonte, h1, cor_da_fonte, True)

        deslocamento_superior += 45
        self.tela_de_mensagens(u"Atreyu possui %i peças!" % qnt_c, (x_s, deslocamento_superior), fonte, h3, sombra, True)
        self.tela_de_mensagens(u"Atreyu possui %i peças!" % qnt_c, (x, deslocamento_superior), fonte, h3, cor_da_fonte, True)

        deslocamento_superior += 30
        self.tela_de_mensagens(u"Neytiri possui %i peças!" % qnt_e, (x_s, deslocamento_superior), fonte, h3, sombra, True)
        self.tela_de_mensagens(u"Neytiri possui %i peças!" % qnt_e, (x, deslocamento_superior), fonte, h3, cor_da_fonte, True)

        deslocamento_superior += 40
        msg = self.tela_de_mensagens("Clique aqui para Jogar Novamente", (x_s, deslocamento_superior), fonte, h4, cor_da_fonte, True)
        self.opcoes[jogar_novamente] = msg

        self.tela_de_mensagens("Pressione 'ESC' para retornar ao menu", (x_s, y), fonte, h5, sombra, True)

        pygame.display.flip()
