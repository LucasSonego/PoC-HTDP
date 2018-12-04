#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Personagem:
x e y = posição do personagem na tela
dx e dy = a Variação de x e y
posi = LEFT / RIGHT / UP / DOWN (direção)
'''
Personagem = definir_estrutura("Personagem", "x, y, dx, dy, direcao")
PERSONAGEM_L0 = Personagem(100, 350, 0, 0, 4)
PERSONAGEM_L1 = Personagem(100, 350, 0, 0, 4)
PERSONAGEM_L2 = Personagem(350, 600, 0, 0, 1)
PERSONAGEM_L3 = Personagem(100, 350, 0, 0, 4)
PERSONAGEM_L4 = Personagem(100, 350, 0, 0, 4)
PERSONAGEM_L5 = Personagem(350, 100, 0 , 0, 3)
PERSONAGEM_L6 = Personagem(1200,1200,0 ,0 , 1)

'''Tiro:
x e y = posição do tiro na tela
direcao = LEFT / RIGHT / UP / DOWN (direção)
'''
Tiro = definir_estrutura("Tiro", "x, y, direcao")
TIRO_INICIAL = []

'''Inimigo
x e y = posição na tela
dx , dy = variação de x e y
direcao = LEFT / RIGHT
'''
Inimigo = definir_estrutura("Inimigo", "x, y, dx, dy")
INIMIGO_L0 = []

INIMIGO_L1 =   [Inimigo(316,171,0,0),
                Inimigo(576,381,0,0),
                Inimigo(269,572,0,0)]

INIMIGO_L2 =   [Inimigo(123,436,0,0),
                Inimigo(146,174,0,0),
                Inimigo(356,203,0,0),
                Inimigo(562,148,0,0),
                Inimigo(542,383,0,0),]

INIMIGO_L3 =   [Inimigo(333,145,0,0),
                Inimigo(535,175,0,0),
                Inimigo(588,350,0,0),
                Inimigo(506,544,0,0),
                Inimigo(254,570,0,0)]

INIMIGO_L4 =   [Inimigo(161,125,0,0),
                Inimigo(565,112,0,0),
                Inimigo(532,397,0,0),
                Inimigo(563,612,0,0),
                Inimigo(317,551,0,0),
                Inimigo(152,613,0,0)]

INIMIGO_L5 =   [Inimigo(73,356,0,0),
                Inimigo(214,371,0,0),
                Inimigo(84,513,0,0),
                Inimigo(173,517,0,0),
                Inimigo(196,613,0,0),
                Inimigo(473,617,0,0),
                Inimigo(617,594,0,0),
                Inimigo(490,487,0,0),
                Inimigo(622,416,0,0),
                Inimigo(519,346,0,0),
                Inimigo(599,251,0,0)]

INIMIGO_L6 = []

'''Jogo:
contem as estruturas Personagem e Tiro
'''
Jogo = definir_estrutura("Jogo","personagem, tiros, inimigos, game_over, layout")
JOGO_L0 = Jogo(PERSONAGEM_L0, TIRO_INICIAL, INIMIGO_L0, False, 0)
JOGO_L1 = Jogo(PERSONAGEM_L1, TIRO_INICIAL, INIMIGO_L1, False, 1)
JOGO_L2 = Jogo(PERSONAGEM_L2, TIRO_INICIAL, INIMIGO_L2, False, 2)
JOGO_L3 = Jogo(PERSONAGEM_L3, TIRO_INICIAL, INIMIGO_L3, False, 3)
JOGO_L4 = Jogo(PERSONAGEM_L4, TIRO_INICIAL, INIMIGO_L4, False, 4)
JOGO_L5 = Jogo(PERSONAGEM_L5, TIRO_INICIAL, INIMIGO_L5, False, 5)
JOGO_L6 = Jogo(PERSONAGEM_L6, TIRO_INICIAL, INIMIGO_L6, False, 6)


Porta = definir_estrutura("Porta", "x, y")
'''Porta eh formado por um x[LIMITE_ESQUERDO, LIMITE_DIREITO]'''
PORTA_L0 = Porta(600, 300)
PORTA_L1 = Porta(300, 80)
PORTA_L2 = Porta(600, 300)
PORTA_L3 = Porta(600, 300)
PORTA_L4 = Porta(300, 620)
PORTA_L5 = Porta(350, 550)
PORTA_L6 = Porta(1000,1000)


LAYOUT = [JOGO_L0, JOGO_L1, JOGO_L2, JOGO_L3, JOGO_L4, JOGO_L5, JOGO_L6]
PORTAS = [PORTA_L0, PORTA_L1, PORTA_L2, PORTA_L3, PORTA_L4, PORTA_L5, PORTA_L6]

