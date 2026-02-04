from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({"message": "Bem vindo ao Stylesync!"})

@main_bp.route('/products')
def get_products():
    return jsonify({"message": "Esta é a rota de listagem dos produtos"})

@main_bp.route('/login', methods=['POST'])
def login():
    # Se tentar acessar via navegador (GET), dará erro 405 (Method Not Allowed)
    return jsonify({"message": "Login realizado com sucesso"})
