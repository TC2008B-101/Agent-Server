import json
import uuid
from flask import Blueprint, jsonify, request
from jsonschema import validate, ValidationError
from Agents.trailerSim import start_simulation  
from commons.db import collection


simulation_bp = Blueprint('simulation', __name__)

schema = {
    "type": "object",
    "properties": {
        
        "route_name": {"type": "string"},
        "start_time": {"type": "integer"},
        "weather": {"type": "string"},
        "maintenance": {"type": "number"},
        "total_time": {"type": "integer"},
        "end_time": {"type": "integer"},
        "coordinates": {"type": "array"},
        "segment": {"type": "array"},
    },
    "required": ["route_name", "start_time", "weather", "maintenance", "total_time", "end_time", "coordinates", "segment"]
}

#TODO: CREATE A NEW PARAMETER SIMULATION_ID AND ADD IT TO THE JSON
#TODO: THE GENERATED ID SHOULD BE UUID 
#TODO: IN THE RESPONSE RETURN ALSO THE GENERATED SIMULATION_ID

@simulation_bp.route('', methods=['POST'])
def generate_simulation_pipeline():
    # JSON Validation
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    try:
        # Validate JSON against schema
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    # Main-Pipeline (Agent execution, database backup and returned response)
    try:
        # Run the simulation and generate the result
        simulation_result = start_simulation(data)
        
        # Insert the simulation result into MongoDB
        result = collection.insert_one(simulation_result)
        
        # Convert the ObjectId to string before returning it in JSON response
        simulation_result['_id'] = str(result.inserted_id)

        return jsonify({
            "message": "Data-simulation generated successfully",
            "simulation_id": data['simulation_id'], 
            "simulation_result": simulation_result
        }), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "description": "Unexpected error occurred.",
        }), 500



    
#TODO: CREATE ANOTHER ENDPOINT FOR GET THAT RECEIVES THE SIMULATION_ID BY THE PARAMETERS

#TODO: VALIDATE THE PARAMETERS FROM THE REQUEST

#TODO: GET THE SIMULATION OF MONGODB THAT HAS THE SIMULATION_ID

#TODO: RETURN THE SIMULATION JSON