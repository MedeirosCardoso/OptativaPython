class Endereco:
    def __init__(self, cep, logradouro, numero, bairro, municipio, estado):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado

    def __str__(self):
        return "Endereco: " + self.logradouro + ", " + str(self.numero) + " - " + self.bairro + ", " + self.municipio + " - " + self.estado + ", " + str(self.cep)


if __name__ == "__main__":
    end = Endereco(89035100, "Rua abc", 123, "Vila Nova", "Blumenau", "SC")
    print(end)
