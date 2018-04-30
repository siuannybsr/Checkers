# -*- coding: utf-8 -*-
# aluna: siuanny.rocha (117210395)
# atividade: damas (unidade 11 - Miniprojeto 1)
# 2017.2, programação 1 - ufcg

# variáveis que irão permanecer constantes
historia, comecar, ajuda, creditos, sair, jogar_novamente = 1, 2, 3, 4, 5, 6
exibir_menu, exibir_historia, jogar, manual, exibir_creditos, FIM = 1, 2, 3, 4, 5, 6
escuras, damas_escuras, claras, damas_claras, dama = 'e', 'E', 'c', 'C', 'D'
bloqueado, livre = 'X', ' '
sugerido, disponivel, nao_disponivel = 's', 'd', 'nd'
tamanho_casas, tamanho_circulos = 60, 25
deslocamento_linha, deslocamento_coluna = 1, 3
total_de_pecas_no_momento = 0
reta_final = False

direcao = {
             escuras:  1,
             claras: -1
}

cores = {
           escuras:        [(228,  38, 146), (164,  10, 105)],
           claras:         [(141, 204, 173), ( 53, 145, 148)],
           bloqueado:       (197, 207, 198),
           livre:           ( 44,  26,  86),
           sugerido:        ( 32,  72,  56),
           nao_disponivel:  (221,  17,  34),
           disponivel:      ( 32,  72,  56)
}


# função de apoio 1
def eh_casa_valida(l, c):
    return (l % 2 == 0 and c % 2 != 0) or (l % 2 != 0 and c % 2 == 0)


# função de apoio 2
def capturar(jogador):
    return claras if jogador == escuras else escuras
