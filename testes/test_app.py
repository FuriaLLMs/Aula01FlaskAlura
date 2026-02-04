import pytest
import sys
import os

# Adiciona o diretório raiz ao path para importar 'app' corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.json == {"message": "Bem-vindo à API da StyleSync!"}

def test_products(client):
    rv = client.get('/products')
    assert rv.status_code == 200
    assert rv.json == {"message": "Esta é a rota de listagem dos produtos"}

def test_login_post(client):
    rv = client.post('/login')
    assert rv.status_code == 200
    assert rv.json == {"message": "Login realizado com sucesso"}

def test_login_get_405(client):
    rv = client.get('/login')
    assert rv.status_code == 405
