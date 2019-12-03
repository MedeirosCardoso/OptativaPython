from flask import Flask, jsonify, render_template, request, redirect
from playhouse.shortcuts import model_to_dict
from Veiculo import *
from Rota import *
from Reserva import *

listaReservas = []

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Servidor de api backend<a href=/listarVeiculos>listar</a>"


@app.route("/incluirReserva", methods=['post'])
def incluirReserva():
    msg = jsonify({"mensagem": "ok"})
    dados = request.get_json(force=True)
    idReserva = 0
    try:
        idReserva = dados['id']
    except: # Exception as e:
        pass
    placa = dados['placa']
    idRota = dados['idRota']
    data = dados['data']
    query = Reserva.select().where(Reserva.id == idReserva)
    if query.exists():
        reservaDadosOriginal = Reserva.get_by_id(idReserva)
        reservaDadosOriginal.veiculo = Veiculo.get_by_id(placa)
        reservaDadosOriginal.rota = Rota.get_by_id(idRota)
        reservaDadosOriginal.save()
    else:
        veiculo = Veiculo.get_by_id(placa)
        rota = Rota.get_by_id(idRota)
        Reserva.create(veiculo=veiculo, data=data, rota=rota)
    return msg

@app.route("/excluirReserva")
def excluirReserva():
    msg = jsonify({"mensagem": "ok"})
    reservaAexcluir = request.args.get("reservaExcluir")
    Reserva.delete_by_id(reservaAexcluir)
    return msg

@app.route("/listarVeiculos")
def listarVeiculos():
    veiculos = list(map(model_to_dict, Veiculo.select()))
    return jsonify(veiculos)

@app.route("/listarRotas")
def listarRotas():
    rotas = list(map(model_to_dict, Rota.select()))
    return jsonify(rotas)

@app.route("/listarReservas")
def listarReservas():
    reservas = list(map(model_to_dict, Reserva.select()))
    return jsonify(reservas)

@app.route("/consultarReserva")
def consultarReserva():
    msg = jsonify({"mensagem": "ok"})
    id = request.args.get("id")
    reserva = Reserva.get_by_id(id)
    msg = jsonify({"mensagem": "ok","data":model_to_dict(reserva)})
    return msg

@app.route("/incluirVeiculo", methods=['post'])
def incluirVeiculo():
    msg = jsonify({"mensagem": "ok"})
    dados = request.get_json(force=True)
    placa = dados['placa']
    marca = dados['marca']
    modelo = dados['modelo']
    observacao = dados['obs']
    query = Veiculo.select().where(Veiculo.placa == placa)
    if query.exists():
        veiculoDadosOriginal = Veiculo.get_by_id(placa)
        veiculoDadosOriginal.placa = placa
        veiculoDadosOriginal.marca = marca
        veiculoDadosOriginal.modelo = modelo
        veiculoDadosOriginal.observacao = observacao
        veiculoDadosOriginal.save()
    else:
        Veiculo.create(placa=placa, marca=marca,modelo=modelo, observacao=observacao)
    return msg

@app.route("/excluirVeiculo")
def excluirVeiculo():
    msg = jsonify({"mensagem": "ok"})
    placaAexcluir = request.args.get("placaExcluir")
    Veiculo.delete_by_id(placaAexcluir)
    return msg

@app.route("/consultarVeiculo")
def consultarVeiculo():
    msg = jsonify({"mensagem": "ok"})
    placa = request.args.get("placa")
    veiculo = Veiculo.get_by_id(placa)
    msg = jsonify({"mensagem": "ok","data":model_to_dict(veiculo)})
    return msg

@app.route("/incluirRota", methods=['post'])
def incluirRota():
    msg = jsonify({"mensagem": "ok"})
    dados = request.get_json(force=True)
    partida = dados['partida']
    destino = dados['destino']
    Rota.create(partida = partida, destino = destino)
    return msg

app.run(debug=True, port=4999)
