from flask import Flask, render_template, request
from modelo import Pessoa
app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def listarPessoas():
    p1=Pessoa("Joao da Silva","Rua A, 01","999999999")
    p2=Pessoa("Maria Oliveira","Rua B, 02"," ")
    p3=Pessoa("Paulo","Rua C, 03","888888888 ")
    lista=[p1,p2,p3]
    return render_template('listaPessoas.html',pessoas=lista)

@app.route("/formIncluirPessoa")
def abreFormularioIncluirPessoa():
    return render_template('formIncluirPessoa.html')

@app.route("/incluirPessoa")
def incluirPessoa():
    nome=request.args.get("nome")
    endereco=request.args.get("endereco")
    telefone=request.args.get("telefone")
    #Montar mensagem de resposta#
    mensagem = "Os seguintes dados do formulário foram recebidos: "
    mensagem += nome+", " + endereco + ", " + telefone
    return render_template('formIncluirPessoa.html', msn=mensagem)

app.run()