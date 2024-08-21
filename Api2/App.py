from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

# Ruta para obtener todos los items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Ruta para obtener un item por su ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Ruta para crear un nuevo item
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Ruta para actualizar un item existente
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        data = request.get_json()
        item.update(data)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Ruta para eliminar un item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
