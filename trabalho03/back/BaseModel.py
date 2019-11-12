from peewee import *

arq = '/home/aluno/Documentos/optativaPython/trabalho03/back/BDtrabalho03.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db