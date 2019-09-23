from peewee import *
arq = 'pessoas.db'
db = SqliteDatabase(arq)

class Pessoa(Model):
    nome = CharField()
    endereco = CharField()
    email = CharField()

    def __str__(self):
        return "Nome: "+self.nome + "Endereço: "+self.endereco+"email: "+self.email

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])

    joao = Pessoa.create(nome='Joao da Silva', endereco = 'Rua a', email = 'joao@hotmail.com')

    for p in Pessoa.select():
        print(joao)