from Veiculo import Veiculo
from Servico import Servico
from Produto import Produto
from peewee import *
from BaseModel import *
from datetime import *
import os


class Manutencao(BaseModel):
    veiculo = ForeignKeyField(Veiculo)
    servicos = ManyToManyField(Servico)
    produtos = ManyToManyField(Produto)
    data = DateField()

    def __str__(self):
        return "Manutenção do veiculo: " + str(self.veiculo.placa) + " - Data: " + self.data.strftime('%d/%m/%Y')


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Veiculo, Servico, Produto, Manutencao, Manutencao.servicos.get_through_model(
    ), Manutencao.produtos.get_through_model()])

    v1 = Veiculo.create(placa="ABC-0000", marca="GM",
                        modelo="Onix", observacao="")
    man = Manutencao.create(veiculo=v1, data=date.today())

    servA = Servico.create(
        codServico="s001", descServico="Alinhamento e balanceamento", custoServico=99.99)
    servB = Servico.create(
        codServico="s002", descServico="Troca do oleo", custoServico=19.99)
    servC = Servico.create(
        codServico="s003", descServico="Regulagem dos farois", custoServico=49.00)
    prodA = Produto.create(
        codProduto="p001", descProduto="Pneu R14", qtdProduto=4, custoProduto=199.99)
    prodB = Produto.create(
        codProduto="p001", descProduto="Oleo W40", qtdProduto=5, custoProduto=19.99)

    man.servicos.add([servA, servB, servC])
    man.produtos.add([prodA, prodB])

    print(man)
    print("lista de serviços: ")
    for servico in man.servicos:
        print(servico.descServico)

    print("lista de produtos: ")
    for produto in man.produtos:
        print(produto.descProduto)

    print("---------------------------")
    todos = Manutencao.select()
    for manu in todos:
        print("VEICULO: "+manu.veiculo.placa)
        for serv in manu.servicos:
            print(serv.descServico)
        for prod in manu.produtos:
            print(prod.descProduto)
