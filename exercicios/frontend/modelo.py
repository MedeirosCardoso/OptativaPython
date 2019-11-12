from peewee import *

arq = '/tmp/outro.db' #':memory:'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()

    
if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao da Silva", endereco="Casa 9", telefone="123456",email="joao@hotmail.com")
    print(joao.nome, ",", joao.endereco, ",", joao.email)
