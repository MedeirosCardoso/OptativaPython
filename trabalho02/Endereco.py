from peewee import *
from BaseModel import *
import os


class Endereco(BaseModel):
    cep = IntegerField()
    logradouro = CharField()
    numero = IntegerField()
    bairro = CharField()
    municipio = CharField()
    estado = CharField()

    def __str__(self):
        return "Endereco: " + self.logradouro + ", " + str(self.numero) + " - " + self.bairro + ", " + self.municipio + " - " + self.estado + ", " + str(self.cep)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Endereco])
    end = Endereco.create(cep=89035100, logradouro="Rua abc", numero=123,
                            bairro="Vila Nova", municipio="Blumenau", estado="SC")
    print(end)
