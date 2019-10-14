from peewee import *
from BaseModel import *
import os

class Servico(BaseModel):
    codServico = CharField()
    descServico = CharField()
    custoServico = FloatField()

    def __str__(self):
        return "Código: " + self.codServico + ", Descrição: " + self.descServico + ", Custo R$" + str(self.custoServico)

if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Servico])
    serv = Servico.create(codServico="s001", descServico = "Alinhamento e balanceamento", custoServico = 99.99)
    print(serv)