#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
from def_dados import *


def mover_perso(per):
    posicao_x = per.x + per.dx
    posicao_y = per.y + per.dy
    if posicao_x > LIMITE_DIREITO or posicao_x < LIMITE_ESQUERDO:
        return Personagem(per.x, per.y, per.dx, per.dy, per.posi)
    if posicao_y < LIMITE_CIMA or posicao_y > LIMITE_BAIXO:
        return Personagem(per.x, per.y, per.dx, per.dy, per.posi)
    return Personagem(posicao_x, posicao_y, per.dx, per.dy, per.posi)

def mover_tiro(pow):
    if pow.posi == 1:
        novo = pow.y - VEL_TIRO
        return Tiro(pow.x, novo, pow.posi)
    if pow.posi == 2:
        novo = pow.x - VEL_TIRO
        return Tiro(novo, pow.y, pow.posi)
    if pow.posi == 3:
        novo = pow.y + VEL_TIRO
        return Tiro(pow.x, novo, pow.posi)
    if pow.posi == 4:
        novo = pow.x + VEL_TIRO
        return Tiro(novo, pow.y, pow.posi)
    return pow


def mover_jogo(jogo):
    per=mover_perso(jogo.Personagem)
    tir=mover_tiro(jogo.Tiro)
    return Jogo(per, tir)
'''
desenha: Personagem -> Imagem
Desenha...'''

#TODO
''' criar 'if' para direção do tiro , perosnagem e inimigo '''

def desenha(per):
    colocar_imagem(IMG_LAYOUT_1,tela,LARGURA//2,ALTURA//2)
    if per.posi == 1:
        colocar_imagem(PERSONAGEM_UP, tela, per.x, per.y)
    elif per.posi == 2:
        colocar_imagem(PERSONAGEM_LEFT, tela, per.x, per.y)
    elif per.posi == 3:
        colocar_imagem(PERSONAGEM_DOWN, tela, per.x, per.y)
    elif per.posi == 4:
        colocar_imagem(PERSONAGEM_RIGHT, tela, per.x, per.y)
    else:
        colocar_imagem(PERSONAGEM_DOWN,tela,per.x,per.y)


def desenha_tiro(pow):
    if pow.posi == 1:
        colocar_imagem(TIRO_UP, tela, pow.x, pow.y)
    if pow.posi == 2:
        colocar_imagem(TIRO_LEFT, tela, pow.x, pow.y)
    if pow.posi == 3:
        colocar_imagem(TIRO_DOWN, tela, pow.x, pow.y)
    if pow.posi == 4:
        colocar_imagem(TIRO_RIGHT, tela, pow.x, pow.y)


def desenha_jogo(jogo):
    desenha(jogo.Personagem)
    desenha_tiro(jogo.Tiro)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_tecla(per, tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, 0, -VEL_PERSONAGEM, 1)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, -VEL_PERSONAGEM, 0, 2)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, 0, VEL_PERSONAGEM, 3)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, VEL_PERSONAGEM, 0, 4)
    return per

def trata_tecla_tiro(jog, tecla):
    if tecla == pg.K_SPACE:
        tiro_x=jog.Personagem.x
        tiro_y=jog.Personagem.y
        return Tiro(tiro_x, tiro_y, jog.Personagem.posi)
    #else
    return jog.Tiro

def trata_tecla_jogo(jogo, tecla):
    per = trata_tecla(jogo.Personagem, tecla)
    tir = trata_tecla_tiro(jogo, tecla)
    return Jogo(per, tir)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_solta(per,tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, per.dx, 0, per.posi)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, 0, per.dy, per.posi)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, per.dx, 0, per.posi)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, 0, per.dy, per.posi)
    return per

def trata_solta_tiro(tiro, tecla):
    if tecla==pg.K_SPACE:
        return tiro
    return tiro

def trata_tecla_solta_jogo(jogo, tecla):
    per=trata_solta(jogo.Personagem, tecla)
    tir=trata_solta_tiro(jogo.Tiro, tecla)
    return Jogo(per, tir)