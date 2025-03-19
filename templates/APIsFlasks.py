'''
Template
Útil para: Criar APIs Web rapidamente
'''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "Bem-vindo à API!"})

if __name__ == "__main__":
    app.run(debug=True)
