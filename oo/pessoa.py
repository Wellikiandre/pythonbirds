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

if __name__=='__main__':
    filho=Pessoa(nome='Cesar',idade=10)
    p=Pessoa(filho,nome='Wellikiandre',idade=30)
    print (f'{p.nome}, {p.idade}')
    for f in p.filhos:
        print(f.nome)
        print(f.idade)
    print (Pessoa.metodo_estatico() , p.metodo_estatico())
    print (Pessoa.metodo_de_classe_e_atributo(),filho.metodo_de_classe_e_atributo())
