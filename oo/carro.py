"""
DOCTEST

Exemplo:
>>>#Testando motor.
>>>motor = Motor()
>>>motor.velocidade
0
>>>motor.acelarar()
>>>motor.velocidade
1
>>>motor.acelarar()
>>>motor.velocidade
2
>>>motor.acelarar()
>>>motor.velocidade
3
>>>motor.frear()
>>>motor.velocidade
1
>>>motor.frear()
>>>motor.velocidade
0
>>>#Testando Direcao
>>>diracao = Direcao()
>>>direcao.valor
'Norte'
>>>diracao.girar_a_direita()
>>>direcao.valor
'Leste'
>>>diracao.girar_a_direita()
>>>direcao.valor
'Sul'
>>>diracao.girar_a_direita()
>>>direcao.valor
'Oeste'
>>>diracao.girar_a_direita()
>>>direcao.valor
'Norte'
>>>diracao.girar_a_esquerda()
>>>direcao.valor
'Oeste'
>>>diracao.girar_a_esquerda()
>>>direcao.valor
'Sul'
>>>diracao.girar_a_esquerda()
>>>direcao.valor
'Leste'
>>>diracao.girar_a_esquerda()
>>>direcao.valor
'Norte'
>>>carro = Carro(direcao,motor)
>>>carro.calcular_velocidade()
0
>>>carro.acelerar()
>>>carro.calcular_velocidade()
1
>>>carro.acelerar()
>>>carro.calcular_velocidade()
2
>>>carro.frear()
>>>carro.calcular_velocidade()
0
>>>carro.calcular_direcao()
>>>'Norte'
>>>carro.girar_a_direira()
>>>carro.calcular_direcao()
>>>'Leste'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
>>>'Norte'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
>>>'Oeste'





"""
NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'


class Direcao:
    def __init__(self):
        self.valor=NORTE

    def girar_a_direita(self):
        self.valor=LESTE

class Motor:
    def __init__(self):
        self.velocidade=0

    def acelerar(self):
        self.velocidade+=1

    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0,self.velocidade)

