import os

class Config:
    # Tenta ler de uma variável de ambiente do Linux, senão usa a string padrão
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-bem-dificil'
