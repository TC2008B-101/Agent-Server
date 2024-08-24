from flask import Flask, jsonify
from flask_cors import CORS
from os import environ
from routes import agents_bp
import logging

# Configura el logging
logging.basicConfig(level=logging.INFO,  # Cambia a DEBUG para mayor detalle
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(agents_bp, url_prefix='/api/agents')
CORS(app)

@app.errorhandler(Exception)
def handle_error(e):
    logger.error(f"Error inesperado: {e}")
    response = {
        "error": str(e),
        "description": "Unexpected error occurred."
    }
    return jsonify(response), 500

@app.route('/api/')
def root():
    logger.info("Ruta /api/ accedida")
    return jsonify(message="Hello, /")

if __name__ == "__main__":
    logger.info("Servidor iniciado")
    app.run(debug=environ.get('DEBUG', False), host='0.0.0.0')
