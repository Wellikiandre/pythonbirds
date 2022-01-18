#TesteCase do UnitTest
from unittest import TestCase

from oo.carro import Motor


class CarroTestCase(TestCase):
    #Tem que começar com teste
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)
        #Para executar via terminal (python -m unittest discover oo)

    def teste_acelerar(self):
        motor = Motor()
        self.assertEqual(1,motor.velocidade)
        #Obs. em cima do metodo roda so o metodo do teste






