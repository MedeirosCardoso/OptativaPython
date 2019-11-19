from flask import Flask, render_template, redirect, request
from Veiculo import *
from Rota import *
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__, static_url_path='', static_folder='templates')

msg = ""


@app.route("/")
def inicio():
    return redirect("/incluirReserva")
    # return "Sistema de reservas: <a href=/listarVeiculos>iniciar</a>"


def obterRotas():
    rotasDados = requests.get('http://localhost:4999/listarRotas')
    jsonRotas = rotasDados.json()
    rotas = []
    for rotaJson in jsonRotas:
        r = dict_to_model(Rota, rotaJson)
        rotas.append(r)
    return rotas


def obterVeiculos():
    # obter do back os dados dos veiculos;
    veiculosDados = requests.get('http://localhost:4999/listarVeiculos')
    # converter os dados recebidos para json
    jsonVeiculos = veiculosDados.json()
    veiculos = []
    # percorrer os veiculos em json
    for veiculoJson in jsonVeiculos:
        # converter o veiculo em json para veiculo peewe;
        v = dict_to_model(Veiculo, veiculoJson)
        # adiciona o veiculo convertido a lista de veiculos;
        veiculos.append(v)
    # fornecer a lista de veiculos para o front exibir os veiculos na pagina;
    return veiculos


@app.route("/incluirReserva")
def incluirReserva():
    return render_template('realizarReserva.html', listaVeiculos=obterVeiculos(), listarRotas=obterRotas())

@app.route("/gerenciarVeiculo")
def gerenciarVeiculo():
    global msg
    x = render_template('gerenciarVeiculo.html', listaVeiculos=obterVeiculos(), mensagem=msg)
    msg = ""
    return x

@app.route("/incluirVeiculo", methods=['post'])
def incluirVeiculo():
    placa = request.form["placaVeiculo"]
    marca = request.form["marcaVeiculo"]
    modelo = request.form["modeloVeiculo"]
    observacao = request.form["observacaoVeiculo"]
    dadosJson = {"placa": placa, "marca": marca,
                 "modelo": modelo, "obs": observacao}
    req = requests.post(
        url='http://localhost:4999/incluirVeiculo', json=dadosJson)
    resp = req.json()
    global msg
    msg = "Veiculo cadastrado com sucesso!"
    if resp['mensagem'] != 'ok':
        msg = "Erro!"
    return redirect("/gerenciarVeiculo")


@app.route("/excluirVeiculo")
def excluirVeiculo():
    placaAexcluir = request.args.get("placaExcluir")
    req = requests.get(
        'http://localhost:4999/excluirVeiculo?placaExcluir='+placaAexcluir)
    resp = req.json()
    global msg
    msg = "Veiculo excluido!"
    if resp['mensagem'] != 'ok':
        msg = "Erro!"
    return redirect("/gerenciarVeiculo")

@app.route("/alterarVeiculo", methods=['post'])
def alterarVeiculo():
    

app.run(debug=True)
