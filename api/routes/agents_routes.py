import json
from typing import List, Optional
from flask import Blueprint, jsonify, request
from typing import List, Dict, Optional
import requests

agents_bp = Blueprint('agents', __name__)


@agents_bp.route('', methods=['POST'])
def create_graphrag_pipeline():

    print   (request.get_json())
    data = request.get_json()

    # headers = {
    #     'Content-Type': 'application/json',
    #     'Authorization': 'Bearer ' + data['token']
    # }   

    return jsonify(data), 200