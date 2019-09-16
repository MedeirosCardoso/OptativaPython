class Servico:
    def __init__(self, cod='', descServico=''):
        self.descServico = descServico
        self.cod = cod

    def __str__(self):
        return "\nServico: "+self.cod+" - "+self.descServico


if __name__ == "__main__":
    s = Servico("01", "Troca de oleo")
    print(s)
