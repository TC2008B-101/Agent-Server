import json
import uuid
from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from tablib import Dataset
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

@simulation_bp.route('', methods=['GET'])
def get_all_simulations():
    try:
        data = Dataset(headers=['ID', 'Hora Inicial', 'Hora Final', 'Tiempos de checkpoint'])

        simulations = list(collection.find())
        for simulation in simulations:
            # Convert ObjectId to string
            simulation['_id'] = str(simulation['_id'])
            
            # Access fields directly
            unique_id = simulation.get('_id')
            start = simulation.get('start_time')
            finish = simulation.get('end_time')
            time = simulation.get('total_time')
            
            # Append to dataset
            data.append([unique_id, start, finish, time])

        # Export the data to CSV format and append it to the simulations list
        csv_data = data.export('csv')
        simulations.append(csv_data)
        
        print(simulations)
        return jsonify(simulations), 200
    except Exception as e:
        return jsonify({
            "error": str(e),
            "description": "Unexpected error occurred while fetching simulations.",
        }), 500



@simulation_bp.route('/<string:simulation_id>', methods=['GET'])
def get_simulation(simulation_id):

    try:
        try:
            obj_id = ObjectId(simulation_id)
        except:
            return jsonify({"error": "Invalid simulation_id format or not founded"}), 400

        simulation = collection.find_one({"_id": obj_id})

        if simulation:
            simulation['_id'] = str(simulation['_id'])
            return jsonify(simulation), 200
        else:
            return jsonify({"error": "Simulation not found"}), 404
    except Exception as e:
        return jsonify({
            "error": str(e),
            "description": "Unexpected error occurred while fetching the simulation.",
        }), 500