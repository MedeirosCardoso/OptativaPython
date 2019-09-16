from Profissional import Profissional
from Servico import Servico
from Produto import Produto
from Cliente import Cliente


class Atendimento:
    def __init__(self, codAtendimento='', cliente=None, profissional=None, servico=None, produto=None):
        self.codAtendimento = codAtendimento
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.produto = produto

    def __str__(self):
        toString = "\nAtendimento: "+self.codAtendimento + \
            str(self.cliente)+str(self.profissional)+str(self.servico)
        if self.produto:
            toString += str(self.produto)
        return toString


if __name__ == "__main__":
    cli = Cliente("99999999", "Maria")
    prof = Profissional("123", "Joao", "Mecanico")
    ser = Servico("01", "Troca de oleo")
    prod = Produto("01", "Oleo")
    aten = Atendimento("001", cli, prof, ser, prod)
    print(aten)
