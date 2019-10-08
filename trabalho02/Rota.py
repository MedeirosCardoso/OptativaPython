from peewee import *
from BaseModel import *
import os

class Rota(BaseModel):
    codRota = CharField()
    partida = CharField()
    destino = CharField()

    def __str__(self):
        return self.codRota + ": " + self.partida + ", " + self.destino


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Rota])
    r1 = Rota.create(codRota = "Rota001", partida = "Blumenau", destino = "Gaspar")
    print(r1)
