
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *


PosicaoMouse = definir_estrutura("PosicaoMouse","x,y")
MOUSE_INICIAL = PosicaoMouse(0,0)

RISCO_V = retangulo(LARGURA*2,1,Cor('red'))
RISCO_H = retangulo(1,LARGURA*2,Cor('red'))


STRX = "X "
STRY = "Y "


'''Imagens soltas na tela'''



def desenha(mouse):
    stringx = STRX + str(mouse.x)
    img_textox = texto((str(stringx)), Fonte("arial black", 20), Cor("green"))
    stringy = STRY + str(mouse.y)
    img_textoy = texto((str(stringy)), Fonte("arial black", 20), Cor("green"))
    img_texto = encima(img_textox,img_textoy)
    tela = criar_tela_base(LARGURA, ALTURA)

    '''coloque aqui as imagens'''
    tela = colocar_imagem(IMG_LAYOUT_1, tela, LARGURA // 2, ALTURA // 2)
    # tela = colocar_imagem(PERSONAGEM_LEFT, tela, 100, 100)
    # tela = colocar_imagem(PERSONAGEM_RIGHT, tela, 100, 200)
    # tela = colocar_imagem(PERSONAGEM_UP, tela, 100, 300)
    # tela = colocar_imagem(PERSONAGEM_DOWN, tela, 100, 400)
    #
    # tela = colocar_imagem(TIRO_LEFT, tela, 200, 100)
    # tela = colocar_imagem(TIRO_RIGHT, tela, 200, 200)
    # tela = colocar_imagem(TIRO_UP, tela, 200, 300)
    # tela = colocar_imagem(TIRO_DOWN, tela, 200, 400)
    #
    # tela = colocar_imagem(INIMIGO_LEFT, tela, 300, 100)
    # tela = colocar_imagem(INIMIGO_RIGHT, tela, 300, 200)

    tela = colocar_imagem(RISCO_V, tela, mouse.x, mouse.y)
    tela = colocar_imagem(RISCO_H, tela, mouse.x, mouse.y)

    tela = colocar_imagem(img_texto,tela,largura_imagem(img_texto),altura_imagem(img_texto))



def mouse(mouse,x,y,ev):
    if ev == pg.MOUSEBUTTONDOWN:
        print("Inimigo(%d,%d,0,0),"%(x,y))

    if ev == pg.MOUSEMOTION:
        return PosicaoMouse(x,y)
    #else
    return PosicaoMouse(mouse.x,mouse.y)



def main(inic):
    big_bang(inic,
             desenhar=desenha, #Mundo -> imagem
             quando_mouse=mouse,  #Mundo, mouse -> Mundo
             )

main(MOUSE_INICIAL)

