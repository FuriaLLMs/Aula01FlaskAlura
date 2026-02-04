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

def test_login(client):
    rv = client.post('/login')
    assert rv.status_code == 200
    assert rv.json == {"message": "Realizar o login"}

def test_get_products(client):
    rv = client.get('/products')
    assert rv.status_code == 200
    assert rv.json == {"message": "Esta é a rota de listagem dos produtos"}

def test_create_product(client):
    rv = client.post('/products')
    assert rv.status_code == 200
    assert rv.json == {"message": "Esta é a rota de criação de produto"}

def test_get_product_by_id(client):
    product_id = 1
    rv = client.get(f'/product/{product_id}')
    assert rv.status_code == 200
    assert rv.json == {"message": f"Esta é a rota de visualizacao do detalhe do id do produto {product_id}"}

def test_update_product(client):
    product_id = 1
    rv = client.put(f'/product/{product_id}')
    assert rv.status_code == 200
    assert rv.json == {"message": f"Esta é a rota de atualizacao do produto com o id {product_id}"}

def test_delete_product(client):
    product_id = 1
    rv = client.delete(f'/product/{product_id}')
    assert rv.status_code == 200
    assert rv.json == {"message": f"Esta é a rota de deleção do produto com o id {product_id}"}

def test_upload_sales(client):
    rv = client.post('/sales/upload')
    assert rv.status_code == 200
    assert rv.json == {"message": "Esta é a rota de upload do arquivo de vendas"}
