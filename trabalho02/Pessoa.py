from Endereco import Endereco
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.Endereco = endereco
        self.email = email
        super().__init__()

    def __str__(self):
        return "Nome: " + self.nome + ", email: " + self.email+ ", " + str(self.Endereco)


if __name__ == "__main__":
    end = Endereco(89035100, "Rua abc", 123, "Vila Nova", "Blumenau", "SC")
    p1 = Pessoa("Joao", end, "manda@gmail.com")
    print(p1)
