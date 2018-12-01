from funcoes import *
import unittest


#mover_personagem
MOVER_PERSONAGEM_1 = Personagem(100, 100, 3, 0, 1)
MOVER_PERSONAGEM_2 = Personagem(100, 100, -3, 0, 1)
MOVER_PERSONAGEM_3 = Personagem(100, 100, 0, 3, 1)
MOVER_PERSONAGEM_4 = Personagem(100, 100, 0, -3, 1)
MOVER_PERSONAGEM_5 = Personagem(LIMITE_MEIO_ESQ, ALTURA // 2, 3, 0, 1)
MOVER_PERSONAGEM_6 = Personagem(LIMITE_MEIO_DIR, ALTURA // 2, -3, 0, 1)
MOVER_PERSONAGEM_7 = Personagem(LARGURA // 2, LIMITE_MEIO_CIMA, 0, 3, 1)
MOVER_PERSONAGEM_8 = Personagem(LARGURA // 2, LIMITE_MEIO_BAIXO, 0, -3, 1)

#mover_inimigo
MOVER_INIMIGO_I_1 = Inimigo(200,200,0,0)
MOVER_INIMIGO_P_1 = Personagem(100,100,0,0,1)
MOVER_INIMIGO_I_2 = Inimigo()
MOVER_INIMIGO_P_2 = Personagem()
MOVER_INIMIGO_I_3 = Inimigo()
MOVER_INIMIGO_P_3 = Personagem()
MOVER_INIMIGO_I_4 = Inimigo()
MOVER_INIMIGO_P_4 = Personagem()

#TODO criar testes para todas as funçoes possiveis




class Test(unittest.TestCase):

    #linha 5
    def test_mover_perso(self):
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_1), Personagem(103, 100, 3, 0, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_2), Personagem(97, 100, -3, 0, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_3), Personagem(100, 103, 0, 3, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_4), Personagem(100, 97, 0, -3, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_5), Personagem(LIMITE_MEIO_ESQ, ALTURA // 2, 3, 0, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_6), Personagem(LIMITE_MEIO_DIR, ALTURA // 2, -3, 0, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_7), Personagem(LARGURA // 2, LIMITE_MEIO_CIMA, 0, 3, 1))
        self.assertEqual(mover_perso(MOVER_PERSONAGEM_8), Personagem(LARGURA // 2, LIMITE_MEIO_BAIXO, 0, -3, 1))

    def test_modulo(self):
        self.assertEqual(modulo(1),1)
        self.assertEqual(modulo(-1),1)

    #
    def test_mover_inimigo(self):
        self.assertEqual(mover_inimigo(MOVER_INIMIGO_I_1,MOVER_INIMIGO_P_1),Inimigo(200,200,0,0))