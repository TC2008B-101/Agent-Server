import json
from typing import List, Optional
from flask import Blueprint, jsonify, request
from typing import List, Dict, Optional
import requests

agents_bp = Blueprint('agents', __name__)

@agents_bp.route('', methods=['POST'])
def create_agents_pipeline():
    # TODO: VALIDATE THE REQUEST IT MUST HAVE THE FOLLOWING JSON
    # {
    # "name": "string",
    # "startDate": "date",
    # "weatherReaport": "string",
    # "maintenance": "string",
    # "totalTime": "string",
    # }
    print(request.get_json())
    data = request.get_json()

    # Validate and extract all the data from the request
    try:
        [name, startDate, weatherReaport, maintenance, totalTime] = [
            data['name'],
            data['startDate'],
            data['weatherReaport'],
            data['maintenance'],
            data['totalTime'],
        ]

        #TODO: Save the data to the database "agents" table

        #TODO: Execute the agent pipeline with the request data

        #TODO: Return the response from the agent pipeline

        return jsonify({
            "message": "Agent created successfully",
        }), 200

    # TODO: Save the data to the database "routes" table
    except Exception as e:
        return jsonify({
            "error": str(e),
            "description": "Unexpected error occurred.",
        }), 500

# agents_bp = Blueprint('agents', __name__)

# @agents_bp.route('', methods=['POST'])
# def create_graphrag_pipeline():
#     print(request.get_json())
#     data = request.get_json()

#     # Extract all the data from the request
#     # Note: We're not doing anything specific with the data here,
#     # just returning it as per the original code

#     # Uncomment and use if needed:
#     # headers = {
#     #     'Content-Type': 'application/json',
#     #     'Authorization': 'Bearer ' + data['token']
#     # }

#     return jsonify(data), 200