import json
from typing import List, Dict, Optional
from flask import Blueprint, jsonify, request
import logging
import requests

agents_bp = Blueprint('agents', __name__)

# Configura el logger para este modulo
logger = logging.getLogger(__name__)

@agents_bp.route('', methods=['POST'])
def create_graphrag_pipeline():
    try:
        data = request.get_json()
        logger.info(f"Datos recibidos para create_graphrag_pipeline: {data}")

        # headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Bearer ' + data['token']
        # }   

        return jsonify(data), 200
    except Exception as e:
        logger.error(f"Error en create_graphrag_pipeline: {e}")
        return jsonify({"error": "Ocurrió un error al procesar la solicitud."}), 500
