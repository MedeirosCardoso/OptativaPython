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