import json
from typing import List, Optional
from flask import Blueprint, jsonify, request
from typing import List, Dict, Optional
import requests
from Agents.trailerSim import trailer_sim_handler

agents_bp = Blueprint('agents', __name__)

@agents_bp.route('', methods=['POST'])
def create_agents_pipeline():
    # TODO: VALIDATE THE REQUEST IT MUST HAVE THE FOLLOWING JSON

    print(request.get_json())
    data = request.get_json()

    # Validate the request
    required_fields = ['inicio', 'checkpoints', 'final']
    if not all(field in data for field in required_fields):
        return jsonify({
            "error": "Missing required fields",
            "description": "Please provide 'inicio', 'checkpoints', and 'final' in the request.",
        }), 400

    # Validate and extract all the data from the request
    try:

        #TODO: Execute the agent pipeline with the request data

        simulation_result = trailer_sim_handler(data)

        #TODO: Save the data to the database "agents" table

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