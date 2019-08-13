from flask import Flask, render_template
app=Flask(__name__, static_url_path='',static_folder='templates')

@app.route("/")
def realizarReserva():
    return render_template('realizarReserva.html')

@app.route("/gerenciarVeiculo")
def gerenciarVeiculo():
    return render_template('gerenciarVeiculo.html')

@app.route("/gerenciarReserva")
def gerenciarReserva():
    return render_template('gerenciarReserva.html')

@app.route("/cadastrarRota")
def cadastrarRota():
    return render_template('cadastrarRota.html')

@app.route("/imgMapaNavegacao")
def imgMapaNavegacao():
    return render_template('imgMapaNavegacao.html')
    
app.run()