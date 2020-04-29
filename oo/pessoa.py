class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
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
    print(Pessoa.metodo_estatico(), mairon.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), mairon.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Homem))
