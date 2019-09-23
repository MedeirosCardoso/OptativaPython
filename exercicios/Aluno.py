from peewee import *

arq = 'ifc.db'
db = SqliteDatabase(arq)


class Aluno(Model):
    matricula = IntegerField()
    nome = CharField()
    email = CharField()

    def __str__(self):
        return "Id do aluno: "+str(self.id)+", Matricula: "+str(self.matricula) + " Nome: "+self.nome+" email: "+self.email

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Aluno])
    aluno = Aluno.create(matricula=123, nome='adriano', email='')
    print(aluno)
