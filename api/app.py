from os import environ 
from flask import Flask, jsonify
from flask_cors import CORS
from api.routes.simulation_routes import simulation_bp

app = Flask(__name__)
app.register_blueprint(simulation_bp, url_prefix='/api/simulation')
CORS(app)

@app.errorhandler(Exception)
def handle_error(e):
    response = {
        "error": str(e),
        "description": "Unexpected error occurred."
    }
    return jsonify(response), 500

@app.route('/api/')
def root():
    return jsonify(message="Hello, /")