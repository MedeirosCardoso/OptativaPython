from flask import Flask, render_template, request, redirect
from modelo import Veiculo, Rota, Reserva

listaVeiculo=[]
listaRota=[]
listaReservas=[]

app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def realizarReserva():
    return render_template('realizarReserva.html',listaVeiculo = listaVeiculo)

@app.route("/gerenciarVeiculo")
def gerenciarVeiculo():
    return render_template('gerenciarVeiculo.html',listaVeiculo = listaVeiculo)

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
    return render_template('gerenciarReserva.html',listaReservas = listaReservas)

@app.route("/incluirReserva", methods=['post'])
def incluirReserva():
    placa = request.form["veiculo"]
    data = request.form["dataAgendamento"]
    horario = request.form["horarioSaida"]
    rota = request.form["destinoViagem"]
    obsMotorista = request.form["motorista"]
    nova=Reserva(placa,data,horario,rota,obsMotorista)
    listaReservas.append(nova)
    return redirect("/")

@app.route("/cadastrarRota")
def cadastrarRota():
    return render_template('cadastrarRota.html',listaRota = listaRota)

@app.route("/incluirRota", methods=['post'])
def incluirRota():
    codRota = request.form["codRota"]
    partida = request.form["partida"]
    destino = request.form["destino"]
    novaRota = Rota(codRota,partida,destino)
    listaRota.append(novaRota)
    return redirect("/cadastrarRota")

@app.route("/imgMapaNavegacao")
def imgMapaNavegacao():
    return render_template('imgMapaNavegacao.html')
    
app.run(debug=True)