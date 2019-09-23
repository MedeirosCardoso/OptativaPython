from peewee import *

arq = 'ifc.db'
db = SqliteDatabase(arq)


class Disciplina(Model):
    codDisciplina = IntegerField()
    descricao = CharField()
    cargaHoraria = IntegerField()

    def __str__(self):
        return "id da disciplina"+str(self.id)+", "+str(self.codDisciplina) + " - "+self.descricao+" - "+str(self.cargaHoraria)+"h"

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Disciplina])
    disciplina = Disciplina.create(
        codDisciplina=936, descricao='DESENVOLVIMENTO DE SISTEMAS EM PYTHON', cargaHoraria=60)
    print(disciplina)
