#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *


'''# Preparacao da Tela'''
(LARGURA, ALTURA) = (700, 700)
tela = criar_tela_base(LARGURA, ALTURA)


'''Imagens'''

#layouts
IMG_LAYOUT_1 = carregar_imagem('./Imagens/layout1.png')
IMG_LAYOUT_1 = definir_dimensoes(IMG_LAYOUT_1,LARGURA,ALTURA)

#personagem
PERSONAGEM_BASE = carregar_imagem('./Imagens/fantasma_lado.png')
PERSONAGEM_BASE = definir_dimensoes(PERSONAGEM_BASE, 55, 80)

PERSONAGEM_LEFT = espelhar(PERSONAGEM_BASE, True, False)

PERSONAGEM_RIGHT = PERSONAGEM_BASE

PERSONAGEM_UP = carregar_imagem('./Imagens/fantasma_costas.png')
PERSONAGEM_UP = definir_dimensoes(PERSONAGEM_UP, 55, 80)

PERSONAGEM_DOWN = carregar_imagem('./Imagens/fantasma_frente.png')
PERSONAGEM_DOWN = definir_dimensoes(PERSONAGEM_DOWN, 55, 80)

PERSONAGEM_ALTURA = altura_imagem(PERSONAGEM_BASE)
PERSONAGEM_LARGURA = largura_imagem(PERSONAGEM_BASE)


#inimigo
INIMIGO = carregar_imagem('./Imagens/passaralho.png')
INIMIGO = definir_dimensoes(INIMIGO, 80, 80)
INIMIGO_RIGHT = espelhar(INIMIGO,True,False)
INIMIGO_LEFT = INIMIGO

#tiro
TIRO = carregar_imagem('./Imagens/tiro.png')
TIRO = definir_dimensoes(TIRO,60,14)
TIRO_LEFT = espelhar(TIRO,True,False)
TIRO_RIGHT = TIRO
TIRO_UP = girar(TIRO,90)
TIRO_DOWN = girar(TIRO,-90)


'''Constantes'''

LIMITE_ESQUERDO = 50 + (PERSONAGEM_LARGURA // 2)
LIMITE_DIREITO = LARGURA-50 - (PERSONAGEM_LARGURA //2)
LIMITE_CIMA = 50 + (PERSONAGEM_ALTURA //2)
LIMITE_BAIXO = ALTURA-50 - (PERSONAGEM_ALTURA // 2)

VEL_PERSONAGEM = 5
VEL_TIRO = 10
