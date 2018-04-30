# -*- coding: utf-8 -*-
# aluna: siuanny.rocha (117210395)
# atividade: damas (unidade 11 - Miniprojeto 1)
# 2017.2, programação 1 - ufcg

# imports
import sys
import Const
import pygame
from pygame.locals import *

class Peca:

    # inicialização
    def __init__(self, jogador, eh_dama = False):
        self.jogador = jogador
        self.eh_dama = eh_dama
