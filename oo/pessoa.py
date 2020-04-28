class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    mairon = Pessoa(renzo, nome='Mairon')
    mairon.olhos = 1
    print(Pessoa.cumprimentar(mairon))
    print(id(mairon))
    print(mairon.cumprimentar())
    print(mairon.nome)
    print(mairon.idade)
    print(mairon.filhos)
    for filho in mairon.filhos:
        print(filho.nome)
    mairon.sobrenome = 'Gallas'
    print(mairon.sobrenome)
    del mairon.filhos
    del mairon.olhos
    print(mairon.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(mairon.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(mairon.olhos), id(renzo.olhos))

