#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

'''Tela'''

ALTURA = 700
LARGURA = 700
tela = criar_tela_base(LARGURA,ALTURA)

'''Imagens'''
FUNDO = carregar_imagem('./Imagens/mapa.png')
FANTASMA = carregar_imagem('./Imagens/fantasma.png')
PASSARALHO = carregar_imagem('./Imagens/passaralho.png')
TIRO = carregar_imagem('./Imagens/naosei.png')

FUNDO = definir_dimensoes(FUNDO,LARGURA,ALTURA)
FANTASMA = definir_dimensoes(FANTASMA,55,80)
PASSARALHO = definir_dimensoes(PASSARALHO,80,80)
TIRO = definir_dimensoes(TIRO,60,14)

tela = colocar_imagem(FUNDO,tela,LARGURA//2,ALTURA//2)
tela = colocar_imagem(FANTASMA,tela,100,200)
tela = colocar_imagem(TIRO,tela,400,200)
tela = colocar_imagem(PASSARALHO,tela,600,200)

colocar_imagem_sobre_tela_e_mostrar(tela,LARGURA//2,ALTURA//2)
