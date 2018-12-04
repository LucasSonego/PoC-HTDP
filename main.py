#!/usr/bin/env python
# -*- coding: utf-8 -*-

from funcoes import *
from constantes import *
from def_dados import *

def main(inic):
    big_bang(inic,
             tela=tela,
             frequencia=FREQUENCIA,
             a_cada_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla_jogo,
             quando_solta_tecla=trata_tecla_solta_jogo,
             modo_debug=False
             )



main(JOGO_L0)

