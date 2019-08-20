class Pessoa:
    def __init__ (self, nome, endereco, telefone):
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone
if __name__=="__main__":
    p1=Pessoa("Joao da Silva","Rua A, 01","999999999")
    p2=Pessoa("Maria Oliveira","Rua B, 02"," ")
    p3=Pessoa("Paulo","Rua C, 03","888888888 ")
    print(p1.nome+", "+p1.endereco,","+p1.telefone)