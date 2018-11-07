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
    per=mover_perso(jogo.personagem)
    tir=mover_tiro(jogo.tiro)
    return Jogo(per, tir)
'''
desenha: Personagem -> Imagem
Desenha...'''

#TODO
''' criar 'if' para direção do tiro , perosnagem e inimigo '''

def desenha(per):
    colocar_imagem(IMG_LAYOUT_1,tela,LARGURA//2,ALTURA//2)
    colocar_imagem(PERSONAGEM, tela, per.x, per.y)

def desenha_tiro(pow):
    colocar_imagem(TIRO, tela, pow.x, pow.y)

def desenha_jogo(jogo):
    desenha(jogo.personagem)
    desenha_tiro(jogo.tiro)

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

def trata_tecla_tiro(pow, tecla):
    if tecla == pg.K_SPACE:
        return Tiro(pow.x, pow.y, pow.posi)
    return pow


def trata_tecla_jogo(jogo, tecla):
    xips = trata_tecla(jogo.personagem, tecla)
    tir=trata_tecla_tiro(Tiro(jogo.personagem.x, jogo.personagem.y, jogo.personagem.posi), tecla)
    return Jogo(xips, tir)

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

def trata_solta_tiro(pow, tecla):
    if tecla==pg.K_SPACE:
        return pow
    return pow

def trata_tecla_solta_jogo(jogo, tecla):
    xops=trata_solta(jogo.personagem, tecla)
    tir=trata_solta_tiro(jogo.tiro, tecla)
    return Jogo(xops, tir)

''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ... '''
def main(inic):
    big_bang(inic, tela=tela, frequencia=50, a_cada_tick=mover_jogo,desenhar=desenha_jogo, quando_tecla=trata_tecla_jogo,quando_solta_tecla=trata_tecla_solta_jogo, modo_debug=True)

main(Jogo(Personagem(100, 100, 0, 0, 0), Tiro(100,100,0)))