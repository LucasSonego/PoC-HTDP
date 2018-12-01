#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *


'''# Preparacao da Tela'''
(LARGURA, ALTURA) = (700, 700)
tela = criar_tela_base(LARGURA, ALTURA)


'''Imagens'''

#layouts
IMG_LAYOUT_0 = carregar_imagem('./Imagens/layout1.png')
IMG_LAYOUT_0 = definir_dimensoes(IMG_LAYOUT_0,LARGURA,ALTURA)
IMG_LAYOUT_1 = carregar_imagem('./Imagens/layout2.png')
IMG_LAYOUT_1 = definir_dimensoes(IMG_LAYOUT_1,LARGURA,ALTURA)
IMG_LAYOUT_2 = carregar_imagem('./Imagens/layout3.png')
IMG_LAYOUT_2 = definir_dimensoes(IMG_LAYOUT_2,LARGURA,ALTURA)
IMG_LAYOUT_3 = carregar_imagem('./Imagens/layout4.png')
IMG_LAYOUT_3 = definir_dimensoes(IMG_LAYOUT_3,LARGURA,ALTURA)
IMG_LAYOUT_4 = carregar_imagem('./Imagens/layout5.png')
IMG_LAYOUT_4 = definir_dimensoes(IMG_LAYOUT_4,LARGURA,ALTURA)
IMG_LAYOUT_5 = carregar_imagem('./Imagens/layout6.png')
IMG_LAYOUT_5 = definir_dimensoes(IMG_LAYOUT_5,LARGURA,ALTURA)

IMGS = [IMG_LAYOUT_0, IMG_LAYOUT_1, IMG_LAYOUT_2, IMG_LAYOUT_3, IMG_LAYOUT_4, IMG_LAYOUT_5]

#personagem
LARGURA_PERSONAGEM = 40
ALTURA_PERSONAGEM = 60

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
LARGURA_INIMIGO = 55
ALTURA_INIMIGO = 55
INIMIGO = carregar_imagem('./Imagens/passaralho.png')
INIMIGO = definir_dimensoes(INIMIGO, LARGURA_INIMIGO, ALTURA_INIMIGO)
INIMIGO_RIGHT = espelhar(INIMIGO,True,False)
INIMIGO_LEFT = INIMIGO

#tiro
TIRO = carregar_imagem('./Imagens/tiro.png')
TIRO = definir_dimensoes(TIRO,40,9)
TIRO_LEFT = espelhar(TIRO,True,False)
TIRO_RIGHT = TIRO
TIRO_UP = girar(TIRO,90)
TIRO_DOWN = girar(TIRO,-90)
LARGURA_TIRO = largura_imagem(TIRO)
ALTURA_TIRO = altura_imagem(TIRO)

'''Outras constantes'''
#layout 1
LIMITE_MEIO_ESQ = 240
LIMITE_MEIO_DIR = 460
LIMITE_MEIO_CIMA = 240
LIMITE_MEIO_BAIXO = 460

LIMITE_ESQUERDO = 55
LIMITE_DIREITO = LARGURA - 55
LIMITE_CIMA = 55
LIMITE_BAIXO = ALTURA - 55


FREQUENCIA = 50
VEL_PERSONAGEM = 4
VEL_TIRO = 10
VEL_INIMIGO = 2