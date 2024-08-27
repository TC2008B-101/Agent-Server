from os import environ 
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from api.routes import simulation_bp
from dotenv import dotenv_values

config = dotenv_values(".env")

uri = config.MONGO_URI
client = MongoClient(uri) 
db = client['simulation_database']
collection = db['simulations']

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

if __name__ == "__main__":
    app.run(debug=environ.get('DEBUG', False), host='0.0.0.0')
