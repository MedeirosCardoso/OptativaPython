class Cliente:
    def __init__(self, telefone='', nome='', email=''):
        self.telefone = telefone
        self.nome = nome
        self.email = email

    def __str__(self):
        toString = "\nCliente: "+self.telefone+", "+self.nome
        if self.email:
            toString += ", "+self.email
        return toString


if __name__ == "__main__":
    c1 = Cliente("99999999", "Maria", "mr@hotmail.com")
    print(c1)

    c2 = Cliente("88888888", "Joao")
    print(c2)
