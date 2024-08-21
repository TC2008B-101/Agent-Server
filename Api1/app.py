from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models import db, Producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

class ProductoResource(Resource):
    def get(self, producto_id=None):
        if producto_id:
            producto = Producto.query.get_or_404(producto_id)
            return jsonify(producto.to_dict())
        productos = Producto.query.all()
        return jsonify([p.to_dict() for p in productos])

    def post(self):
        data = request.get_json()
        nuevo_producto = Producto(nombre=data['nombre'], precio=data['precio'])
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify(nuevo_producto.to_dict()), 201

    def put(self, producto_id):
        producto = Producto.query.get_or_404(producto_id)
        data = request.get_json()
        producto.nombre = data['nombre']
        producto.precio = data['precio']
        db.session.commit()
        return jsonify(producto.to_dict())

    def delete(self, producto_id):
        producto = Producto.query.get_or_404(producto_id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204

api.add_resource(ProductoResource, '/productos', '/productos/<int:producto_id>')

if __name__ == '__main__':
    app.run(debug=True)



