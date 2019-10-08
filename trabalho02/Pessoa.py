from Endereco import Endereco
from abc import ABC, abstractmethod
from peewee import *
from BaseModel import *
import os


class Pessoa(BaseModel):
    nome = CharField()
    endereco = ForeignKeyField(Endereco)
    email = CharField()

    def __str__(self):
        return "Nome: " + self.nome + ", email: " + self.email + ", " + str(self.endereco)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Pessoa, Endereco])
    end = Endereco.create(cep=89035100, logradouro="Rua abc", numero=123,
                          bairro="Vila Nova", municipio="Blumenau", estado="SC")
    p1 = Pessoa.create(nome="Joao", endereco=end, email="manda@gmail.com")
    print(p1)
