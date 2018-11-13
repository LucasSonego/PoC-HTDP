
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *

'''Imagens'''

tela = colocar_imagem(IMG_LAYOUT_1,tela,LARGURA//2,ALTURA//2)
tela = colocar_imagem(PERSONAGEM_LEFT,tela,100,100)
tela = colocar_imagem(PERSONAGEM_RIGHT,tela,100,200)
tela = colocar_imagem(PERSONAGEM_UP,tela,100,300)
tela = colocar_imagem(PERSONAGEM_DOWN,tela,100,400)

tela = colocar_imagem(TIRO_LEFT,tela,200,100)
tela = colocar_imagem(TIRO_RIGHT,tela,200,200)
tela = colocar_imagem(TIRO_UP,tela,200,300)
tela = colocar_imagem(TIRO_DOWN,tela,200,400)

tela = colocar_imagem(INIMIGO_LEFT,tela,300,100)
tela = colocar_imagem(INIMIGO_RIGHT,tela,300,200)


colocar_imagem_sobre_tela_e_mostrar(tela,LARGURA//2,ALTURA//2)
