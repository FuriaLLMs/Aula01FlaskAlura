from flask import Flask
from .routes.main import main_bp

def create_app():
    app = Flask(__name__)
    
    # Carrega as configurações da classe Config
    app.config.from_object('config.Config')
    
    # Registro de Blueprints
    app.register_blueprint(main_bp)
    
    return app
