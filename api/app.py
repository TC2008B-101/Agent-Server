from flask import Flask, jsonify
from flask_cors import CORS
from os import environ 
from routes import agents_bp

app = Flask(__name__)

app.register_blueprint(agents_bp, url_prefix='/api/agents')

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
