#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
from def_dados import *


def mover_perso(jogo):
    '''
    função responsavel por mover o personagem na tela
    :param jogo: Jogo
    :return: Personagem
    '''
    posicao_x = jogo.personagem.x + jogo.personagem.dx
    posicao_y = jogo.personagem.y + jogo.personagem.dy

    #limites laterais para x
    if posicao_x > T1_LIMITE_DIREITO or posicao_x < T1_LIMITE_ESQUERDO:
        return Personagem(jogo.personagem.x, jogo.personagem.y, jogo.personagem.dx, jogo.personagem.dy,
                          jogo.personagem.direcao)
    #limites laterais para y
    if posicao_y < T1_LIMITE_CIMA or posicao_y > T1_LIMITE_BAIXO:
        return Personagem(jogo.personagem.x, jogo.personagem.y, jogo.personagem.dx, jogo.personagem.dy,
                          jogo.personagem.direcao)

    #limites para o bloco do centro
    if (T1_LIMITE_MEIO_ESQ < posicao_x < T1_LIMITE_MEIO_DIR) and (T1_LIMITE_MEIO_CIMA < posicao_y < T1_LIMITE_MEIO_BAIXO):
        return Personagem(jogo.personagem.x, jogo.personagem.y, jogo.personagem.dx, jogo.personagem.dy,
                          jogo.personagem.direcao)
    if (T1_LIMITE_MEIO_CIMA < posicao_y < T1_LIMITE_MEIO_BAIXO) and (T1_LIMITE_MEIO_ESQ < posicao_x < T1_LIMITE_MEIO_DIR):
        return Personagem(jogo.personagem.x, jogo.personagem.y, jogo.personagem.dx, jogo.personagem.dy,
                          jogo.personagem.direcao)

    return Personagem(posicao_x, posicao_y, jogo.personagem.dx, jogo.personagem.dy, jogo.personagem.direcao)

def mover_tiro(tiro):
    '''
    funçao responsavel por mover os tiros na tela
    :param tiro: jogo.tiro
    :return: Tiro
    '''
    if tiro.direcao == 1:
        novo = tiro.y - VEL_TIRO
        return Tiro(tiro.x, novo, tiro.direcao)
    if tiro.direcao == 2:
        novo = tiro.x - VEL_TIRO
        return Tiro(novo, tiro.y, tiro.direcao)
    if tiro.direcao == 3:
        novo = tiro.y + VEL_TIRO
        return Tiro(tiro.x, novo, tiro.direcao)
    if tiro.direcao == 4:
        novo = tiro.x + VEL_TIRO
        return Tiro(novo, tiro.y, tiro.direcao)
    return tiro

def mover_jogo(jogo):
    '''
    função que é chamada no 'big bang' a cada tick
    é responsavel por chamar as outras funçoes
    :param jogo: Jogo
    :return: Jogo
    '''
    per=mover_perso(jogo)
    tir=mover_tiro(jogo.tiro)
    return Jogo(per, tir)

def desenha_pers(personagem):
    '''
    funçao responsavel por desenhar o perosnagem e suas direçoes
    :param personagem: jogo.Personagen
    :return: Jogo
    '''
    colocar_imagem(IMG_LAYOUT_1,tela,LARGURA//2,ALTURA//2)
    if personagem.direcao == 1:
        colocar_imagem(PERSONAGEM_UP, tela, personagem.x, personagem.y)
    elif personagem.direcao == 2:
        colocar_imagem(PERSONAGEM_LEFT, tela, personagem.x, personagem.y)
    elif personagem.direcao == 3:
        colocar_imagem(PERSONAGEM_DOWN, tela, personagem.x, personagem.y)
    elif personagem.direcao == 4:
        colocar_imagem(PERSONAGEM_RIGHT, tela, personagem.x, personagem.y)
    else:
        colocar_imagem(PERSONAGEM_DOWN, tela, personagem.x, personagem.y)


def desenha_tiro(tiro):
    '''
    responsavel por desenhar o tiro e suas direçoes
    :param tiro: jogo.tiro
    :return: tela(Imagem)
    '''
    if tiro.direcao == 1:
        colocar_imagem(TIRO_UP, tela, tiro.x, tiro.y)
    if tiro.direcao == 2:
        colocar_imagem(TIRO_LEFT, tela, tiro.x, tiro.y)
    if tiro.direcao == 3:
        colocar_imagem(TIRO_DOWN, tela, tiro.x, tiro.y)
    if tiro.direcao == 4:
        colocar_imagem(TIRO_RIGHT, tela, tiro.x, tiro.y)


def desenha_jogo(jogo):
    '''
    funçao que é chamada no 'big bang'
    é responsavel por chamar as funçoes de desenhar
    :param jogo: Jogo
    :return: tela(imagem)
    '''
    desenha_pers(jogo.personagem)
    desenha_tiro(jogo.tiro)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_tecla_pers(personagem, tecla):
    if tecla == pg.K_w:
        return Personagem(personagem.x, personagem.y, 0, -VEL_PERSONAGEM, 1)
    if tecla == pg.K_a:
        return Personagem(personagem.x, personagem.y, -VEL_PERSONAGEM, 0, 2)
    if tecla == pg.K_s:
        return Personagem(personagem.x, personagem.y, 0, VEL_PERSONAGEM, 3)
    if tecla == pg.K_d:
        return Personagem(personagem.x, personagem.y, VEL_PERSONAGEM, 0, 4)
    return personagem

def trata_tecla_tiro(jogo, tecla):
    '''
    responsavel por atirar, quando tecla == pg.K_SPACE
    :param jogo: jogo
    :param tecla: pg.<tecla>
    :return: Tiro
    '''
    if tecla == pg.K_SPACE:
        tiro_x=jogo.personagem.x
        tiro_y=jogo.personagem.y
        return Tiro(tiro_x, tiro_y, jogo.personagem.direcao)
    #else
    return jogo.tiro

def trata_tecla_jogo(jogo, tecla):
    '''
    funçao que é chamada no 'big bang' por quando_tecla
    é reponsavel por chamar as funçoes baseadas em teclas
    :param jogo: Jogo
    :param tecla: pg.<tecla>
    :return: Jogo
    '''
    per = trata_tecla_pers(jogo.personagem, tecla)
    tir = trata_tecla_tiro(jogo, tecla)
    return Jogo(per, tir)

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_solta_per(personagem, tecla):
    '''
    funçao responsavel por parar o personagem quando o jogador solta a tecla
    :param personagem: jogo.personagem
    :param tecla: pg.<tecla>
    :return: Personagem
    '''
    if tecla == pg.K_w:
        return Personagem(personagem.x, personagem.y, personagem.dx, 0, personagem.direcao)
    if tecla == pg.K_a:
        return Personagem(personagem.x, personagem.y, 0, personagem.dy, personagem.direcao)
    if tecla == pg.K_s:
        return Personagem(personagem.x, personagem.y, personagem.dx, 0, personagem.direcao)
    if tecla == pg.K_d:
        return Personagem(personagem.x, personagem.y, 0, personagem.dy, personagem.direcao)
    return personagem

def trata_solta_tiro(tiro, tecla):
    '''
    função responsavel por poha nenuhma...
    :param tiro: jogo.tiro
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
    personagem=trata_solta_per(jogo.personagem, tecla)
    tiro=trata_solta_tiro(jogo.tiro, tecla)
    return Jogo(personagem, tiro)