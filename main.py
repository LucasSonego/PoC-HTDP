#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcoes import *
from constantes import *

def main(inic):
    big_bang(inic,
             tela=tela,
             frequencia=50,
             a_cada_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla_jogo,
             quando_solta_tecla=trata_tecla_solta_jogo,
             modo_debug=True)

main(Jogo(Personagem(100, 100, 0, 0, 0), Tiro(100,100,0)))