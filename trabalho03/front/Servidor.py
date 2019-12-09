from flask import Flask, render_template, redirect, request
from Veiculo import *
from Rota import *
from Reserva import *
from datetime import *
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__, static_url_path='', static_folder='templates')

msg = []

@app.route("/")
def inicio():
    return redirect("/form_incluirReserva")

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

def obterReservas():
    # obter do back os dados de reservas;
    reservasDados = requests.get('http://localhost:4999/listarReservas')
    # converter os dados recebidos para json;
    jsonReservas = reservasDados.json()
    # cria uma lista de reservas;
    reservas=[]
    # percorrer as reservas em json;
    for reservaJson in jsonReservas:
        # converter a reserva json para reserva peewe;
        r = dict_to_model(Reserva, reservaJson)
        # adiciona a reserva convertida a lista de reservas;
        reservas.append(r)
    # fornecer a lista de reservas para o front exibir na pagina html;    
    return reservas

@app.route("/form_incluirReserva")
def form_incluirReserva():
    x = render_template('realizarReserva.html', listaVeiculos=obterVeiculos(), listaRotas=obterRotas(), mensagem=msg)
    msg.clear()
    return x

# INCLUIR ou ALTERAR, o back decide com base na
# pré-existência ou não da RESERVA;
@app.route("/incluirReserva", methods=['post'])
def incluirReserva():
    idReserva = 0
    try:
        idReserva = request.form["idReserva"]
    except:
        pass
    placa = request.form["veiculo"]
    data = request.form["dataAgendamento"]
    idRota = request.form["rota"]
    dadosJson = {"idReserva": idReserva, "placa": placa, "data": data,"idRota": idRota}
    req = requests.post(url='http://localhost:4999/incluirReserva', json=dadosJson)
    resp = req.json() 
    msg.append("Reserva realizado com sucesso!")
    if resp['mensagem'] != 'ok':
        msg.append("Erro!")
    return redirect("/")

@app.route("/gerenciarReserva")
def gerenciarReserva():
    return render_template('gerenciarReserva.html', listaReservas=obterReservas()) 

# O back consulta se a reserva existe;
# A reserva existe, o back retorna os dados da reserva a ser alterada;
# O front manda a reserva a ser alterada para a pagina realizarReserva.html;
# A pagina realizarReserva.html preenche os inputs com os dados da reservaAalterar;
@app.route("/alterarReserva")
def alterarReserva():
    id = request.args.get("id")
    req = requests.get('http://localhost:4999/consultarReserva?id='+id)
    resp = req.json()
    if resp['mensagem'] == 'ok':
        reservaAalterar=dict_to_model(Reserva,resp['data'])
        x = reservaAalterar.data
        y = datetime.strptime(x, '%a, %d %b %Y %H:%M:%S GMT').date()
        z = y.strftime('%Y-%m-%d')
        reservaAalterar.data = str(z)
        return render_template('realizarReserva.html', reservaAalterar = reservaAalterar, listaVeiculos=obterVeiculos(), listaRotas=obterRotas(), op = 'alterar')
    else:
        return redirect("/")

@app.route("/excluirReserva")
def excluirReserva():
    id = request.args.get("id")
    requests.get('http://localhost:4999/excluirReserva?reservaExcluir='+id)
    return redirect("/gerenciarReserva")

@app.route("/gerenciarVeiculo")
def gerenciarVeiculo():
    return render_template('gerenciarVeiculo.html', listaVeiculos=obterVeiculos()) 

# INCLUIR ou ALTERAR, o back decide com base na
# pré-existência ou não da RESERVA;
@app.route("/incluirVeiculo", methods=['post'])
def incluirVeiculo():
    placa = request.form["placaVeiculo"]
    marca = request.form["marcaVeiculo"]
    modelo = request.form["modeloVeiculo"]
    observacao = request.form["observacaoVeiculo"]
    dadosJson = {"placa": placa, "marca": marca,"modelo": modelo, "obs": observacao}
    requests.post(url='http://localhost:4999/incluirVeiculo', json=dadosJson)
    return redirect("/gerenciarVeiculo")


@app.route("/excluirVeiculo")
def excluirVeiculo():
    placaAexcluir = request.args.get("placaExcluir")
    requests.get('http://localhost:4999/excluirVeiculo?placaExcluir='+placaAexcluir)
    return redirect("/gerenciarVeiculo")

# O back consulta se o veiculo existe;
# O veiculo existe, o back retorna os dados do veiculo a ser alterado;
# O front manda o veiculo a ser alterado para a pagina gerenciarVeiculo.html;
# A pagina gerenciarVeiculo.html preenche os inputs com os dados do veiculoAalterar;
@app.route("/alterarVeiculo")
def alterarVeiculo():
    placaAalterar = request.args.get("placaAlterar")
    req = requests.get('http://localhost:4999/consultarVeiculo?placa='+placaAalterar)
    resp = req.json()
    if resp['mensagem'] == 'ok':
        veiculoAalterar=dict_to_model(Veiculo,resp['data'])
        return render_template('gerenciarVeiculo.html', veiculoAalterar = veiculoAalterar, op = 'alterar')
    else:
        return redirect("/gerenciarVeiculo") 

@app.route("/cadastrarRota")
def cadastrarRota():
    return render_template('cadastrarRota.html',listaRota = obterRotas())

@app.route("/incluirRota", methods=['post'])
def incluirRota():
    partida = request.form["partida"]
    destino = request.form["destino"]
    dadosJson = {"partida": partida, "destino": destino}
    requests.post(url='http://localhost:4999/incluirRota', json=dadosJson)
    return redirect("/cadastrarRota")
 
app.run(debug=True)