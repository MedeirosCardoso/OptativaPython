from peewee import *
from Pessoa import Pessoa
from Endereco import Endereco
from BaseModel import *
import os


class Usuario(Pessoa):
    login = CharField()
    senha = CharField()

    def __str__(self):
        return super().__str__() + "Login: " + self.login + " Senha: " + str(self.senha)


if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Usuario, Endereco])

    end = Endereco.create(cep=89035100, logradouro="Rua abc", numero=123,
                          bairro="Vila Nova", municipio="Blumenau", estado="SC")

    usuario = Usuario.create(nome="Joao da silva", endereco=end, email="manda@gmail.com",
                             login="testeLogin", senha="123456789")
    print(usuario)
