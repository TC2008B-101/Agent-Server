from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from tablib import Dataset
from jsonschema import validate, ValidationError
from Agents.trailerSim import trailer_sim_handler # Assuming that it'll be created as this
from commons.db import collection

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

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    try:
        simulation_result = trailer_sim_handler(data)
        collection.insert_one(simulation_result)
        return jsonify({
            "message": "Data-simulation generated successfully",
            # "simulation_result": simulation_result 
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
            simulation['_id'] = str(simulation['_id'])
            unique_id, start, time, finish = simulation.values()
            data.append([unique_id, start, finish, time])
    
        simulations.append(data.export('csv'))

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