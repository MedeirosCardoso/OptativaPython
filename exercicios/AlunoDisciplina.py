from peewee import *
from Aluno import Aluno
from Disciplina import Disciplina

arq = 'ifc.db'
db = SqliteDatabase(arq)


class AlunoDisciplina(Model):
    aluno = ForeignKeyField(Aluno)
    disciplina = ForeignKeyField(Disciplina)

    def __str__(self):
        return str(self.aluno) + str(self.disciplina)

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Aluno, Disciplina, AlunoDisciplina])

    joao = Aluno.create(matricula=123, nome='adriano', email='')

    optativa = Disciplina.create(
        codDisciplina=936, descricao='DESENVOLVIMENTO DE SISTEMAS EM PYTHON', cargaHoraria=60)
    bdI = Disciplina.create(
        codDisciplina=937, descricao='BANCO DE DADOS I', cargaHoraria=60)
    pgmV = Disciplina.create(
        codDisciplina=938, descricao='PROGRAMAÇÃO V', cargaHoraria=60)

    disciplinaDoAluno1 = AlunoDisciplina.create(
        aluno=joao, disciplina=optativa)
    disciplinaDoAluno2 = AlunoDisciplina.create(aluno=joao, disciplina=bdI)
    disciplinaDoAluno3 = AlunoDisciplina.create(aluno=joao, disciplina=pgmV)

    for mat in AlunoDisciplina.select():
        print(mat)
