#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
from def_dados import *


def mover_perso(per):
    '''
    função responsavel por mover o personagem na tela
    :param per: jogo.Personagem
    :return: Personagem
    '''
    posicao_x = per.x + per.dx
    posicao_y = per.y + per.dy
    if posicao_x > L1_LIMITE_DIREITO or posicao_x < L1_LIMITE_ESQUERDO:
        return Personagem(per.x, per.y, per.dx, per.dy, per.direcao)
    if posicao_y < L1_LIMITE_CIMA or posicao_y > L1_LIMITE_BAIXO:
        return Personagem(per.x, per.y, per.dx, per.dy, per.direcao)
    return Personagem(posicao_x, posicao_y, per.dx, per.dy, per.direcao)

def mover_tiro(tir):
    '''
    funçao responsavel por mover os tiros na tela
    :param tir: jogo.Tiro
    :return: Tiro
    '''
    if tir.direcao == 1:
        novo = tir.y - VEL_TIRO
        return Tiro(tir.x, novo, tir.direcao)
    if tir.direcao == 2:
        novo = tir.x - VEL_TIRO
        return Tiro(novo, tir.y, tir.direcao)
    if tir.direcao == 3:
        novo = tir.y + VEL_TIRO
        return Tiro(tir.x, novo, tir.direcao)
    if tir.direcao == 4:
        novo = tir.x + VEL_TIRO
        return Tiro(novo, tir.y, tir.direcao)
    return tir

def mover_jogo(jogo):
    '''
    função que é chamada no 'big bang' a cada tick
    é responsavel por chamar as outras funçoes
    :param jogo: Jogo
    :return: Jogo
    '''
    per=mover_perso(jogo.Personagem)
    tir=mover_tiro(jogo.Tiro)
    return Jogo(per, tir)

def desenha_pers(per):
    '''
    funçao responsavel por desenhar o perosnagem e suas direçoes
    :param per: jogo.Personagen
    :return: Jogo
    '''
    colocar_imagem(IMG_LAYOUT_1,tela,LARGURA//2,ALTURA//2)
    if per.direcao == 1:
        colocar_imagem(PERSONAGEM_UP, tela, per.x, per.y)
    elif per.direcao == 2:
        colocar_imagem(PERSONAGEM_LEFT, tela, per.x, per.y)
    elif per.direcao == 3:
        colocar_imagem(PERSONAGEM_DOWN, tela, per.x, per.y)
    elif per.direcao == 4:
        colocar_imagem(PERSONAGEM_RIGHT, tela, per.x, per.y)
    else:
        colocar_imagem(PERSONAGEM_DOWN,tela,per.x,per.y)


def desenha_tiro(tir):
    '''
    responsavel por desenhar o tiro e suas direçoes
    :param tir: jogo.Tiro
    :return: tela(Imagem)
    '''
    if tir.direcao == 1:
        colocar_imagem(TIRO_UP, tela, tir.x, tir.y)
    if tir.direcao == 2:
        colocar_imagem(TIRO_LEFT, tela, tir.x, tir.y)
    if tir.direcao == 3:
        colocar_imagem(TIRO_DOWN, tela, tir.x, tir.y)
    if tir.direcao == 4:
        colocar_imagem(TIRO_RIGHT, tela, tir.x, tir.y)


def desenha_jogo(jogo):
    '''
    funçao que é chamada no 'big bang'
    é responsavel por chamar as funçoes de desenhar
    :param jogo: Jogo
    :return: tela(imagem)
    '''
    desenha_pers(jogo.Personagem)
    desenha_tiro(jogo.Tiro)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_tecla_pers(per, tecla):
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
    '''
    responsavel por atirar, quando tecla == pg.K_SPACE
    :param jog: jogo
    :param tecla: pg.<tecla>
    :return: Tiro
    '''
    if tecla == pg.K_SPACE:
        tiro_x=jog.Personagem.x
        tiro_y=jog.Personagem.y
        return Tiro(tiro_x, tiro_y, jog.Personagem.direcao)
    #else
    return jog.Tiro

def trata_tecla_jogo(jogo, tecla):
    '''
    funçao que é chamada no 'big bang' por quando_tecla
    é reponsavel por chamar as funçoes baseadas em teclas
    :param jogo: Jogo
    :param tecla: pg.<tecla>
    :return: Jogo
    '''
    per = trata_tecla_pers(jogo.Personagem, tecla)
    tir = trata_tecla_tiro(jogo, tecla)
    return Jogo(per, tir)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_solta_per(per, tecla):
    '''
    funçao responsavel por parar o personagem quando o jogador solta a tecla
    :param per: jogo.Personagem
    :param tecla: pg.<tecla>
    :return: Personagem
    '''
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, per.dx, 0, per.direcao)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, 0, per.dy, per.direcao)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, per.dx, 0, per.direcao)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, 0, per.dy, per.direcao)
    return per

def trata_solta_tiro(tiro, tecla):
    '''
    função responsavel por poha nenuhma...
    :param tiro: jogo.Tiro
    :param tecla: pg.<tecla>
    :return: Tiro(a mesma merda)
    '''
    if tecla==pg.K_SPACE:
        return tiro
    return tiro

def trata_tecla_solta_jogo(jogo, tecla):
    '''
    função que é chamada no 'big bang' em quando_solta_tecla
    responsavel por chamar as funçoes de solta tecla
    :param jogo: Jogo
    :param tecla: pg.<tecla>
    :return: Jogo
    '''
    per=trata_solta_per(jogo.Personagem, tecla)
    tir=trata_solta_tiro(jogo.Tiro, tecla)
    return Jogo(per, tir)