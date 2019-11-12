from peewee import *
from BaseModel import *

class Rota(BaseModel):
    partida = CharField()
    destino = CharField()

    def __str__(self):
        return "Cod: "+str(self.id)+" - Rota: " + self.partida + ", " + self.destino


if __name__ == "__main__":
    db.connect()
    db.create_tables([Rota])
    r1 = Rota.create(partida = "Blumenau", destino = "Gaspar")
    print(r1)