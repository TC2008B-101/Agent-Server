import json
from typing import List, Optional
from flask import Blueprint, jsonify, request
from typing import List, Dict, Optional
import requests

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('', methods=['POST'])
def create_routes_pipeline():

    # TODO: VALIDATE THE REQUEST IT MUST HAVE THE FOLLOWING JSON
    # {
    #     "name": "string",
    #     "startDate": "date",
    #     "weatherReaport": "string",
    #     "coordsStart": {
    #       "x": 0,
    #       "y": 0
    #     },
    #     "coordsFinal": {
    #       "x": 0,
    #       "y": 0
    #     },
    # },

    print   (request.get_json())
    data = request.get_json()
    #Extract all the data from the request
    [name, startDate, weatherReaport, coordsStart, coordsFinal] = [data['name'], data['startDate'], data['weatherReaport'], data['coordsStart'], data['coordsFinal']]
    
    #TODO: Save the data to the database "routes" table

    return jsonify({
        "message": "Route created successfully",
    }), 200