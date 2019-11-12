from peewee import *
from BaseModel import *
import os

class Veiculo(BaseModel):
    placa = CharField(primary_key=True)
    marca = CharField()
    modelo = CharField()
    observacao = CharField()

    def __str__(self):
        return "Placa: " + self.placa + ", " + self.marca + ", " + self.modelo + ", " + self.observacao


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Veiculo])
    v1 = Veiculo.create(placa = "ABC-0000", marca = "GM", modelo = "Onix", observacao = "")
    print(v1)
