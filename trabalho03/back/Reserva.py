from peewee import *
from Veiculo import Veiculo
from Rota import Rota
from BaseModel import *
from datetime import *
import os


class Reserva(BaseModel):
    veiculo = ForeignKeyField(Veiculo)
    rota = ForeignKeyField(Rota)
    data = DateField()

    def __str__(self):
        toString = "Reserva do veiculo: " + \
            str(self.veiculo.placa) + " data: " + self.data.strftime('%d/%m/%Y') + " - " + str(self.rota)
        return toString


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Veiculo, Reserva, Rota])

    veic = Veiculo.create(placa="ABC-0000", marca="GM", modelo="Onix", observacao="")
    rot = Rota.create(partida="Blumenau", destino="Gaspar")
    res = Reserva.create(veiculo=veic, data=date(2019, 11, 30), rota=rot)
    print(res)