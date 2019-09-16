class Profissional:
    def __init__(self, matricula='', nome='', funcao=''):
        self.matricula = matricula
        self.nome = nome
        self.funcao = funcao

    def __str__(self):
        return "\nProfissional: "+self.matricula+", "+self.nome+", funcao: "+self.funcao


if __name__ == "__main__":
    p1 = Profissional("123", "Joao", "Mecanico")
    p2 = Profissional("456", "Pedro", "Eletricista")
    print(p2)
