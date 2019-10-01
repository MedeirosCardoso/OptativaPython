class Veiculo:
    def __init__(self, placa, marca, modelo, observacao):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.observacao = observacao

    def __str__(self):
        return "Placa: " + self.placa + ", " + self.marca + ", " + self.modelo + ", " + self.observacao


if __name__ == "__main__":
    v1 = Veiculo("ABC-0000", "GM", "Onix", "")
    v2 = Veiculo("DEF-0001", "VW", "Gol", "veiculo cambio manual")
    print(v1)
    print(v2)
