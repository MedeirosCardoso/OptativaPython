from flask import Flask, jsonify, render_template, request, redirect
from modelo import Pessoa
import requests
from playhouse.shortcuts import dict_to_model, model_to_dict

pessoas = []

app = Flask(__name__)

@app.route("/")
def inicio():
    return "frontend do sistema de pessoas. <a href=/listar_pessoas>Operação listar</a>"

@app.route("/listar_pessoas")
def listar_pessoas():

    dados_pessoas = requests.get('http://localhost:4999/listar_pessoas')

    json_pessoas = dados_pessoas.json()

    for pessoa_em_json in json_pessoas['lista']:
        p = dict_to_model(Pessoa, pessoa_em_json)
        pessoas.append(p)
    
    return render_template("listar_pessoas.html", lista = pessoas)

@app.route("/incluir_pessoa")
def incluir_pessoa():
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    email = request.args.get("email")
    nova = Pessoa.create(nome=nome, endereco=endereco, telefone=telefone, email=email)

    # converte a pessoa em peewee para json
    pessoa_json = model_to_dict(Pessoa, nova)

    # envia a pessoa nova em json para o backend cadastrar (chamada post)
    resultado = requests.get('http://localhost:4999/incluir_pessoa', params=pessoa_json)

    return resultado
    # analisa o resultado e mostra se deu certo ou não

app.run(debug=True)