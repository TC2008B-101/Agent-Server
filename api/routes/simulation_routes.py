import json
from flask import Blueprint, jsonify, request
from jsonschema import validate, ValidationError
# from agents.trailerSim import trailer_sim_handler # Assuming that it'll be created as this
from api.app import collection

simulation_bp = Blueprint('simulation', __name__)

schema = {
    "type": "object",
    "properties": {
        "simulation_id": {"type": "integer"},
        "route_name": {"type": "string"},
        "start_time": {"type": "integer"},
        "weather": {"type": "integer"},
        "maintenance": {"type": "number"},
        "total_time": {"type": "integer"},
        "end_time": {"type": "integer"},
        "coordinates": {"type": "array"},
        "segment": {"type": "array"},
    },
    "required": ["simulation_id", "route_name", "start_time", "weather", "maintenance", "total_time", "end_time", "coordinates", "segment"]
}

@simulation_bp.route('', methods=['POST'])
def generate_simulation_pipeline():

    # JSON Validation
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    # Main-Pipeline (Agent execution, database backup and returned response)
    try:
        # simulation_result = trailer_sim_handler(data)
        collection.insert_one(data)

        return jsonify({
            "message": "Data-simulation generated successfully",
            # "simulation_result": simulation_result 
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "description": "Unexpected error occurred.",
        }), 500