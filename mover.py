#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Mover personagem '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (700, 700)
tela = criar_tela_base(LARGURA, ALTURA)

#Criar/carregar imagens:
IMG_PERSONAGEM = carregar_imagem("fantasma.png")
IMG_PERSONAGEM = definir_dimensoes(IMG_PERSONAGEM, 80, 120)

LIMITE_ESQUERDO = 0 + largura_imagem(IMG_PERSONAGEM) // 2
LIMITE_DIREITO = LARGURA - (largura_imagem(IMG_PERSONAGEM) // 2)
LIMITE_CIMA = 0 + altura_imagem(IMG_PERSONAGEM) // 2
LIMITE_BAIXO = ALTURA - (altura_imagem(IMG_PERSONAGEM) // 2)


VEL_PERSONAGEM = 5
'''==================='''
'''# Definições de dados: '''

Personagem = definir_estrutura("Personagem", "x, y, dx, dy")
''' Personagem pode ser formado por: Personagem(Int[LIMITE_ESQUERDO, LIMITE_DIREITO], Int[LIMITE_CIMA, LIMITE_BAIXO], Int, Int 
Rep. a posicao do eixo x e y e as velocidades do personagem
'''

'''===================='''
''' Funções: '''

'''
tock: Personagem -> Personagem
Produz o próximo Personagem'''

def mover_perso(per):
    posicao_x = per.x + per.dx
    posicao_y = per.y + per.dy
    if posicao_x > LIMITE_DIREITO or posicao_x < LIMITE_ESQUERDO:
        return Personagem(per.x, per.y, per.dx, per.dy)
    if posicao_y < LIMITE_CIMA or posicao_y > LIMITE_BAIXO:
        return Personagem(per.x, per.y, per.dx, per.dy)
    return Personagem(posicao_x, posicao_y, per.dx, per.dy)

'''
desenha: Personagem -> Imagem
Desenha...'''

def desenha_perso(per):
    colocar_imagem(IMG_PERSONAGEM, tela, per.x, per.y)


'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_tecla(per, tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, 0, -VEL_PERSONAGEM)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, -VEL_PERSONAGEM, 0)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, 0, VEL_PERSONAGEM)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, VEL_PERSONAGEM, 0)
    return per

'''
trata_tecla: Personagem, Tecla -> Personagem
Conforme aperta as teclas de movimento muda o dx e dy do personagem'''

def trata_solta(per,tecla):
    if tecla == pg.K_w:
        return Personagem(per.x, per.y, per.dx, 0)
    if tecla == pg.K_a:
        return Personagem(per.x, per.y, 0, per.dy)
    if tecla == pg.K_s:
        return Personagem(per.x, per.y, per.dx, 0)
    if tecla == pg.K_d:
        return Personagem(per.x, per.y, 0, per.dy)
    return per



''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ... '''
def main(inic):
    big_bang(inic, tela=tela, frequencia=50, quando_tick=mover_perso,desenhar=desenha_perso, quando_tecla=trata_tecla,quando_solta_tecla=trata_solta, modo_debug=True)

main(Personagem(100, 100, 0, 0))

