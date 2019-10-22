from peewee import *
from Endereco import Endereco
from Rota import Rota
from Veiculo import Veiculo
from Rota import Rota
from Motorista import Motorista
from BaseModel import *
from datetime import *
import os


class Reserva(BaseModel):
    veiculo = ForeignKeyField(Veiculo)
    rota = ForeignKeyField(Rota)
    motorista = ForeignKeyField(Motorista)
    data = DateField()

    def __str__(self):
        toString = "Reserva do veiculo: " + \
            str(self.veiculo.placa) + " data: " + \
            self.data.strftime('%d/%m/%Y') + " - " + str(self.rota.codRota)
        if self.motorista:
            toString += ", com motorista: " + str(self.motorista.nome)
        return toString


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()
    db.create_tables([Veiculo, Endereco, Motorista, Reserva, Rota])

    end = Endereco.create(cep=89035100, logradouro="Rua abc", numero=123, bairro="Vila Nova", municipio="Blumenau", estado="SC")
    veic = Veiculo.create(placa="ABC-0000", marca="GM", modelo="Onix", observacao="")
    rot = Rota.create(codRota="Rota001", partida="Blumenau", destino="Gaspar")
    mot = Motorista.create(nome="Joao da silva", endereco=end, email="manda@gmail.com", matricula="D001", catCNH="categoria D")
    res = Reserva.create(veiculo=veic, data=date.today(), rota=rot, motorista=mot)

    #Id da primeira reserva;
    id=1

    #Obter a reserva original;
    reservaRetornada = Reserva.get_by_id(id)
    print(reservaRetornada,"- Reserva original")
    
    #Altera o veiculo da reserva original;
    reservaRetornada.veiculo = Veiculo.create(placa="DEF-0001", marca="VW", modelo="Gol", observacao="cambio manual")
    #Altera a data da reserva original;
    reservaRetornada.data = date(2019, 10, 31)
    #Atualiza as informações da reserva original;
    reservaRetornada.save()

    #Busca a reserva com os dados alterados;
    reservaRetornada = Reserva.get_by_id(id)
    print(reservaRetornada,"- Reserva alterada")

    #Deleta a primeira reserva
    Reserva.delete_by_id(id)