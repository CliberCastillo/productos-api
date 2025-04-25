# Productos API

A simple RESTful API for managing products built with Flask.

## Description

Productos API is a lightweight RESTful web service that allows you to perform CRUD operations (Create, Read, Update, Delete) on a product catalog. The API stores products in memory and provides filtering capabilities.

## Features

- Get all products with optional filtering by name, minimum price, and maximum price
- Get a single product by ID
- Create new products
- Update existing products
- Delete products

## Technologies

- Python 3.9
- Flask
- Docker
- Kubernetes

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/CliberCastillo/productos-api.git
cd productos-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The API will be available at http://localhost:5000

### Docker

1. Build the Docker image:
```bash
docker build -t productos-api:latest .
```

2. Run the container:
```bash
docker run -p 5000:5000 productos-api:latest
```

### Kubernetes Deployment

1. Apply the Kubernetes configuration:
```bash
kubectl apply -f deployment.yaml
```

## API Endpoints

### GET /productos
Returns all products with optional filtering.

Query parameters:
- `nombre`: Filter products that contain this string in their name (case-insensitive)
- `precio_min`: Filter products with price greater than or equal to this value
- `precio_max`: Filter products with price less than or equal to this value

Example:
```
GET /productos?nombre=laptop&precio_min=500&precio_max=2000
```

### GET /productos/{id}
Returns a specific product by ID.

Example:
```
GET /productos/1
```

### POST /productos
Creates a new product.

Request body:
```json
{
    "nombre": "New Product",
    "precio": 299.99
}
```

### PATCH /productos/{id}
Updates an existing product.

Request body:
```json
{
    "nombre": "Updated Product Name",
    "precio": 399.99
}
```

### DELETE /productos/{id}
Deletes a product by ID.

## License

[MIT](LICENSE)

## Author

Cliber Castillo
