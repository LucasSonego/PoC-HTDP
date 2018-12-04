from funcoes import *
import unittest


#mover_personagem
MOVER_PERSONAGEM_W = Personagem(100, 100, 0, -VELOCIDADE_PERSONAGEM, 1)
MOVER_PERSONAGEM_A = Personagem(100, 100, -VELOCIDADE_PERSONAGEM, 0, 1)
MOVER_PERSONAGEM_S = Personagem(100, 100, 0, VELOCIDADE_PERSONAGEM, 1)
MOVER_PERSONAGEM_D = Personagem(100, 100, VELOCIDADE_PERSONAGEM, 0, 1)
MOVER_PERSONAGEM_LE = Personagem(LIMITE_ESQUERDO,ALTURA//2,-VELOCIDADE_PERSONAGEM,0,1)
MOVER_PERSONAGEM_LD = Personagem(LIMITE_DIREITO,ALTURA//2,VELOCIDADE_PERSONAGEM,0,1)
MOVER_PERSONAGEM_LC = Personagem(LARGURA//2,LIMITE_CIMA,0,-VELOCIDADE_PERSONAGEM,1)
MOVER_PERSONAGEM_LB = Personagem(LARGURA//2,LIMITE_BAIXO,0,VELOCIDADE_PERSONAGEM,1)
MOVER_PERSONAGEM_LME = Personagem(LIMITE_MEIO_ESQ, ALTURA // 2, VELOCIDADE_PERSONAGEM, 0, 1)
MOVER_PERSONAGEM_LMD = Personagem(LIMITE_MEIO_DIR, ALTURA // 2, -VELOCIDADE_PERSONAGEM, 0, 1)
MOVER_PERSONAGEM_LMC = Personagem(LARGURA // 2, LIMITE_MEIO_CIMA, 0, VELOCIDADE_PERSONAGEM, 1)
MOVER_PERSONAGEM_LMB = Personagem(LARGURA // 2, LIMITE_MEIO_BAIXO, 0, -VELOCIDADE_PERSONAGEM, 1)


#mover_inimigo
MOVER_INIMIGO_I_1 = Inimigo(200,200,0,0)
MOVER_INIMIGO_P_1 = Personagem(100,100,0,0,1)

MOVER_INIMIGO_I_2 = Inimigo(100,100,0,0)
MOVER_INIMIGO_P_2 = Personagem(200,200,0,0,1)

MOVER_INIMIGO_I_3 = Inimigo(200,200,0,0)
MOVER_INIMIGO_P_3 = Personagem(204,100,0,0,1)

MOVER_INIMIGO_I_4 = Inimigo(100,204,0,0)
MOVER_INIMIGO_P_4 = Personagem(200,200,0,0,1)

MOVER_INIMIGO_I_5 = Inimigo(200,200,0,0)
MOVER_INIMIGO_P_5 = Personagem(600,600,0,0,1)


#mover_tiro
MOVER_TIRO_W = Tiro(100,100,1)
MOVER_TIRO_A = Tiro(100,100,2)
MOVER_TIRO_S = Tiro(100,100,3)
MOVER_TIRO_D = Tiro(100,100,4)


#exemplos de Personagem

PERSONAGEM_1 = Personagem(100, 100, 0, 0, 1)
PERSONAGEM_BASE_W = Personagem(100, 100, 0, 0, 1)
PERSONAGEM_BASE_A = Personagem(100, 100, 0, 0, 2)
PERSONAGEM_BASE_S = Personagem(100, 100, 0, 0, 3)
PERSONAGEM_BASE_D = Personagem(100, 100, 0, 0, 4)

PERSONAGEM_W = Personagem(100, 100, 0, -VELOCIDADE_PERSONAGEM, 1)
PERSONAGEM_A = Personagem(100, 100, -VELOCIDADE_PERSONAGEM, 0, 2)
PERSONAGEM_S = Personagem(100, 100, 0, +VELOCIDADE_PERSONAGEM, 3)
PERSONAGEM_D = Personagem(100, 100, +VELOCIDADE_PERSONAGEM, 0, 4)

#exemplos de jogo (para teste colide_inimigo_tiro)

COLIDE_TIRO = Jogo(PERSONAGEM_BASE_D, Tiro(300,300,4), Inimigo(300,300,0,0), False, 0)
NAO_COLIDE_TIRO = Jogo(PERSONAGEM_BASE_D, Tiro(300,300,4), Inimigo(400,400,0,0), False, 0)



class Test(unittest.TestCase):

    #linha 5
    def test_mover_personagem(self):
        # W pressionado
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_W), Personagem(100, 100 - VELOCIDADE_PERSONAGEM,
                                                                          0, -VELOCIDADE_PERSONAGEM, 1))

        # A pressionado
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_A), Personagem(100 - VELOCIDADE_PERSONAGEM,
                                                                          100, -VELOCIDADE_PERSONAGEM, 0, 1))

        # S pressionado
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_S), Personagem(100, 100 + VELOCIDADE_PERSONAGEM,
                                                                          0, VELOCIDADE_PERSONAGEM, 1))

        # D pressionado
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_D), Personagem(100 + VELOCIDADE_PERSONAGEM,
                                                                          100, VELOCIDADE_PERSONAGEM, 0, 1))

        # Colisao com LIMITE_ESQUERDO
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LE), MOVER_PERSONAGEM_LE)

        # Colisao com LIMITE_DIREITO
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LD), MOVER_PERSONAGEM_LD)

        # Colisao com LIMITE_CIMA
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LC), MOVER_PERSONAGEM_LC)

        # Colisao com LIMITE_BAIXO
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LB), MOVER_PERSONAGEM_LB)

        # colisao com LIMITE_MEIO_ESQ
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LME), MOVER_PERSONAGEM_LME)

        # colisao com LIMITE_MEIO_DIR
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LMD), MOVER_PERSONAGEM_LMD)

        # colisao com LIMITE_MEIO_CIMA
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LMC), MOVER_PERSONAGEM_LMC)

        # colisao com LIMITE_MEIO_BAIXO
        self.assertEqual(mover_personagem(MOVER_PERSONAGEM_LMB), MOVER_PERSONAGEM_LMB)

    #linha 20
    def test_mover_inimigo(self):
        # mover -dx e -dy
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_1, MOVER_INIMIGO_P_1), Inimigo(200-VELOCIDADE_INIMIGO,
                                                                                      200-VELOCIDADE_INIMIGO,
                                                                                      -VELOCIDADE_INIMIGO,
                                                                                      -VELOCIDADE_INIMIGO))

        # mover +dx e +dy
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_2, MOVER_INIMIGO_P_2), Inimigo(100+VELOCIDADE_INIMIGO,
                                                                                      100+VELOCIDADE_INIMIGO,
                                                                                      +VELOCIDADE_INIMIGO,
                                                                                      +VELOCIDADE_INIMIGO))
        #mover apenas dy
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_3, MOVER_INIMIGO_P_3), Inimigo(200,
                                                                                      200-VELOCIDADE_INIMIGO,
                                                                                      0,
                                                                                      -VELOCIDADE_INIMIGO))
        #mover apenas dx
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_4, MOVER_INIMIGO_P_4), Inimigo(100+VELOCIDADE_INIMIGO,
                                                                                      204,
                                                                                      +VELOCIDADE_INIMIGO,
                                                                                      0))
        #fora do range
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_5, MOVER_INIMIGO_P_5), MOVER_INIMIGO_I_5)



    #linha 37
    def test_mover_tiro(self):
        self.assertEqual(mover_tiro(MOVER_TIRO_W), Tiro(100, 100 - VELOCIDADE_TIRO, 1)) # W

        self.assertEqual(mover_tiro(MOVER_TIRO_A), Tiro(100 - VELOCIDADE_TIRO, 100, 2)) # A

        self.assertEqual(mover_tiro(MOVER_TIRO_S), Tiro(100, 100 + VELOCIDADE_TIRO, 3)) # S

        self.assertEqual(mover_tiro(MOVER_TIRO_D), Tiro(100 + VELOCIDADE_TIRO, 100, 4)) # D

    def test_mover_tiros(self):
        self.assertEqual(mover_tiros([MOVER_TIRO_A, MOVER_TIRO_D]),
                         [Tiro(100 - VELOCIDADE_TIRO, 100, 2), Tiro(100 + VELOCIDADE_TIRO, 100, 4)])
        self.assertEqual(mover_tiros([MOVER_TIRO_W, MOVER_TIRO_D]),
                         [Tiro(100, 100 - VELOCIDADE_TIRO, 1), Tiro(100 + VELOCIDADE_TIRO, 100, 4)])

    #linha 44
    def test_trata_tecla_personagem(self):
        self.assertEqual(trata_tecla_personagem(PERSONAGEM_1, pg.K_w), PERSONAGEM_W)  # W

        self.assertEqual(trata_tecla_personagem(PERSONAGEM_1, pg.K_a), PERSONAGEM_A)  # A

        self.assertEqual(trata_tecla_personagem(PERSONAGEM_1, pg.K_s), PERSONAGEM_S)  # S

        self.assertEqual(trata_tecla_personagem(PERSONAGEM_1, pg.K_d), PERSONAGEM_D)  # D

    # linha 44
    def test_trata_solta_personagem(self):
        self.assertEqual(trata_solta_personagem(PERSONAGEM_W, pg.K_w), PERSONAGEM_BASE_W)  # W

        self.assertEqual(trata_solta_personagem(PERSONAGEM_A, pg.K_a), PERSONAGEM_BASE_A)  # A

        self.assertEqual(trata_solta_personagem(PERSONAGEM_S, pg.K_s), PERSONAGEM_BASE_S)  # S

        self.assertEqual(trata_solta_personagem(PERSONAGEM_D, pg.K_d), PERSONAGEM_BASE_D)  # D


    def test_colide_inimigo(self):
        self.assertEqual(colide_inimigo(Personagem(100, 100, 0, 0, 1), Inimigo(300, 300, 0, 0)), False) # nao colide
        self.assertEqual(colide_inimigo(Personagem(100, 100, 0, 0, 1), Inimigo(105, 105, 0, 0)), True)  # colide

    def test_colidem_inimigos(self):
        self.assertEqual(
            colidem_inimigos(Personagem(100, 100, 0, 0, 1), [Inimigo(300, 300, 0, 0), Inimigo(105, 105, 0, 0)]), True)
        self.assertEqual(
            colidem_inimigos(Personagem(100, 100, 0, 0, 1), [Inimigo(300, 300, 0, 0), Inimigo(550, 550, 1, 0)]), False)
        self.assertEqual(
            colidem_inimigos(Personagem(100, 100, 0, 0, 1),
                             [Inimigo(300, 300, 0, 0), Inimigo(550, 550, 1, 0), Inimigo(105, 105, 0, 0)]), True)

    def test_trata_tecla_tiro(self):
        self.assertEqual(
            trata_tecla_tiro(Jogo(Personagem(100, 100, 0, 0, 1), [], [Inimigo(300, 300, 0, 0)], False, 2), pg.K_SPACE),
            [Tiro(100, 100, 1)])
        self.assertEqual(
            trata_tecla_tiro(Jogo(Personagem(200, 200, 0, 0, 3), [Tiro(100, 100, 1)], [Inimigo(300, 300, 0, 0)], False, 2), pg.K_SPACE),
            [Tiro(100, 100, 1), Tiro(200, 200, 3)])
        self.assertEqual(
            trata_tecla_tiro(
                Jogo(Personagem(200, 200, 0, 0, 3), [Tiro(100, 100, 1), Tiro(200, 200, 3)], [Inimigo(300, 300, 0, 0)], False, 2),
                pg.K_SPACE),
            [Tiro(100, 100, 1), Tiro(200, 200, 3)])

    def test_move_dx(self):
        self.assertEqual(move_dx(Inimigo(200, 200, 0, 0), Personagem(100, 100, 0, 0, 1)), -VELOCIDADE_INIMIGO) # -dx
        self.assertEqual(move_dx(Inimigo(100, 200, 0, 0), Personagem(200, 200, 0, 0, 1)), VELOCIDADE_INIMIGO)  # +dx
        self.assertEqual(move_dx(Inimigo(104, 104, 0, 0), Personagem(100, 100, 0, 0, 1)), 0)                   # nao move

    def test_move_dy(self):
        self.assertEqual(move_dx(Inimigo(200, 200, 0, 0), Personagem(100, 100, 0, 0, 1)), -VELOCIDADE_INIMIGO) # +dy
        self.assertEqual(move_dx(Inimigo(100, 200, 0, 0), Personagem(200, 200, 0, 0, 1)), VELOCIDADE_INIMIGO)  # -dy
        self.assertEqual(move_dx(Inimigo(104, 104, 0, 0), Personagem(100, 100, 0, 0, 1)), 0)                   # nao move

    #linha 57
    def test_colite_inimigo_tiro(self):
        self.assertEqual(colide_inimigo_tiro(COLIDE_TIRO), COLIDE_TIRO)
        self.assertEqual(colide_inimigo_tiro(NAO_COLIDE_TIRO), False)

    def test_colide_tiros(self):
        self.assertEqual(
            colide_tiros(Jogo(PERSONAGEM_BASE_D, [Tiro(300, 300, 4)], [Inimigo(300, 300, 0, 0)], False, 0)),
            Jogo(PERSONAGEM_BASE_D, [], [], False, 0))
        self.assertEqual(
            colide_tiros(Jogo(PERSONAGEM_BASE_D, [Tiro(300,300,4)], [Inimigo(400,400,0,0)], False, 0)),
            Jogo(PERSONAGEM_BASE_D, [Tiro(300,300,4)], [Inimigo(400, 400, 0, 0)], False, 0))
        self.assertEqual(
            colide_tiros(Jogo(PERSONAGEM_BASE_D, [Tiro(LIMITE_ESQUERDO, 100, 1)], [Inimigo(400, 400, 0, 0)], False, 0)),
                         Jogo(PERSONAGEM_BASE_D, [], [Inimigo(400, 400, 0, 0)], False, 0))

    def test_personagem_porta(self):
        self.assertEqual(personagem_porta(Personagem(100, 100, 0, 0, 1), 0), False) #nao colide
        self.assertEqual(personagem_porta(Personagem(600, 300, 0, 0, 1), 0), True)  #colide


    def test_colide_tiro_parede(self):
        self.assertEqual(colide_tiro_parede(Tiro(100, 100, 1)), False)  #nao colide
        self.assertEqual(colide_tiro_parede(Tiro(LIMITE_ESQUERDO, 100, 1)), Tiro(LIMITE_ESQUERDO, 100, 1)) #colide

    def test_att_layout(self):
        self.assertEqual(att_layout(1),JOGO_L2)

    def test_chama_inicio(self):
        self.assertEqual(chama_inicio(),JOGO_L0)


    def test_modulo(self):
        self.assertEqual(modulo(1),1)
        self.assertEqual(modulo(-1),1)

    def test_distancia(self):
        self.assertEqual(int(distancia(5,20,10,25)),7)
