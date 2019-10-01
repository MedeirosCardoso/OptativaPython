class Rota:
    def __init__(self, codRota, partida, destino):
        self.codRota = codRota
        self.partida = partida
        self.destino = destino

    def __str__(self):
        return self.codRota + ": " + self.partida + ", " + self.destino


if __name__ == "__main__":
    r1 = Rota("Rota001", "Blumenau", "Gaspar")
    r2 = Rota("Rota002", "Blumenau", "Brusque")
    print(r1)
    print(r2)
