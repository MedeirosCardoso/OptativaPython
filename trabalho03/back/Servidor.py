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


@app.route("/incluirReserva")
def incluirReserva():
    pass


@app.route("/listarVeiculos")
def listarVeiculos():
    veiculos = list(map(model_to_dict, Veiculo.select()))
    return jsonify(veiculos)


@app.route("/listarRotas")
def listarRotas():
    rotas = list(map(model_to_dict, Rota.select()))
    return jsonify(rotas)


@app.route("/incluirVeiculo", methods=['post'])
def incluirVeiculo():
    msg = jsonify({"mensagem": "ok"})
    dados = request.get_json(force=True)
    placa = dados['placa']
    marca = dados['marca']
    modelo = dados['modelo']
    observacao = dados['obs']
    Veiculo.create(placa=placa, marca=marca,
                   modelo=modelo, observacao=observacao)
    return msg


@app.route("/excluirVeiculo")
def excluirVeiculo():
    msg = jsonify({"mensagem": "ok"})
    placaAexcluir = request.args.get("placaExcluir")
    Veiculo.delete_by_id(placaAexcluir)
    return msg

@app.route("/alterarVeiculo", methods=['post'])
def alterarVeiculo():
     msg = jsonify({"mensagem": "ok"})
     dados = request.get_json(force=True)
     placa = dados['placa']
     marca = dados['marca']
     modelo = dados['modelo']
     observacao = dados['obs']
     veiculoDadosOriginal = Veiculo.get_by_id(placa)
     veiculoDadosOriginal.placa = placa
     veiculoDadosOriginal.marca = marca
     veiculoDadosOriginal.modelo = modelo
     veiculoDadosOriginal.observacao = observacao
     veiculoDadosOriginal.save()
     return msg

app.run(debug=True, port=4999)
