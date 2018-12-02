#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constantes import *
from def_dados import *
from math import *



#FUNCOES MOVE
def mover_jogo(jogo):
    '''
    função que é chamada no 'big bang' a cada tick
    é responsavel por chamar as outras funçoes
    :param jogo: Jogo
    :return: Jogo
    '''
    if personagem_porta(jogo.personagem, jogo.cont):
        jogo = att_layout(jogo.cont)
    if (colidem_inimigos(jogo.personagem, jogo.inimigos)):
        return Jogo(jogo.personagem, jogo.tiros, jogo.inimigos, True, jogo.cont)
    else:
        lista = colide_tiros(jogo)
        personagem=mover_perso(jogo.personagem)
        tiros=mover_tiros(lista.tiros)
        inimigo=mover_inimigos(lista.inimigos,jogo.personagem)
    return Jogo(personagem, tiros, inimigo, jogo.game_over, jogo.cont)


def mover_perso(personagem):
    '''
    função responsavel por mover o personagem na tela
    :param personagem: Personagem
    :return: Personagem
    '''
    posicao_x = personagem.x + personagem.dx
    posicao_y = personagem.y + personagem.dy

    #limites laterais para x
    if posicao_x + M_LARGURA_PERSONAGEM > LIMITE_DIREITO or posicao_x - M_LARGURA_PERSONAGEM < LIMITE_ESQUERDO:
        return Personagem(personagem.x, personagem.y, personagem.dx, personagem.dy,
                          personagem.direcao)
    #limites laterais para y
    if posicao_y - M_ALTURA_PERSONAGEM < LIMITE_CIMA or posicao_y + M_ALTURA_PERSONAGEM> LIMITE_BAIXO:
        return Personagem(personagem.x, personagem.y, personagem.dx, personagem.dy,
                          personagem.direcao)

    #limites para o bloco do centro
    if (LIMITE_MEIO_ESQ < posicao_x + M_LARGURA_PERSONAGEM and posicao_x - M_LARGURA_PERSONAGEM < LIMITE_MEIO_DIR) and\
            (LIMITE_MEIO_CIMA < posicao_y + M_ALTURA_PERSONAGEM and posicao_y - M_ALTURA_PERSONAGEM < LIMITE_MEIO_BAIXO):
        return Personagem(personagem.x, personagem.y, personagem.dx, personagem.dy,
                          personagem.direcao)

    return Personagem(posicao_x, posicao_y, personagem.dx, personagem.dy, personagem.direcao)


def mover_tiros(tiros):
    '''
    Chama a funcao de mover_tiro para a lista de tiros
    :param tir: Lista Tiro
    :return: Lista Tiro
    '''
    return [mover_tiro(tiro) for tiro in tiros]


def mover_tiro(tiro):
    '''
    funçao responsavel por mover os tiros na tela
    :param tiro: Tiro
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

def mover_inimigos(inimigos, per):
    '''
    Chama a funcao de mover_inimigo para a lista de inimigos
    :param inimigos: Lista Inimigo
    :param per: Personagem
    :return: Lista Inimigo
    '''
    return[mover_inimigo(inimigo, per)for inimigo in inimigos]


def mover_inimigo(inimigo,personagem):
    '''
    Dependendo da distancia do personagem em relacao ao inimigo ele move inimigo
    :param inimigo: Inimigo
    :param personagem: Personagem
    :return: Inimigo
    '''
    distancia_x = personagem.x - inimigo.x
    distancia_x = modulo(distancia_x)

    distancia_y = personagem.y - inimigo.y
    distancia_y = modulo(distancia_y)

    if distancia_x < 300 and distancia_y < 300:

        dx = move_dx(inimigo,personagem)
        dy = move_dy(inimigo,personagem)

        return Inimigo(inimigo.x + dx,inimigo.y + dy,dx,dy)
    #else
    return Inimigo(inimigo.x,inimigo.y,0,0)

#FUNCOES DESENHA
def desenha_jogo(jogo):
    '''
    funçao que é chamada no 'big bang'
    é responsavel por chamar as funçoes de desenhar
    :param jogo: Jogo
    :return: Imagem
    '''
    if jogo.game_over == False :
        fundo = IMGS [jogo.cont]
        colocar_imagem(fundo, tela, LARGURA // 2, ALTURA // 2)
        desenha_pers(jogo.personagem)
        desenha_tiros(jogo.tiros)
        desenha_inimigos(jogo.inimigos)
    else:
        desenha_game_over()


def desenha_pers(personagem):
    '''
    funçao responsavel por desenhar o perosnagem e suas direçoes
    :param personagem: Personagem
    '''
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


def desenha_inimigos(inimigos):
    '''
    Chama a funcao de desenha_inimigo para a lista de inimigos
    :param inimigos: Lista Inimigos
    :return: Imagem
    '''
    for inimigo in inimigos:
        desenha_inimigo(inimigo)


def desenha_inimigo(inimigo):
    '''
    desenha inimigo left/right
    :param inimigo: Inimigo
    :return:Imagem
    '''
    if inimigo.dx > 0:
        colocar_imagem(INIMIGO_RIGHT, tela, inimigo.x, inimigo.y)
    if inimigo.dx < 0:
        colocar_imagem(INIMIGO_LEFT, tela, inimigo.x, inimigo.y)
    if inimigo.dx == 0:
        colocar_imagem(INIMIGO_LEFT, tela, inimigo.x, inimigo.y)

def desenha_tiros(tiros):
    '''
    chama a funcao de desenha_tiro para a lista
    :param tiros: Tiro
    :return: Imagem
    '''
    for tiro in tiros:
        desenha_tiro(tiro)


def desenha_tiro(tiro):
    '''
    responsavel por desenhar o tiro e suas direçoes
    :param tiro: Tiro
    '''
    if tiro.direcao == 1:
        colocar_imagem(TIRO_UP, tela, tiro.x, tiro.y)
    if tiro.direcao == 2:
        colocar_imagem(TIRO_LEFT, tela, tiro.x, tiro.y)
    if tiro.direcao == 3:
        colocar_imagem(TIRO_DOWN, tela, tiro.x, tiro.y)
    if tiro.direcao == 4:
        colocar_imagem(TIRO_RIGHT, tela, tiro.x, tiro.y)


def desenha_game_over():
    '''
    Desenha o game over
    :return: Imagem
    '''
    texto_game_over = texto("GAME OVER          APERTE ENTER PARA REINICIAR", Fonte("comicsans", 50), Cor("red"))
    colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)

#FUNCOES TRATA TECLA
def trata_tecla_jogo(jogo, tecla):
    '''
    funçao que é chamada no 'big bang' por quando_tecla
    é reponsavel por chamar as funçoes baseadas em teclas
    :param jogo: Jogo
    :param tecla: pg.<tecla>
    :return: Jogo
    '''
    if tecla == pg.K_KP_ENTER:
        jogo = chama_inicio()
    perosnagem = trata_tecla_pers(jogo.personagem, tecla)
    tiro = trata_tecla_tiro(jogo, tecla)
    return Jogo(perosnagem, tiro, jogo.inimigos, jogo.game_over, jogo.cont)


def trata_tecla_pers(personagem, tecla):
    '''
    Conforme aperta as teclas de movimento muda o dx e dy do personagem
    :param personagem: Personagem
    :param tecla: pg.key
    :return: Personagem
    '''
    if tecla == pg.K_w:
        return Personagem(personagem.x, personagem.y, 0, -VEL_PERSONAGEM, 1)
    if tecla == pg.K_a:
        return Personagem(personagem.x, personagem.y, -VEL_PERSONAGEM, 0, 2)
    if tecla == pg.K_s:
        return Personagem(personagem.x, personagem.y, 0, VEL_PERSONAGEM, 3)
    if tecla == pg.K_d:
        return Personagem(personagem.x, personagem.y, VEL_PERSONAGEM, 0, 4)
    return personagem

def trata_tecla_tiro(jog, tecla):
    '''
    responsavel por atirar, quando tecla == pg.K_SPACE
    :param jog: jogo
    :param tecla: pg.<tecla>
    :return: Lista Tiro
    '''
    if tecla == pg.K_SPACE:
        tiro_x = jog.personagem.x
        tiro_y = jog.personagem.y
        if len(jog.tiros) <= 1 :
            jog.tiros.append(Tiro(tiro_x, tiro_y, jog.personagem.direcao))
        return jog.tiros
    # else
    return jog.tiros

#FUNCOES TRATA SOLTA TECLA
def trata_tecla_solta_jogo(jogo, tecla):
    '''
    função que é chamada no 'big bang' em quando_solta_tecla
    responsavel por chamar as funçoes de solta tecla
    :param jogo: Jogo
    :param tecla: pg.<tecla>
    :return: Jogo
    '''
    personagem=trata_solta_per(jogo.personagem, tecla)
    tiro=trata_solta_tiro(jogo.tiros, tecla)

    return Jogo(personagem, tiro, jogo.inimigos, jogo.game_over, jogo.cont)


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
    Tinha que existir
    :param tiro: jogo.tiro
    :param tecla: pg.<tecla>
    :return: Tiro(a mesma merda)
    '''
    if tecla==pg.K_SPACE:
        return tiro
    return tiro

#FUNCOES DE COLISAO
def colide_inimigo(per, ini):
    '''
    Verifica se inimigo colide com personagem
    :param per: Personagem
    :param ini: Inimigo
    :return: Boolean
    '''
    raio1 = LARGURA_INIMIGO//2
    raio2 = LARGURA_INIMIGO//2
    d = distancia(per.x, per.y, ini.x, ini.y)
    if d <= raio1 + raio2:
        return True
    # else
    return False


def personagem_porta(personagem, cont):
    '''
    Verifica se o personagem colide com a Porta
    :param personagem: Personagem
    :param cont: int
    :return: Boolean
    '''
    esquerda_per = personagem.x - LARGURA_PERSONAGEM
    direita_per = personagem.x + LARGURA_PERSONAGEM
    cima_per = personagem.y - ALTURA_PERSONAGEM
    baixo_per = personagem.y + ALTURA_PERSONAGEM

    porta = PORTAS[cont]
    return direita_per >= porta.x and \
            esquerda_per <= porta.x and \
            baixo_per >= porta.y and \
            cima_per <= porta.y

def colidem_inimigos(per, inimigos):
    '''
    Verifica colisao para lista de inimigos
    :param per: Personagem
    :param inimigos: Inimigo
    :return: Boolean
    '''
    for inimigo in inimigos:
        if colide_inimigo(per, inimigo):
            return True
    #else
    return False

def colide_inimigo_tiro(jogo):
    '''
    Verifica se o tiro entrou em colisao com o inimigo se sim retorna o jogo se nao retorna False
    :param jogo: Jogo
    :return: Jogo ou False
    '''
    esquerda_ini = jogo.inimigos.x - LARGURA_INIMIGO//2
    direita_ini = jogo.inimigos.x + LARGURA_INIMIGO//2
    cima_ini = jogo.inimigos.y - ALTURA_INIMIGO//2
    baixo_ini = jogo.inimigos.y + ALTURA_INIMIGO//2

    esquerda_tiro = jogo.tiros.x - LARGURA_TIRO//2
    direita_tiro = jogo.tiros.x + LARGURA_TIRO//2
    cima_tiro = jogo.tiros.y - ALTURA_TIRO//2
    baixo_tiro = jogo.tiros.y + ALTURA_TIRO//2


    if direita_ini >= esquerda_tiro and \
            esquerda_ini<= direita_tiro and \
            baixo_ini >= cima_tiro and \
            cima_ini <= baixo_tiro:
        return jogo
    return False

def colide_tiro_parede(tiro):
    '''
    Verifica se o tiro bateu nos limites laterais se sim retorna o tiro se nao retora False
    :param tiro: Tiro
    :return: Tiro ou False
    '''
    if LIMITE_DIREITO <= tiro.x + LARGURA_TIRO // 3 or \
            LIMITE_ESQUERDO >= tiro.x - LARGURA_TIRO // 3 or \
            LIMITE_BAIXO <= tiro.y + ALTURA_TIRO // 2 or \
            LIMITE_CIMA >= tiro.y - ALTURA_TIRO // 2 :
        return tiro
    return False


def colide_tiros(jogo):
    '''
    Exclui os tiros e os inimigos que colidiram
    :param jogo: Jogo
    :return: Jogo
    '''
    for tiro in jogo.tiros:
        for inimigo in jogo.inimigos:
            some_inimigo_tiro = colide_inimigo_tiro(Jogo(jogo.personagem, tiro, inimigo, jogo.game_over, jogo.cont))
            if some_inimigo_tiro:
                jogo.tiros.remove(some_inimigo_tiro.tiros)
                jogo.inimigos.remove(some_inimigo_tiro.inimigos)
        tiro_some_parede = colide_tiro_parede(tiro)
        if tiro_some_parede:
            jogo.tiros.remove(tiro_some_parede)

    return jogo

#FUNCOES AUXILIARES
def distancia(x1, y1, x2, y2):
    '''
    Calcula a distancia entre o inimigo e o personagem
    :param x1: Personagem.x(Int)
    :param y1: Personagem.y(Int)
    :param x2: Inimigo.x(Int)
    :param y2: Inimigo.y(Int)
    :return: Int
    '''
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def modulo(num):
    '''
    Faz o modulo do numero recebido
    :param num: Int
    :return: Int
    '''
    if num < 0:
        return -num
    return num


def move_dx(inimigo,personagem):
    '''
    Verifica posicao do inimigo em relacao ao personagem e envia um dx dependendo da circunstancia
    :param inimigo: Inimigo
    :param personagem: Personagem
    :return: Int
    '''
    if -(inimigo.x - personagem.x) < -5:
        dx = -VEL_INIMIGO
    elif -(inimigo.x - personagem.x) > 5:
        dx = VEL_INIMIGO
    else:
        dx = 0

    return dx

def move_dy(inimigo,personagem):
    '''
    Verifica posicao do inimigo em relacao ao personagem e envia um dy dependendo da circunstancia
    :param inimigo: Inimigo
    :param personagem: Personagem
    :return: Int
    '''
    if -(inimigo.y - personagem.y) < -5:
        dy = -VEL_INIMIGO
    elif -(inimigo.y - personagem.y) > 5:
        dy = VEL_INIMIGO
    else:
        dy = 0

    return dy

def att_layout(cont):
    '''
    Atualiza quando troca de salas
    :param cont: int
    :return: Jogo
    '''
    return LAYOUT[cont+1]


def chama_inicio():
    '''
    Chama o Layout inicial do jogo
    :return: Jogo
    '''
    return JOGO_L0