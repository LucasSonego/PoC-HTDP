#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Personagem:
x e y = posição do personagem na tela
dx e dy = a Variação de x e y
posi = LEFT / RIGHT / UP / DOWN (direção)
'''
Personagem = definir_estrutura("Personagem", "x, y, dx, dy, direcao")
PERSONAGEM_L0 = Personagem(350,600,0,0,1)
PERSONAGEM_L1 = Personagem(350,600,0,0,1)
PERSONAGEM_L2 =
PERSONAGEM_L3 =
PERSONAGEM_L4 =
PERSONAGEM_L5 =

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
INIMIGO_L1 = [Inimigo(500,500,0,0), Inimigo(650,350,0,0), Inimigo(150,150,0,0),Inimigo(100,320,0,0),Inimigo(500,100,0,0)]
INIMIGO_L2 =
INIMIGO_L3 =
INIMIGO_L4 =
INIMIGO_L5 =


'''Jogo:
contem as estruturas Personagem e Tiro
'''
Jogo = definir_estrutura("Jogo","personagem, tiros, inimigo, game_over, cont")
JOGO_L0 = Jogo(PERSONAGEM_L0, TIRO_INICIAL, INIMIGO_L0, False, 0)
JOGO_L1 = Jogo(PERSONAGEM_L1, TIRO_INICIAL, INIMIGO_L1, False, 1)
JOGO_L2 = Jogo(PERSONAGEM_L2, TIRO_INICIAL, INIMIGO_L2, False, 2)
JOGO_L3 = Jogo(PERSONAGEM_L3, TIRO_INICIAL, INIMIGO_L3, False, 3)
JOGO_L4 = Jogo(PERSONAGEM_L4, TIRO_INICIAL, INIMIGO_L4, False, 4)
JOGO_L5 = Jogo(PERSONAGEM_L5, TIRO_INICIAL, INIMIGO_L5, False, 5)


Porta = definir_estrutura("Porta", "x, y")
'''Porta eh formado por um x[LIMITE_ESQUERDO, LIMITE_DIREITO]'''
PORTA_L0 = Porta(600, 300)
PORTA_L1 = Porta(650, 350)
PORTA_L2 =
PORTA_L3 =
PORTA_L4 =
PORTA_L5 = Porta(800, 800)

LAYOUT = [JOGO_L0, JOGO_L1, JOGO_L2, JOGO_L3, JOGO_L4, JOGO_L5]
PORTAS = [PORTA_L0, PORTA_L1, PORTA_L2, PORTA_L3, PORTA_L4, PORTA_L5]

