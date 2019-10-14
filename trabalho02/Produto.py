from peewee import *
from BaseModel import *
import os


class Produto(BaseModel):
    codProduto = CharField()
    descProduto = CharField()
    custoProduto = FloatField()
    qtdProduto = FloatField()

    def __str__(self):
        return "Código: " + self.codProduto + ", Descrição: " + self.descProduto + " - qtd: " + str(self.qtdProduto)+", Custo R$" + str(self.custoProduto)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Produto])
    prod = Produto.create(
        codProduto="p001", descProduto="Pneu R14", qtdProduto=4, custoProduto=199.99)
    print(prod)
