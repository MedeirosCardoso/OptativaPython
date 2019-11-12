class Veiculo:
    def __init__ (self, placa, marca, modelo, observacao):
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.observacao=observacao
if __name__=="__main__":
    v1=Veiculo("ABC-0000","GM","Onix","")
    v2=Veiculo("DEF-0001","VW","Gol","veiculo cambio manual")
    print(v1.placa+", "+v1.marca,","+v1.modelo,", "+v1.observacao)
    print(v2.placa+", "+v2.marca,","+v2.modelo,", "+v2.observacao)

class Rota:
    def __init__ (self, codRota, partida, destino):
        self.codRota=codRota
        self.partida=partida
        self.destino=destino
if __name__=="__main__":
    r1=Rota("Rota001","Blumenau","Gaspar")
    r2=Rota("Rota002","Blumenau","Brusque")
    print(r1.codRota+", "+r1.partida,","+r1.destino)
    print(r2.codRota+", "+r2.partida,","+r2.destino)

class Reserva:
    def __init__ (self,placa, data, horario, rota, obsMotorista):
        self.placa=placa
        self.data=data
        self.horario=horario
        self.rota=rota
        self.obsMotorista=obsMotorista
if __name__=="__main__":
    rs1=Reserva("ABC-0000","01/01/2019","10:00","Rota001","com Motorista")
    print(rs1.placa+", "+rs1.data+", "+rs1.horario+", "+rs1.obsMotorista)        