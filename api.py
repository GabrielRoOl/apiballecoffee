from flask import Flask, jsonify

app = Flask(__name__)

# Dados das receitas de cafés
receitas_cafes = [
    {"nome": "Expresso", "ingredientes": ["água", "pó de café"], "instrucoes": "Use máquina de café expresso."},
    {"nome": "Café Americano", "ingredientes": ["água", "pó de café"], "instrucoes": "Misture água quente com café expresso."},
    {"nome": "Cappuccino", "ingredientes": ["água', "pó de café", "chocolate em pó", "creme de leite" "leite", "açucar"], "instruções": "Misture água quente com o pó de café e açucar, adicione leite quente, creme de leite e o chocolate em pó."},
    # Adicione mais 7 receitas aqui
]

# Rota para listar todas as receitas de cafés
@app.route('/receitas', methods=['GET'])
def get_receitas():
    return jsonify(receitas_cafes)

# Iniciando o servidor
if __name__ == '__main__':
    app.run()
