#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Personagem:
x e y = posição do personagem na tela
dx e dy = a Variação de x e y
posi = LEFT / RIGHT / UP / DOWN (direção)
'''
Personagem = definir_estrutura("Personagem", "x, y, dx, dy, posi")

'''Tiro:
x e y = posição do tiro na tela
posi = LEFT / RIGHT / UP / DOWN (direção)
'''
Tiro = definir_estrutura("Tiro", "x, y, posi")

'''Jogo:
contem as estruturas Personagem e Tiro
'''
Jogo = definir_estrutura("Jogo","Personagem, Tiro")

