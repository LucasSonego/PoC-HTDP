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
LARGURA_PERSONAGEM = 55
ALTURA_PERSONAGEM = 80

M_LARGURA_PERSONAGEM = LARGURA_PERSONAGEM//2
M_ALTURA_PERSONAGEM = ALTURA_PERSONAGEM//2

PERSONAGEM_BASE = carregar_imagem('./Imagens/fantasma_lado.png')
PERSONAGEM_BASE = definir_dimensoes(PERSONAGEM_BASE, LARGURA_PERSONAGEM, ALTURA_PERSONAGEM)

PERSONAGEM_LEFT = espelhar(PERSONAGEM_BASE, True, False)

PERSONAGEM_RIGHT = PERSONAGEM_BASE

PERSONAGEM_UP = carregar_imagem('./Imagens/fantasma_costas.png')
PERSONAGEM_UP = definir_dimensoes(PERSONAGEM_UP, LARGURA_PERSONAGEM, ALTURA_PERSONAGEM)

PERSONAGEM_DOWN = carregar_imagem('./Imagens/fantasma_frente.png')
PERSONAGEM_DOWN = definir_dimensoes(PERSONAGEM_DOWN, LARGURA_PERSONAGEM, ALTURA_PERSONAGEM)


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


'''Outras constantes'''
#layout 1
L1_LIMITE_MEIO_ESQ = 250 - M_LARGURA_PERSONAGEM
L1_LIMITE_MEIO_DIR = 460 + M_LARGURA_PERSONAGEM
L1_LIMITE_MEIO_CIMA = 250 - M_ALTURA_PERSONAGEM
L1_LIMITE_MEIO_BAIXO = 460 + M_ALTURA_PERSONAGEM

L1_LIMITE_ESQUERDO = 55 + M_LARGURA_PERSONAGEM
L1_LIMITE_DIREITO = LARGURA - 55 - M_LARGURA_PERSONAGEM
L1_LIMITE_CIMA = 55 + M_ALTURA_PERSONAGEM
L1_LIMITE_BAIXO = ALTURA - 55 - M_ALTURA_PERSONAGEM


FREQUENCIA = 50
VEL_PERSONAGEM = 5
VEL_TIRO = 10
