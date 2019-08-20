from flask import Flask, render_template, request, redirect
from modelo import Veiculo

listaVeiculo=[]

app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def realizarReserva():
    return render_template('realizarReserva.html')

@app.route("/gerenciarVeiculo")
def gerenciarVeiculo():
    return render_template('gerenciarVeiculo.html', listaVeiculo = listaVeiculo)

@app.route("/incluirVeiculo", methods=['post'])
def incluirVeiculo():
    placa = request.form["placaVeiculo"]
    marca = request.form["marcaVeiculo"]
    modelo = request.form["modeloVeiculo"]
    observacao = request.form["observacaoVeiculo"]
    novo = Veiculo(placa,marca,modelo,observacao)
    listaVeiculo.append(novo)
    return redirect("/gerenciarVeiculo")

@app.route("/gerenciarReserva")
def gerenciarReserva():
    return render_template('gerenciarReserva.html')

@app.route("/cadastrarRota")
def cadastrarRota():
    return render_template('cadastrarRota.html')

@app.route("/imgMapaNavegacao")
def imgMapaNavegacao():
    return render_template('imgMapaNavegacao.html')
    
app.run(debug=True)