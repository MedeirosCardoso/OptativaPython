from flask import Flask, jsonify, render_template, request, redirect
from playhouse.shortcuts import model_to_dict
from Veiculo import *
from Rota import *
from Reserva import *

listaReservas=[]

app=Flask(__name__)

@app.route("/")
def inicio():
    return "Servidor de api backend<a href=/listarVeiculos>listar</a>"

@app.route("/incluirReserva")
def incluirReserva():
    pass

@app.route("/listarVeiculos")
def listarVeiculos():
    veiculos = list(map(model_to_dict,Veiculo.select()))
    return jsonify(veiculos)

@app.route("/listarRotas")
def listarRotas():
    rotas = list(map(model_to_dict,Rota.select()))
    return jsonify(rotas)

app.run(debug=True,port=4999)