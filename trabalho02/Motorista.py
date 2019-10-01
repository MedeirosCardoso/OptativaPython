from Pessoa import Pessoa
from Endereco import Endereco


class Motorista(Pessoa):
    def __init__(self, nome, endereco, email, matricula, catCNH=''):
        self.matricula = matricula
        self.catCNH = catCNH
        super().__init__(nome, endereco, email)

    def __str__(self):
        return super().__str__() + "Matricula: " + self.matricula + "CNH: " + self.catCNH


if __name__ == '__main__':
    end = Endereco(89035101, "Rua abcd", 123, "Vila Nova", "Blumenau", "SC")
    mot = Motorista("Joao da silva", end, "manda@gmail.com",
                    "D001", "categoria D")
    print(mot)
