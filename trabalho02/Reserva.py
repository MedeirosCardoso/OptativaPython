from Veiculo import Veiculo
from Rota import Rota
from Motorista import Motorista


class Reserva:
    def __init__(self, veiculo, data, horario, rota, motorista):
        self.Veiculo = veiculo
        self.data = data
        self.horario = horario
        self.Rota = rota
        self.Motorista = motorista

    def __str__(self):
        toString = "Reserva do veiculo: " + str(self.Veiculo.placa) + " data: " + self.data + "-" + \
            self.horario + ", " + str(self.Rota.codRota)
        if self.Motorista:
            toString += ", com motorista: " + str(self.Motorista.nome)
        return toString


if __name__ == "__main__":
    v1 = Veiculo("ABC-0000", "GM", "Onix", "")
    r1 = Rota("Rota001", "Blumenau", "Gaspar")
    mot = Motorista("Joao da silva", None, "manda@gmail.com", "D001", "categoria D")
    rs1 = Reserva(v1, "01/01/2019", "10:00", r1, mot)
    print(rs1)
