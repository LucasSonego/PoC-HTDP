#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Personagem:
x e y = posição do personagem na tela
dx e dy = a Variação de x e y
posi = LEFT / RIGHT / UP / DOWN (direção)
'''
Personagem = definir_estrutura("Personagem", "x, y, dx, dy, direcao")
PERSONAGEM_INICIAL = Personagem(100,100,0,0,0)

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
INIMIGO_INICIAL = Inimigo(600,600,0,0)

'''Jogo:
contem as estruturas Personagem e Tiro
'''
Jogo = definir_estrutura("Jogo","personagem, tiros, inimigo, game_over")
JOGO_INICIAL = Jogo(PERSONAGEM_INICIAL,TIRO_INICIAL,INIMIGO_INICIAL, False)


