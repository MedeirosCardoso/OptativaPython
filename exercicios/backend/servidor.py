from flask import Flask, jsonify, request
from Pessoa import *
import requests
from playhouse.shortcuts import model_to_dict, dict_to_model

app=Flask(__name__)

@app.route("/")
def inicio():
    return "backend do sistema de pessoas; <a href= /listar_pessoas>API listar pessoas</a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas})

@app.route("/incluir_pessoa")
def incluir_pessoa():

    json_pessoa = request.get_json(force=True)
    print(json_pessoa)
    Pessoa.create(nome=json_pessoa['nome'],
    endereco=json_pessoa['endereco'],
    telefone=json_pessoa['telefone'],
    email=json_pessoa['email'])
    #p=dict_to_model(Pessoa, json_pessoa)
    #p.save()
    return jsonify({"message":"ok"})


app.run(debug=True, port=4999)