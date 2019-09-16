class Produto:
    def __init__(self, cod='', descProduto=''):
        self.descProduto = descProduto
        self.cod = cod

    def __str__(self):
        return "\nProduto: "+self.cod+" - "+self.descProduto


if __name__ == "__main__":
    p = Produto("01", "Oleo")
    print(p)
