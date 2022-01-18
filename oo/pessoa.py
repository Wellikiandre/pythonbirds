class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome=None,idade=None ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 49

    @classmethod
    def metodo_de_classe_e_atributo(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mulher(Pessoa):
    pass

if __name__=='__main__':
    cesar=Homem(nome='Cesar',idade=10)
    wellikiandre=Homem(cesar,nome='Wellikiandre',idade=30)
    print (f'{wellikiandre.nome}, {wellikiandre.idade}')
    for f in wellikiandre.filhos:
        print(f.nome)
        print(f.idade)
    print (Pessoa.metodo_estatico() , wellikiandre.metodo_estatico())
    print (Pessoa.metodo_de_classe_e_atributo(),cesar.metodo_de_classe_e_atributo())

### HERANÇA

    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(wellikiandre,Pessoa))
    print(isinstance(wellikiandre,Homem))