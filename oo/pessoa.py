class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    mairon = Pessoa(renzo, nome='Mairon')
    print(Pessoa.cumprimentar(mairon))
    print(id(mairon))
    print(mairon.cumprimentar())
    print(mairon.nome)
    print(mairon.idade)
    print(mairon.filhos)
    for filho in mairon.filhos:
        print(filho.nome)


