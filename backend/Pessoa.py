from peewee import *
from BaseModel import *

arq = '/tmp/pessoas.db'
db = SqliteDatabase(arq)

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()

    def __str__(self):
        return "Nome: "+self.nome + " Endereço: "+self.endereco+" Telefone: "+self.telefone+" email: "+self.email

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])

    joao = Pessoa.create(nome='Joao da Silva', endereco = 'Rua a', telefone = "12345",email = 'joao@hotmail.com')

    for p in Pessoa.select():
        print(joao)