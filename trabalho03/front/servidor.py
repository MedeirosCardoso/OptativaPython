from flask import Flask, render_template, redirect
from Veiculo import *
from Rota import *
import requests
from playhouse.shortcuts import dict_to_model

app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def inicio():
    return redirect("/listarVeiculos")
    #return "Sistema de reservas: <a href=/listarVeiculos>iniciar</a>"

@app.route("/incluirReserva")
def incluirReserva():
    pass

@app.route("/listarVeiculos")
def listarVeiculos():
    #obter do back os dados dos veiculos;
    veiculosDados = requests.get('http://localhost:4999/listarVeiculos')
    #converter os dados recebidos para json
    jsonVeiculos = veiculosDados.json()
    veiculos=[]
    #percorrer os veiculos em json
    for veiculoJson in jsonVeiculos:
        #converter o veiculo em json para veiculo peewe;
        v = dict_to_model(Veiculo, veiculoJson)
        #adiciona o veiculo convertido a lista de veiculos;
        veiculos.append(v)
    #fornecer a lista de veiculos para o front exibir os veiculos na pagina;
    #return redirect("/")
    return render_template('realizarReserva.html',listaVeiculos=veiculos)

@app.route("/listarRotas")
def listarRotas():
    rotasDados = requests.get('http://localhost:4999/listarRotas')
    jsonRotas = rotasDados.json()
    rotas=[]
    for rotaJson in jsonRotas:
        r = dict_to_model(Rota, rotaJson)
        rotas.append(r)
    return render_template('realizarReserva.html',listaRotas=rotas)

app.run(debug=True)