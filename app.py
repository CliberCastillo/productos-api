from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
import json
import os

app = Flask(__name__)

# Lista en memoria para almacenar productos
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 999.99},
    {"id": 2, "nombre": "Smartphone", "precio": 599.99}
]

# Función para generar el próximo ID
def get_next_id():
    return max(producto["id"] for producto in productos) + 1 if productos else 1

# GET - Obtener todos los productos con filtros opcionales
@app.route('/productos', methods=['GET'])
def get_productos():
    # Filtros mediante query parameters
    nombre_filtro = request.args.get('nombre', '').lower()
    precio_min = request.args.get('precio_min', None)
    precio_max = request.args.get('precio_max', None)
    
    # Aplicar filtros
    filtrados = productos
    
    if nombre_filtro:
        filtrados = [p for p in filtrados if nombre_filtro in p['nombre'].lower()]
    
    if precio_min:
        try:
            precio_min = float(precio_min)
            filtrados = [p for p in filtrados if p['precio'] >= precio_min]
        except ValueError:
            pass
    
    if precio_max:
        try:
            precio_max = float(precio_max)
            filtrados = [p for p in filtrados if p['precio'] <= precio_max]
        except ValueError:
            pass
    
    return jsonify(filtrados)

# GET - Obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

# POST - Crear un nuevo producto
@app.route('/productos', methods=['POST'])
def create_producto():
    if not request.json or 'nombre' not in request.json:
        return jsonify({"error": "El nombre del producto es obligatorio"}), 400
    
    nuevo_producto = {
        "id": get_next_id(),
        "nombre": request.json['nombre'],
        "precio": request.json.get('precio', 0)
    }
    
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# PATCH - Actualizar parcialmente un producto
@app.route('/productos/<int:producto_id>', methods=['PATCH'])
def update_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    if not request.json:
        return jsonify({"error": "Datos no proporcionados"}), 400
    
    # Actualizar sólo los campos proporcionados
    if 'nombre' in request.json:
        producto['nombre'] = request.json['nombre']
    
    if 'precio' in request.json:
        producto['precio'] = request.json['precio']
    
    return jsonify(producto)

# DELETE - Eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    global productos
    producto = next((p for p in productos if p['id'] == producto_id), None)
    
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    productos = [p for p in productos if p['id'] != producto_id]
    return jsonify({"mensaje": f"Producto con ID {producto_id} eliminado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)