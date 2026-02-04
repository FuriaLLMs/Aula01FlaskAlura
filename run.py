from app import create_app

app = create_app()

if __name__ == '__main__':
    # No Manjaro, certifique-se de que seu venv está ativo
    app.run(debug=True)
